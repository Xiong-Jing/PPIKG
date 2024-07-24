import pandas as pd
from transformers import BertTokenizer, BertModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Define the function for calculating cosine similarity
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Define the function for calculating cosine distance
def cosine_distance(a, b):
    return 1 - cosine_similarity(a, b)

# Load BioBERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('BioBERT-Base_v1.2')
model = BertModel.from_pretrained('BioBERT-Base_v1.2',ignore_mismatched_sizes=True)

def get_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()[0]

# The function description of p53_HUMAN
text_T = "Acts as a tumor suppressor in many tumor types; induces growth arrest or apoptosis depending on the physiological circumstances and cell type (PubMed:11025664, PubMed:12524540, PubMed:12810724, PubMed:15186775, PubMed:15340061, PubMed:17189187, PubMed:17317671, PubMed:17349958, PubMed:19556538, PubMed:20673990, PubMed:20959462, PubMed:22726440, PubMed:24051492, PubMed:24652652, PubMed:9840937). Involved in cell cycle regulation as a trans-activator that acts to negatively regulate cell division by controlling a set of genes required for this process (PubMed:11025664, PubMed:12524540, PubMed:12810724, PubMed:15186775, PubMed:15340061, PubMed:17317671, PubMed:17349958, PubMed:19556538, PubMed:20673990, PubMed:20959462, PubMed:22726440, PubMed:24051492, PubMed:24652652, PubMed:9840937). One of the activated genes is an inhibitor of cyclin-dependent kinases. Apoptosis induction seems to be mediated either by stimulation of BAX and FAS antigen expression, or by repression of Bcl-2 expression (PubMed:12524540, PubMed:17189187). Its pro-apoptotic activity is activated via its interaction with PPP1R13B/ASPP1 or TP53BP2/ASPP2 (PubMed:12524540). However, this activity is inhibited when the interaction with PPP1R13B/ASPP1 or TP53BP2/ASPP2 is displaced by PPP1R13L/iASPP (PubMed:12524540). In cooperation with mitochondrial PPIF is involved in activating oxidative stress-induced necrosis; the function is largely independent of transcription. Induces the transcription of long intergenic non-coding RNA p21 (lincRNA-p21) and lincRNA-Mkln1. LincRNA-p21 participates in TP53-dependent transcriptional repression leading to apoptosis and seems to have an effect on cell-cycle regulation. Implicated in Notch signaling cross-over. Prevents CDK7 kinase activity when associated to CAK complex in response to DNA damage, thus stopping cell cycle progression. Isoform 2 enhances the transactivation activity of isoform 1 from some but not all TP53-inducible promoters. Isoform 4 suppresses transactivation activity and impairs growth suppression mediated by isoform 1. Isoform 7 inhibits isoform 1-mediated apoptosis. Regulates the circadian clock by repressing CLOCK-BMAL1-mediated transcriptional activation of PER2 (PubMed:24051492)."

df = pd.read_excel('Table3.xls')

# The embedding vector of text_T
embedding_T = get_embedding(text_T)

results = []

for index, row in df.iterrows():
	name = row['Name']
    text = row['Function']
    embedding = get_embedding(text)
    similarity = cosine_similarity(embedding_T, embedding)
    results.append({'Name': name, 'Similarity': similarity})

# Sort the results by similarity
results = sorted(results, key=lambda x: x['Similarity'], reverse=True)

# Save the results to a CSV file
results_df = pd.DataFrame(results)
results_df.to_csv('cosine_similarity_results.csv', index=False)
