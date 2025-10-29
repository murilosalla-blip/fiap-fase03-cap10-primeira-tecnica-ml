import argparse
import os
import pandas as pd
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True, help="Caminho do CSV local (Windows)")
    parser.add_argument("--out", required=True, help="Caminho do arquivo .parquet de saída")
    args = parser.parse_args()

    csv_path = args.csv
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV não encontrado: {csv_path}")

    df = pd.read_csv(csv_path, encoding="latin1")
    # Normaliza nomes de colunas
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    # Salva em parquet
    df.to_parquet(out_path, index=False)
    print(f"OK: salvo {len(df)} linhas em {out_path}")

if __name__ == "__main__":
    main()
