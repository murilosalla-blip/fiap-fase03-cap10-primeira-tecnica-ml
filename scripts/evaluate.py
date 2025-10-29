import argparse
from pathlib import Path
import joblib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

def save_fig(path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=180)
    plt.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="inp", required=True, help="Parquet (não usado aqui; mantido por simetria)")
    parser.add_argument("--assets", required=True, help="Pasta onde estão os modelos e onde salvar outputs")
    args = parser.parse_args()

    X_test = pd.read_parquet(Path(args.assets)/"X_test.parquet")
    y_test = pd.read_parquet(Path(args.assets)/"y_test.parquet")["label"]

    rows = []
    for model_path in sorted(Path(args.assets).glob("model_*.joblib")):
        bundle = joblib.load(model_path)
        pipe = bundle["pipeline"]
        name = model_path.stem.replace("model_", "")

        y_pred = pipe.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average="macro", zero_division=0)
        rec = recall_score(y_test, y_pred, average="macro", zero_division=0)
        f1 = f1_score(y_test, y_pred, average="macro", zero_division=0)
        rows.append({"model": name, "accuracy": acc, "precision_macro": prec, "recall_macro": rec, "f1_macro": f1})

        # Confusion matrix plot
        cm = confusion_matrix(y_test, y_pred, labels=sorted(y_test.unique()))
        plt.figure(figsize=(6,5))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=sorted(y_test.unique()), yticklabels=sorted(y_test.unique()))
        plt.title(f"Matriz de confusão — {name}")
        plt.xlabel("Predito")
        plt.ylabel("Verdadeiro")
        save_fig(Path(args.assets)/f"cm_{name}.png")

        # Classification report (txt)
        rep = classification_report(y_test, y_pred, zero_division=0)
        (Path(args.assets)/f"classification_report_{name}.txt").write_text(rep, encoding="utf-8")

    dfm = pd.DataFrame(rows).sort_values("f1_macro", ascending=False)
    dfm.to_csv(Path(args.assets)/"metrics_comparison.csv", index=False, encoding="utf-8")
    print("Comparativo salvo em metrics_comparison.csv")
    print(dfm)

if __name__ == "__main__":
    main()
