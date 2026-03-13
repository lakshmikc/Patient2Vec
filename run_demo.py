import torch
import torch.nn as nn
import torch.optim as optim
from pathlib import Path

from src.preprocessing import load_data
from src.tensorization import tensorize
from src.model import PatientEncoder
from src.visualization import plot_embeddings

def main():
    # Load data
    df = load_data(
        "data/sample_genomics.csv",
        "data/sample_expression.csv",
        "data/sample_clinical.csv",
    )

    patient_ids = df["patient_id"].tolist()

    # Tensorize
    g, r, c, y, clean_df = tensorize(df)
    patient_ids = clean_df["PATIENT_ID"].tolist()


    print("\nTensor shapes:")
    print("Genomics:", g.shape)
    print("Expression:", r.shape)
    print("Clinical:", c.shape)
    print("Labels:", y.shape)


    # Model
    model = PatientEncoder(
        g_dim=g.shape[1],
        r_dim=r.shape[1],
        c_dim=c.shape[1],
        embedding_dim=8,
    )

    criterion = nn.BCEWithLogitsLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    # Train
    epochs = 300
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()

        embedding, logits = model(g, r, c)
        loss = criterion(logits, y)

        loss.backward()
        optimizer.step()

        if epoch % 50 == 0 or epoch == epochs - 1:
            with torch.no_grad():
                probs = torch.sigmoid(logits)
                preds = (probs > 0.5).float()
                acc = (preds == y).float().mean().item()
            print(f"Epoch {epoch:03d} | Loss: {loss.item():.4f} | Acc: {acc:.2f}")

    # Final embeddings
    model.eval()
    with torch.no_grad():
        embedding, logits = model(g, r, c)
        probs = torch.sigmoid(logits)

    print("\nPatient-level predictions")
    for pid, prob, label in zip(patient_ids, probs.squeeze().tolist(), y.squeeze().tolist()):
        print(f"{pid}: predicted_prob={prob:.3f}, true_label={int(label)}")

    # Make figures dir if needed
    Path("figures").mkdir(exist_ok=True)

    plot_embeddings(
        embedding,
        y,
        patient_ids=patient_ids,
        save_path="figures/patient_embeddings.png",
    )

if __name__ == "__main__":
    main()

