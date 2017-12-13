#encoding:utf-8

import json
from datetime import datetime,timedelta
from pprint import pprint
from random import randint

from gensim.models import Doc2Vec
from util import LabeledLineSentence

from sklearn.linear_model import LogisticRegression
import numpy

closed = [] 
articles = []
sources = { 'data-pos.txt':'pos','data-neg.txt':'neg' }
sentences = LabeledLineSentence(sources)

closed = [1,1,1,1,1] + [0,0,0,0,0] #positive + negative

# doc 2 vec model training
model = Doc2Vec(min_count=1, window=2, size=10, sample=1e-4, negative=5)
model.build_vocab(sentences.to_array())

for epoch in range(10):
    model.train(sentences.sentences_perm())

model.save('./test.d2v')

train_arrays = numpy.zeros( (10, 10) )
train_labels = closed 
for i in range(5):
    train_arrays[i] = model.docvecs['pos_{}'.format(i)] #positive vectors
    train_arrays[i+5] = model.docvecs['neg_{}'.format(i)] #negative vectors

classifier = LogisticRegression()
classifier.fit(train_arrays, train_labels)

print(classifier.score(train_arrays, train_labels))
