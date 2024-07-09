import pandas as pd
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

# 读取CSV文件中的蛋白质名称
def read_protein_names(csv_file):
    # 使用pandas读取CSV文件
    df = pd.read_csv(csv_file)
    # 从DataFrame中提取'name'列的值到列表中
    protein_names = df['name'].tolist()
    return protein_names

# 调用函数，读取蛋白质名称
protein_names = read_protein_names('protein.csv')

# 加载BioBERT模型和分词器
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
model = AutoModel.from_pretrained("dmis-lab/biobert-base-cased-v1.1")

# 将蛋白质名称编码为向量
def encode_proteins(protein_names):
    encoded_inputs = tokenizer(protein_names, padding=True, truncation=True, return_tensors="pt")
    outputs = model(**encoded_inputs)
    last_hidden_states = outputs.last_hidden_state
    return torch.mean(last_hidden_states, dim=1)  # 取平均向量作为蛋白质的表示

# 计算余弦相似度
def calculate_similarity(protein_vectors):
    similarity_matrix = cosine_similarity(protein_vectors)
    return similarity_matrix

# 将蛋白质名称和它们的向量存储在DataFrame中
protein_vectors = encode_proteins(protein_names)
df = pd.DataFrame(protein_vectors, index=protein_names)

# 计算所有蛋白质名称之间的相似度
similarity_df = pd.DataFrame(calculate_similarity(df.values), index=df.index, columns=df.index)

# 根据余弦相似度排序
sorted_similarity_df = similarity_df.apply(lambda row: row.sort_values(ascending=False))

# 保存到CSV文件
sorted_similarity_df.to_csv("protein_similarity.csv")

print("相似度计算完成并保存到protein_similarity.csv")
