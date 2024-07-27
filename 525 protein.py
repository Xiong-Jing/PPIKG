import gensim

from gensim.models import word2vec
from sklearn.decomposition import PCA
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

model = gensim.models.KeyedVectors.load_word2vec_format("wikipedia-pubmed-and-PMC-w2v.bin", binary=True)
raw_word_vec = model.wv.vectors
words = open("words.txt", encoding="utf-8").readlines()
words = [word.replace("\n", "") for word in words]




wordList = open("union.txt", encoding="utf-8").readlines()
wordList = [word.replace("\n", "").split('_')[0] for word in wordList]
wordList = list(set(wordList) & set(words))
print(len(wordList))

def get_word_index(word):
    index = model.wv.vocab[word].index
    return index

index_map = map(get_word_index, wordList)

print(raw_word_vec[0])



vec_reduced = PCA(n_components=2).fit_transform(raw_word_vec)
x = np.arange(-10, 10, 0.1)
y = x
plt.plot(x, y)


for i in index_map:
    if model.wv.index2word[i] == "PI3K" or model.wv.index2word[i] == "akt":
        plt.text(vec_reduced[i][0], vec_reduced[i][1], model.wv.index2word[i], color='green')
    else:
        plt.text(vec_reduced[i][0], vec_reduced[i][1], model.wv.index2word[i], color='r')


plt.show()



'''
filtWordList = []
position_dict = {}
index_list = list(index_map)
for i in index_list:
    position_dict[model.wv.index2word[i]] = (vec_reduced[i][0], vec_reduced[i][1])

def getDistance(fromWord, toWord):
    return (position_dict[fromWord][0]-position_dict[toWord][0])*(position_dict[fromWord][0]-position_dict[toWord][0]) + (position_dict[fromWord][1]-position_dict[toWord][1])*(position_dict[fromWord][1]-position_dict[toWord][1])

baseDistance = float(getDistance("P53", "UBP7"))

for i in index_list:
    i_distance = float(getDistance(model.wv.index2word[i], "P53"))
    if i_distance <= baseDistance:
        filtWordList.append(model.wv.index2word[i])

with open("filt word.txt", "a", encoding="utf-8") as fw:
    for word in filtWordList:
        fw.write(word + "\n")
fw.close()
'''

