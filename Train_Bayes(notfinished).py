#!/usr/bin/env  python
#-*- coding:utf-8 -*-
import pandas as pd
import csv
import math

Data = pd.read_csv('train.csv')
Content = Data['content']

ContentOfHealthy = Data['content'][Data['target']==0]
ContentOfLj = Data['content'][Data['target']==1]

WordForHealthy = {}
WordForLj = {}


NumberOfH = 0
NumberOfL = 0
PforOne = 1
PforZero = 1

NumberOfAll = 0
for Each in Content:
        wordarray = Each.split(' ')
        NumberOfAll += len(wordarray)


for normal in ContentOfHealthy:
        array = normal.split(' ')
        NumberOfH += len(array)
        for word in array:
          if WordForHealthy.has_key(word)==False:
                WordForHealthy[word]=1
          else:
                WordForHealthy[word]+=1
for normal in ContentOfHealthy:
        array = normal.split(' ')
        for word in array:
          WordForHealthy[word]= ((WordForHealthy[word]/NumberOfH)*(len(ContentOfLj)/len(Content)))/(WordForHealthy[word]/NumberOfAll) #P(正常邮件|出现关键词)
          PforZero *=float(WordForHealthy[word])

for spam in ContentOfLj:
        array = spam.split(' ')
        NumberOfL += len(array)
        for word in array:
          if WordForLj.has_key(word) == False:
                WordForLj[word]=1
          else:
                WordForLj[word] += 1
for spam in ContentOfLj:
        array = spam.split(' ')
        for word in array:
          WordForLj[word]= ((WordForLj[word]/NumberOfL)*(len(ContentOfLj)/len(Content)))/(WordForLj[word]/NumberOfAll) #P(垃圾邮件|出现此关键词) 
          PforOne *= WordForLj[word]

	  
	