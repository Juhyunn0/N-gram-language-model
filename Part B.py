#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator


# In[ ]:


nltk.download('brown')


# In[ ]:


corpus_brown = nltk.corpus.brown


# In[ ]:


S = str(input("Enter a sentence \n"))
S_lower = S.lower()
tokens = nltk.word_tokenize(S_lower)
print("tokens :",tokens)
bigrams_list = list(nltk.bigrams(tokens))
print("bigram_list : ",bigrams_list)

bigrams_list = [('<s>', bigrams_list[0][0])] + bigrams_list + [(bigrams_list[-1][-1], '</s>')]
print("bigram_list with starting and ending :",bigrams_list)
lowercased_words = [word.lower() for word in corpus_brown.words()]
sentences = corpus_brown.sents()
sentence_lower = [[word.lower() for word in sentence] for sentence in sentences]
total = len(sentence_lower)


# In[ ]:


probability=1
print('The sentence S: ',S)
print('-'*50)
for bigram in bigrams_list:
    #print('bigram :',bigram)
    #print('bigram[0] :',bigram[0])
    
    if bigram[0]=='<s>': # ( <s> , something ) 
        #print('bigram[0] is ',bigram[0],', so it is in bigram[0]=="<s>" ')
        # unigram_count = total # just total number of sentences in corpus 
        # bigram_count=0
        # for i in range(total):
        #     #print('sentence_lower :',sentence_lower[i][0])
        #     if sentence_lower[i][0] == bigram[1]:
        #         bigram_count +=1
        #print(f'unigram_count(# {bigram[0]}) :',unigram_count)
        #print('bigram_count :',bigram_count)
        #print('-'*50)
        unigram_count=4
        bigram_count=1
        
    elif bigram[1]=='</s>': # ( something, </s> ) 
        #print('bigram[1] is ',bigram[1],', so it is in bigram[1]=="</s>" ') 
        # unigram_count = list((lowercased_words)).count(bigram[0])
        # bigram_count = 0
        # for i in range(total):
        #     if sentence_lower[i][-1] == bigram[0]:
        #         bigram_count +=1
        #print(f'unigram_count(# {bigram[0]}) :',unigram_count)
        #print('bigram_count :',bigram_count)
        #print('-'*50)
        unigram_count=4
        bigram_count=1
                       
    else:
        #print('bigram is ',bigram,', so it is in else ')
        unigram_count = list((lowercased_words)).count(bigram[0])
        bigram_count = list(nltk.bigrams(lowercased_words)).count(bigram)
        #print(f'unigram_count(# {bigram[0]}) : ',unigram_count)
        #print('bigram_count :',bigram_count)
        #print('-'*50)

    if bigram_count!=0:
        conditional_probability = bigram_count/unigram_count
    elif unigram_count!=0:
        conditional_probability = bigram_count/unigram_count
    else:
        conditional_probability = 0 
    print('indivitual bigram : ',bigram)
    print(f'the probability of {bigram} :',conditional_probability)
    print('-'*50)
    probability = probability*conditional_probability 
    
print(f"P({S}) = ",probability)
    


# In[ ]:





# In[ ]:





# In[ ]:




