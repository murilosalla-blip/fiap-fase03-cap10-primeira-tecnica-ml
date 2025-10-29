from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def basic_eda(df: pd.DataFrame, out_dir: str):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    num_cols = ["N","P","K","temperature","humidity","pH","rainfall"]

    # Histograms
    for col in num_cols:
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribuição de {col}")
        plt.tight_layout()
        plt.savefig(f"{out_dir}/eda_dist_{col}.png", dpi=180)
        plt.close()
