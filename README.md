# Patient2Vec
Learning Multimodal Patient Representations from Omics Data- this is a lightweight framework demonstrating how heterogeneous biomedical measurements (genomics, transcriptomics, clinical traits) can be tensorized and embedded into a unified patient representation.

<img width="1408" height="768" alt="1773177153040" src="https://github.com/user-attachments/assets/38418c21-695f-4360-895a-fd3f6a530d2d" />



# Motivation

Modern biomedical datasets measure patients across many modalities (genomics, transcriptomics, imaging, clinical traits). A central challenge in AI for biomedicine is learning unified representations across these heterogeneous measurements.

This repository demonstrates a lightweight framework for tensorizing multimodal biological data and learning patient embeddings using neural networks.

# Key Concepts

multimodal data integration

representation learning

biological data tensorization

patient embeddings


# Example Workflow
Genomics + RNA-seq + Clinical

→ tensorization

→ multimodal neural network

→ patient embeddings

→ similarity analysis

# Example analysis:

Patients with high NPPA expression cluster with HF phenotypes


## 📁 Repository Structure

```
patient2vec/
│
├── README.md
├── environment.yml
│
├── data
│   ├── sample_genomics.csv
│   ├── sample_expression.csv
│   └── sample_clinical.csv
│
├── notebooks
│   ├── 01_data_tensorization.ipynb
│   ├── 02_multimodal_embedding.ipynb
│   └── 03_patient_similarity_analysis.ipynb
│
├── src
│   ├── preprocessing.py
│   ├── tensorization.py
│   ├── model.py
│   └── visualization.py
│
└── figures

```








