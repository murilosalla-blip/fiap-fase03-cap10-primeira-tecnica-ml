import argparse
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def save_fig(path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=180)
    plt.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="inp", required=True, help="Parquet de entrada")
    parser.add_argument("--assets", required=True, help="Pasta de saída de figuras")
    args = parser.parse_args()

    df = pd.read_parquet(args.inp)

    # 1) Distribuições (histograms)
    for col in ["N","P","K","temperature","humidity","pH","rainfall"]:
        plt.figure()
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribuição de {col}")
        save_fig(f"{args.assets}/eda_dist_{col}.png")

    # 2) Correlação
    plt.figure(figsize=(8,6))
    corr = df[["N","P","K","temperature","humidity","pH","rainfall"]].corr()
    sns.heatmap(corr, annot=True, fmt=".2f")
    plt.title("Matriz de correlação")
    save_fig(f"{args.assets}/eda_correlacao.png")

    # 3) Boxplots por label
    for col in ["N","P","K","temperature","humidity","pH","rainfall"]:
        plt.figure(figsize=(8,5))
        sns.boxplot(data=df, x="label", y=col)
        plt.title(f"{col} por cultura (label)")
        save_fig(f"{args.assets}/eda_boxplot_{col}_by_label.png")

    # 4) Scatter N vs P por label
    plt.figure(figsize=(6,5))
    sns.scatterplot(data=df, x="N", y="P", hue="label", alpha=0.7)
    plt.title("N vs P por cultura")
    save_fig(f"{args.assets}/eda_scatter_NxP_label.png")

    # 5) Scatter pH vs rainfall por label
    plt.figure(figsize=(6,5))
    sns.scatterplot(data=df, x="pH", y="rainfall", hue="label", alpha=0.7)
    plt.title("pH vs rainfall por cultura")
    save_fig(f"{args.assets}/eda_scatter_pH_rainfall_label.png")

    print("EDA OK — figuras salvas em", args.assets)

if __name__ == "__main__":
    main()
