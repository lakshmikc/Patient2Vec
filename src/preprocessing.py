import pandas as pd

def load_data(genomics_file, expression_file, clinical_file):
    genomics = pd.read_csv(genomics_file)
    expression = pd.read_csv(expression_file)
    clinical = pd.read_csv(clinical_file)

    # Clean patient_id consistently
    for df in [genomics, expression, clinical]:
        df["patient_id"] = (
            df["patient_id"]
            .astype(str)
            .str.strip()
            .str.upper()
        )

    print("\nGenomics patient_ids:", genomics["patient_id"].tolist())
    print("Expression patient_ids:", expression["patient_id"].tolist())
    print("Clinical patient_ids:", clinical["patient_id"].tolist())

    data = genomics.merge(expression, on="patient_id", how="inner")
    data = data.merge(clinical, on="patient_id", how="inner")

    print("\nMerged data shape:", data.shape)
    print("Merged columns:", data.columns.tolist())
    print(data.head())

    if data.empty:
        raise ValueError(
            "Merged dataframe is empty. Check that patient_id values match across all input CSV files."
        )

    return data

