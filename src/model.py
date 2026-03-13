import torch
import torch.nn as nn

class PatientEncoder(nn.Module):
    def __init__(self, g_dim: int, r_dim: int, c_dim: int, embedding_dim: int = 8):
        super().__init__()

        self.genomics = nn.Sequential(
            nn.Linear(g_dim, 16),
            nn.ReLU(),
            nn.Linear(16, 16),
            nn.ReLU(),
        )

        self.rna = nn.Sequential(
            nn.Linear(r_dim, 16),
            nn.ReLU(),
            nn.Linear(16, 16),
            nn.ReLU(),
        )

        self.clinical = nn.Sequential(
            nn.Linear(c_dim, 8),
            nn.ReLU(),
            nn.Linear(8, 8),
            nn.ReLU(),
        )

        self.fusion = nn.Sequential(
            nn.Linear(16 + 16 + 8, 16),
            nn.ReLU(),
            nn.Linear(16, embedding_dim),
        )

        self.classifier = nn.Sequential(
            nn.Linear(embedding_dim, 8),
            nn.ReLU(),
            nn.Linear(8, 1),
        )

    def forward(self, g: torch.Tensor, r: torch.Tensor, c: torch.Tensor):
        g_emb = self.genomics(g)
        r_emb = self.rna(r)
        c_emb = self.clinical(c)

        fused = torch.cat([g_emb, r_emb, c_emb], dim=1)
        embedding = self.fusion(fused)
        logits = self.classifier(embedding)

        return embedding, logits

