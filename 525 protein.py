import gensim
from gensim.models import word2vec
from sklearn.decomposition import PCA
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Load wikipedia-pubmed-and-PMC-w2v model
model = gensim.models.KeyedVectors.load_word2vec_format("wikipedia-pubmed-and-PMC-w2v.bin", binary=True)
# Get the raw word vectors
raw_word_vec = model.wv.vectors
# Load a list of words
words = open("words.txt", encoding="utf-8").readlines()
# Remove newline characters from each word
words = [word.replace("\n", "") for word in words]

# Load a list of word unions
wordList = open("union.txt", encoding="utf-8").readlines()
wordList = [word.replace("\n", "").split('_')[0] for word in wordList]
# Get unique words that are present in both the model's vocabulary and the word list
wordList = list(set(wordList) & set(words))
print(len(wordList))  # Print the number of unique words

# get the index of a word in the model's vocabulary
def get_word_index(word):
    index = model.wv.vocab[word].index
    return index

# Create a map of word indices for the filtered word list
index_map = map(get_word_index, wordList)

# Print the first raw word vector
print(raw_word_vec[0])

# Reduce the dimensionality of the word vectors to 2 components using PCA
vec_reduced = PCA(n_components=2).fit_transform(raw_word_vec)

x = np.arange(-10, 10, 0.1)
y = x
plt.plot(x, y)

# Annotate words on the plot
for i in index_map:
    if model.wv.index2word[i] == "PI3K" or model.wv.index2word[i] == "akt":
        plt.text(vec_reduced[i][0], vec_reduced[i][1], model.wv.index2word[i], color='green')
    else:
        plt.text(vec_reduced[i][0], vec_reduced[i][1], model.wv.index2word[i], color='r')

# Display the plot
plt.show()

'''

# Initialize a list to hold filtered words
filtWordList = []
# Initialize a dictionary to hold word positions
position_dict = {}

index_list = list(index_map)
# Store the positions of each word in the dictionary
for i in index_list:
    position_dict[model.wv.index2word[i]] = (vec_reduced[i][0], vec_reduced[i][1])

# Function to calculate the Euclidean distance between two words
def getDistance(fromWord, toWord):
    return (position_dict[fromWord][0]-position_dict[toWord][0])*(position_dict[fromWord][0]-position_dict[toWord][0]) + (position_dict[fromWord][1]-position_dict[toWord][1])*(position_dict[fromWord][1]-position_dict[toWord][1])

# Calculate the base distance between "P53" and "UBP7"
baseDistance = float(getDistance("P53", "UBP7"))

# Filter words based on their distance from "P53"
for i in index_list:
    i_distance = float(getDistance(model.wv.index2word[i], "P53"))
    if i_distance <= baseDistance:
        filtWordList.append(model.wv.index2word[i])

# Save the filtered words to a file
with open("filt word.txt", "a", encoding="utf-8") as fw:
    for word in filtWordList:
        fw.write(word + "\n")
fw.close()
'''