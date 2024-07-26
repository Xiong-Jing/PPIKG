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
tokenizer = BertTokenizer.from_pretrained('biobert_v1.0_pubmed_pmc')
model = BertModel.from_pretrained('biobert_v1.0_pubmed_pmc',ignore_mismatched_sizes=True)

def get_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()[0]

# p53_HUMAN
text_T = 'P53_HUMAN'

# read Excel
df = pd.read_excel('protein.xls')

# The embedding vector of text_T
embedding_T = get_embedding(text_T)

# to save similarity results
results = []

for index, row in df.iterrows():
    name = row['Name']
    # text = name.split('_')[0]
    embedding = get_embedding(name)
    similarity = cosine_similarity(embedding_T, embedding)
    results.append({'Name': name, 'Similarity': similarity})

# Sort the results by similarity
results = sorted(results, key=lambda x: x['Similarity'], reverse=True)

# Save the results to a CSV file
results_df = pd.DataFrame(results)
results_df.to_csv('cosine_similarity_results23.csv', index=False)
