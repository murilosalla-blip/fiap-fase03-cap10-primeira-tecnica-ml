import argparse
import yaml
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import joblib

MODEL_MAP = {
    "KNeighborsClassifier": KNeighborsClassifier,
    "LogisticRegression": LogisticRegression,
    "DecisionTreeClassifier": DecisionTreeClassifier,
    "RandomForestClassifier": RandomForestClassifier,
    "SVC": SVC,
}

def build_pipeline(model_type, params, scale_features=True):
    model_cls = MODEL_MAP[model_type]
    model = model_cls(**(params or {}))
    steps = []
    if scale_features and model_type in ["KNeighborsClassifier", "LogisticRegression", "SVC"]:
        steps.append(("scaler", StandardScaler()))
    steps.append(("model", model))
    return Pipeline(steps)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="inp", required=True, help="Parquet de entrada")
    parser.add_argument("--assets", required=True, help="Pasta para salvar modelos/artefatos")
    parser.add_argument("--config", default="config/settings.yaml", help="YAML de configuração")
    args = parser.parse_args()

    cfg = yaml.safe_load(open(args.config, "r", encoding="utf-8"))
    df = pd.read_parquet(args.inp)

    X = df[cfg["features"]]
    y = df[cfg["target"]]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=cfg["test_size"], random_state=cfg["random_state"], stratify=y
    )

    Path(args.assets).mkdir(parents=True, exist_ok=True)

    for m in cfg["models"]:
        pipe = build_pipeline(m["type"], m.get("params"), cfg["scale_features"])
        pipe.fit(X_train, y_train)
        out = Path(args.assets) / f"model_{m['name']}.joblib"
        joblib.dump({"pipeline": pipe, "features": cfg["features"], "target": cfg["target"]}, out)
        print("Salvo:", out)

    # guarda também os conjuntos para avaliação
    X_train.to_parquet(Path(args.assets)/"X_train.parquet", index=False)
    y_train.to_frame("label").to_parquet(Path(args.assets)/"y_train.parquet", index=False)
    X_test.to_parquet(Path(args.assets)/"X_test.parquet", index=False)
    y_test.to_frame("label").to_parquet(Path(args.assets)/"y_test.parquet", index=False)

if __name__ == "__main__":
    main()
