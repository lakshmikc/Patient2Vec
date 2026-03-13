import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(42)
n = 50

patient_ids = [f"P{i+1}" for i in range(n)]
hf_label = np.random.binomial(1, 0.5, n)

genomics = pd.DataFrame({
    "patient_id": patient_ids,
    "SNP1": np.random.randint(0, 3, n),
    "SNP2": np.random.randint(0, 3, n),
    "SNP3": np.random.randint(0, 3, n),
    "SNP4": np.random.randint(0, 3, n),
})

expression = pd.DataFrame({
    "patient_id": patient_ids,
    "NPPA": np.where(hf_label == 1, np.random.normal(5.5, 0.7, n), np.random.normal(1.5, 0.4, n)),
    "NPPB": np.where(hf_label == 1, np.random.normal(4.8, 0.6, n), np.random.normal(1.2, 0.3, n)),
    "GATA4": np.random.normal(2.3, 0.3, n),
    "MYH7": np.where(hf_label == 1, np.random.normal(3.5, 0.4, n), np.random.normal(2.0, 0.3, n)),
})

clinical = pd.DataFrame({
    "patient_id": patient_ids,
    "BMI": np.where(hf_label == 1, np.random.normal(32, 3, n), np.random.normal(25, 2, n)).round(1),
    "Age": np.where(hf_label == 1, np.random.normal(66, 6, n), np.random.normal(48, 7, n)).round().astype(int),
    "SBP": np.where(hf_label == 1, np.random.normal(145, 8, n), np.random.normal(120, 7, n)).round().astype(int),
    "hf_label": hf_label,
})

Path("data").mkdir(exist_ok=True)
genomics.to_csv("data/sample_genomics.csv", index=False)
expression.to_csv("data/sample_expression.csv", index=False)
clinical.to_csv("data/sample_clinical.csv", index=False)

print("Synthetic data written to data/")

