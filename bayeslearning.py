#-*- coding:utf-8 -*-
from numpy import *
def loadDataSet():
	postingList=[['my','dog','has','flea', \
					'problems','help','please'],
					['maybe','not','take','him', \
					'to','dog','park','stupid'],
					['my','dalmation','is','so','cute', \
					'I', 'love', 'him'],
					['stop','posting','stupid','worthless','garbage'],
					['mr','licks','ate','my','steak','how',\
					'to','stop', 'him'],
					['quit', 'buying', 'worthless', 'dog', 'food','stupid']]
	classVec = [0,1,0,1,0,1] #1 represent 侮辱性 0 represent 正常言论
	return postingList,classVec

def createVocabList(dataSet):	#创立一个空集
	vocabSet = set([]) #返回一个不重复词表
	for document in dataSet:
		vocabSet = vocabSet | set(document) #创建两个集合的并集
	return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
	returnVec = [0]*len(vocabList) #创建一个所有向量都为0的集
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] = 1
		else : print "the word: %s is not in my Vocabulary!" % word
	return returnVec
	
def trainNBO(trainMatrix,trainCategory):
	numTrainDocs = len(trainMatrix)
	numWords = len(trainMatrix[0])
	pAbusive = sum(trainCategory)/floa   t(numTrainDocs)
	p0Num = zeros(numWords); p1Num = zeros(numWords)
	p0Denom = 0.0; p1Denom = 0.0 #初始化概率
	for i in range(numTrainDocs):
		if trainCategory[i] == 1:   #该份文档中出现垃圾词汇 垃圾词汇数组中该文档所有单词次数+1
			p1Num += trainMatrix[i]
			p1Denom += sum(trainMatrix[i])
		else:
			p0Num += trainMatrix[i]
			p0Denom += sum(trainMatrix[i])
	p1Vect = p1Num/p1Denom	#该文档的词汇次数除以总个数
	p0Vect = p0Num/p0Denom
	return p0Vect,p1Vect,pAbusive
	
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
	p1 = sum(vec2Classify * p1Vec) + log(pClass1)
	p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
	if p1>p0:
		return 1
	else:
		return 0
		
def testingNB():
	listOPosts,listClasses = loadDataSet()
	myVocabList = createVocabList(listOPosts)
	trainMat = []
	for postingDoc in listOPosts:
		trainMat.append(setOfWords2Vec(myVocabList, postingDoc))
	p0V,p1V,pAb = trainNBO(array(trainMat),array(listClasses))
	testEntry = ['love','my','dalmation']
	thisDoc = array(setOfWords2Vec(myVocabList, testEntry))#返回一个分类的词向量
	print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)
	testEntry = ['stupid','garbage']
	thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
	print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)
	