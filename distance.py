import gensim
import csv

model = gensim.models.KeyedVectors.load_word2vec_format("wikipedia-pubmed-and-PMC-w2v.bin", binary=True)
vectors = model.vectors
vocab = model.vocab

def get_distance(firstPosition, secondPosition):
    sum = 0
    for i in range(len(firstPosition)):
        short = firstPosition[i] - secondPosition[i]
        sum += short * short
    return sum

'''
position_dict = {}
with open("157_2.csv", encoding="utf-8") as fr:
    reader = csv.DictReader(fr)
    for row in reader:
        name = row["name"].split("_")[0].upper()
        try:
            vocab_index = vocab[name].index
            vector = vectors[vocab_index]
            position_dict[name] = vector
        except:
            pass
fr.close()
'''

position_dict = {}
with open("union.txt", encoding="utf-8") as fr:
    protein_list = fr.readlines()
    protein_list = [protein.replace("\n", "") for protein in protein_list]
    for protein in protein_list:
        name = protein.split("_")[0].upper()
        try:
            vocab_index = vocab[name].index
            vector = vectors[vocab_index]
            position_dict[name] = vector
        except:
            pass
fr.close()


PI3K_position = vectors[vocab["AKT".upper()].index]

for key,value in position_dict.items():
    distance = get_distance(value, PI3K_position)
    with open("AKT distance.txt", "a", encoding="utf-8") as fw:
        fw.write(key + "\t" + str(distance) + "\n")
    fw.close()


print("All Done!!!")



