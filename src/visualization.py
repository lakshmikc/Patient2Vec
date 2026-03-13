import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def plot_embeddings(embeddings, labels, patient_ids=None, save_path=None):
    reduced = PCA(n_components=2).fit_transform(embeddings.detach().cpu().numpy())
    labels_np = labels.detach().cpu().numpy().flatten()

    save_path="figures/patient_embeddings.png"
    plt.figure(figsize=(7, 5))
    scatter = plt.scatter(reduced[:, 0], reduced[:, 1], c=labels_np)

    if patient_ids is not None:
        for i, pid in enumerate(patient_ids):
            plt.annotate(pid, (reduced[i, 0], reduced[i, 1]), fontsize=8)

    plt.title("Patient Embedding Space")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.colorbar(scatter, label="HF Label")

    if save_path:
        plt.savefig(save_path, dpi=200, bbox_inches="tight")

    plt.show()

