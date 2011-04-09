#!/usr/bin/env python
import os, os.path
import nltk
from nltk.corpus import senseval

path = os.path.relpath('nltk_data')
nltk.data.path[0]=path

items = senseval.fileids()
print items

items = items[:1]

for item in items:
	train=[]
	for instance in senseval.instances(item)[:10]:
		pos = instance.position
		context = instance.context
		senses = instance.senses

		d={}
		d['prev_word']=context[pos-1]
		d['next_word']=context[pos+1]
		for sense in senses:
			pair = (d,sense)
			train.append(pair)
			(feature_set, label) = pair
	test = []
	for instance in senseval.instances(item)[10:20]:
		pos = instance.position
		context = instance.context
		senses = instance.senses

		d={}
		d['prev_word']=context[pos-1]
		d['next_word']=context[pos+1]
		test.append(d)

#train2 = [
#    (dict(a=1,b=1,c=1), 'y'),
#    (dict(a=1,b=1,c=1), 'x'),
#    (dict(a=1,b=1,c=0), 'y'),
#    (dict(a=0,b=1,c=1), 'x'),
#    (dict(a=0,b=1,c=1), 'y'),
#    (dict(a=0,b=0,c=1), 'y'),
#    (dict(a=0,b=1,c=0), 'x'),
#    (dict(a=0,b=0,c=0), 'x'),
#    (dict(a=0,b=1,c=1), 'y'),
#    ]
#test = [
#    (dict(a=1,b=0,c=1)), # unseen
#    (dict(a=1,b=0,c=0)), # unseen
#    (dict(a=0,b=1,c=1)), # seen 3 times, labels=y,y,x
#    (dict(a=0,b=1,c=0)), # seen 1 time, label=x
#    ]
#
classifier = nltk.NaiveBayesClassifier.train(train)
senseList = classifier.batch_classify(test)

#file writing stuff.  Will not work in the initial implementation.
#requires all of words to have a sense
f = open('answers.txt')
out = open('responses.txt', 'w')
l = []
for line in f:
  l.append(line)
for x in range(len(senseList)):
  out.write(l[x].rstrip().rstrip('\n') + " " + senseList[x] + '\n')
f.close()
out.close()
print senseList
print classifier.show_most_informative_features()
