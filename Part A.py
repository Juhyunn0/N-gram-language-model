#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator


# In[2]:


nltk.download('brown')
nltk.download('reuters')
nltk.download('stopwords')


# In[3]:


corpus_brown = nltk.corpus.brown
words_brown = corpus_brown.words()

corpus_reuters = nltk.corpus.reuters
words_reuters = corpus_reuters.words()

stopWordsCorpus = nltk.corpus.stopwords.words('english')


# In[4]:


def getFreqDist(words, stopWordsCorpus):    
    words = [w for w in words if w.lower() not in stopWordsCorpus]
    frequencyDistribution = nltk.FreqDist(word.lower() for word in words)
    frequenciesAndWords = dict()
    for word in words:
        frequenciesAndWords[word] = frequencyDistribution[word]
    frequenciesAndWords = list(frequenciesAndWords.items())
    frequenciesAndWords.sort(key = lambda a: a[1])
    frequenciesAndWords.reverse()
    return frequenciesAndWords

print("The word frequency distribution of brown corpora ")
frequenciesAndWords_brown = getFreqDist(words_brown,stopWordsCorpus)
labels_brown, frequencies_brown = map(list, zip(*frequenciesAndWords_brown))
for index in range(len(labels_brown)):
    print(labels_brown[index] , ' ', frequencies_brown[index])
    
print('-'*50)

print("The word frequency distribution of reuters corpora ")
frequenciesAndWords_reuters=getFreqDist(words_reuters, stopWordsCorpus)
labels_reuters, frequencies_reuters = map(list, zip(*frequenciesAndWords_reuters))
for index in range(len(labels_reuters)):
    print(labels_reuters[index] , ' ', frequencies_reuters[index])


# In[5]:


print("A top ten words for Brown corpora")
for index in range(10):
    print(f"{index+1}. :",labels_brown[index] , ', frequency: ', frequencies_brown[index])
print('-'*50)
print("A top ten words for Reuters corpora")
for index in range(10):
    print(f"{index+1}. :",labels_reuters[index] , ', frequency: ', frequencies_reuters[index])


# In[6]:


labels2_brown = labels_brown[:1000]
frequencies2_brown = frequencies_brown[:1000]
fig_brown, ax_brown = plt.subplots()
xs_brown = range(len(labels2_brown))


def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labels2[int(tick_val)]
    else:
        return ''


# A FuncFormatter is created automatically.
ax_brown.xaxis.set_major_formatter(format_fn)
ax_brown.xaxis.set_major_locator(MaxNLocator(integer=True))
#ax.set_yscale('log')
ax_brown.plot(xs_brown, frequencies2_brown)
ax_brown.set_title('Token frequency counts in Brown corpus ranked')
ax_brown.set_xscale('log')
ax_brown.set_yscale('log')
plt.xlabel('log(Rank)')
plt.ylabel('log(Frequency count)')
plt.show()


labels2_reuters = labels_reuters[:1000]
frequencies2_reuters = frequencies_reuters[:1000]
fig_reuters, ax_reuters = plt.subplots()
xs_reuters = range(len(labels2_reuters))


# A FuncFormatter is created automatically.
ax_reuters.xaxis.set_major_formatter(format_fn)
ax_reuters.xaxis.set_major_locator(MaxNLocator(integer=True))
#ax.set_yscale('log')
ax_reuters.plot(xs_reuters, frequencies2_reuters)
ax_reuters.set_title('Token frequency counts in Reuters corpus ranked')
ax_reuters.set_xscale('log')
ax_reuters.set_yscale('log')
plt.xlabel('log(Rank)')
plt.ylabel('log(Frequency count)')
plt.show()


# In[7]:


def getDist(words,stopWordsCorpus):
    words = [w.lower() for w in words if w.lower() not in stopWordsCorpus]
    frequencyDistribution = nltk.FreqDist(word for word in words)
    frequenciesAndWords = dict()
    for word in words:
        frequenciesAndWords[word] = frequencyDistribution[word]
    return frequenciesAndWords
frequencies_brown=getDist(words_brown,stopWordsCorpus)
frequencies_reuters=getDist(words_reuters,stopWordsCorpus)



# In[8]:


def getUnigramProb(word, frequencies):
    word = word.lower()
    total_words = sum(frequencies.values())
    if word not in frequencies:
        return 0,0
    frequency = frequencies[word]
    probability = frequency/total_words
    return probability,frequency

entropy_probability_brown,entropy_frequency_brown = getUnigramProb('quantum',frequencies_brown)
entropy_probability_reuters,entropy_frequency_reuters = getUnigramProb('quantum',frequencies_reuters)

print("The technical word : entropy \nThe unigram occurence probability of the word in Brown :",entropy_probability_brown)
print("The unigram occurrence count in Brown : ",entropy_frequency_brown)
print('-'*50)
print("The technical word : entropy \nThe unigram occurence probability of the word in Reuters :",entropy_probability_reuters)
print("The unigram occurrence count in Reuters : ",entropy_frequency_reuters)

work_probability_brown,work_frequency_brown = getUnigramProb('fine',frequencies_brown)
work_probability_reuters,work_frequency_reuters = getUnigramProb('fine',frequencies_reuters)

print('-'*50)
print("The Non-technical word : work \nThe unigram occurence probability of the word in Brown :",work_probability_brown)
print("The unigram occurrence count in Brown : ",work_frequency_brown)
print('-'*50)
print("The Non-technical word : work \nThe unigram occurence probability of the word in Reuters :",work_probability_reuters)
print("The unigram occurrence count in Reuters : ",work_frequency_reuters)


# In[ ]:





# In[ ]:




