import warnings
warnings.filterwarnings('ignore',
	category=UserWarning)
import nltk.tokenize as tk
import nltk.corpus as nc
import nltk.stem.snowball as sb
import gensim.models.ldamodel as gm
import gensim.corpora as gc
doc = []
with open('../../data/topic.txt', 'r') as f:
	for line in f.readlines():
		doc.append(line[:-1])
print(len(doc))