import gensim
import csv

# Load wikipedia-pubmed-and-PMC-w2v model
model = gensim.models.KeyedVectors.load_word2vec_format("wikipedia-pubmed-and-PMC-w2v.bin", binary=True)
# Access the model's vectors and vocabulary
vectors = model.vectors
vocab = model.vocab

# calculate the squared Euclidean distance between two vectors
def get_distance(firstPosition, secondPosition):
    sum = 0
    for i in range(len(firstPosition)):
        short = firstPosition[i] - secondPosition[i]
        sum += short * short
    return sum

'''

# Initialize a dictionary to hold word positions
position_dict = {}
# Open a CSV file and read its contents
with open("157_2.csv", encoding="utf-8") as fr:
    reader = csv.DictReader(fr)
    for row in reader:
        name = row["name"].split("_")[0].upper()
        try:
            # Get the index of the word in the vocabulary and its vector
            vocab_index = vocab[name].index
            vector = vectors[vocab_index]
            position_dict[name] = vector
        except:
            pass
fr.close()
'''

# Initialize a dictionary to hold protein positions
position_dict = {}
# Open and read union contents
with open("union.txt", encoding="utf-8") as fr:
    protein_list = fr.readlines()
    protein_list = [protein.replace("\n", "") for protein in protein_list]
    for protein in protein_list:
        name = protein.split("_")[0].upper()
        try:
            # Get the index of the protein in the vocabulary and its vector
            vocab_index = vocab[name].index
            vector = vectors[vocab_index]
            position_dict[name] = vector
        except:
            pass
fr.close()

# Get the position vector of AKT
PI3K_position = vectors[vocab["AKT".upper()].index]

# Calculate and save the distance from AKT for each protein in the dictionary
for key, value in position_dict.items():
    distance = get_distance(value, PI3K_position)
    with open("AKT distance.txt", "a", encoding="utf-8") as fw:
        fw.write(key + "\t" + str(distance) + "\n")
    fw.close()

# Print a completion message
print("All Done!!!")