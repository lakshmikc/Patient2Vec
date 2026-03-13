import pandas as pd
import torch

def tensorize(df):
    genomics_cols = ["SNP1", "SNP2", "SNP3", "SNP4"]
    clinical_cols = ["BMI", "AGE", "SBP"]

    df = df.copy()
    df.columns = [c.strip().upper() for c in df.columns]

    genomics_cols = [c for c in genomics_cols if c in df.columns]
    clinical_cols = [c for c in clinical_cols if c in df.columns]
    expression_candidates = ["NPPA", "NPPB", "GATA4", "MYH7"]
    expression_cols = [c for c in expression_candidates if c in df.columns]

    print("\nUsing genomics columns:", genomics_cols)
    print("Using expression columns:", expression_cols)
    print("Using clinical columns:", clinical_cols)

    if len(genomics_cols) == 0:
        raise ValueError("No genomics columns found.")
    if len(expression_cols) == 0:
        raise ValueError("No expression columns found.")
    if len(clinical_cols) == 0:
        raise ValueError("No clinical columns found.")
    if "HF_LABEL" not in df.columns:
        raise ValueError("hf_label column not found in clinical data.")

    needed_cols = genomics_cols + expression_cols + clinical_cols + ["HF_LABEL"]
    for col in needed_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    if df[needed_cols].isnull().any().any():
        print("\nWarning: Missing values detected. Dropping rows with NA.")
        df = df.dropna(subset=needed_cols)

    if df.empty:
        raise ValueError("No rows remaining after numeric conversion / NA filtering.")

    g = torch.tensor(df[genomics_cols].values, dtype=torch.float32)
    r = torch.tensor(df[expression_cols].values, dtype=torch.float32)
    c = torch.tensor(df[clinical_cols].values, dtype=torch.float32)
    y = torch.tensor(df["HF_LABEL"].values, dtype=torch.float32).unsqueeze(1)

    return g, r, c, y, df

