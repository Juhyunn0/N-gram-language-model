#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator


# In[2]:


nltk.download('brown')
corpus_brown = nltk.corpus.brown
words_brown = corpus_brown.words()
stopWordsCorpus = nltk.corpus.stopwords.words('english')
words = [w for w in words_brown if w.lower() not in stopWordsCorpus]
lowercased_words = [word.lower() for word in words]


# In[5]:

def getNext(W_lower, lowercased_words, bigram_FreqDist):
    unigram_count = list((lowercased_words)).count(W_lower)
    bigram_count_dic = {}
    for word in lowercased_words:
        bigram_T = (W_lower,word)
        #print("bigram_T :",bigram_T)
        if bigram_T in bigram_FreqDist:
            bigram_count_dic[bigram_T] = bigram_FreqDist[bigram_T]

    sorted_bigram_count = sorted(bigram_count_dic.items(), key=lambda x: x[1], reverse=True)

    if len(sorted_bigram_count)>=3:
        follow_1, bigram_count_1 = sorted_bigram_count[0]
        follow_2, bigram_count_2 = sorted_bigram_count[1]
        follow_3, bigram_count_3 = sorted_bigram_count[2]

        prob_1 = bigram_count_1/unigram_count
        prob_2 = bigram_count_2/unigram_count
        prob_3 = bigram_count_3/unigram_count

        prob = [prob_1,prob_2,prob_3]
    else:
        follow=[]
        for i in range(len(sorted_bigram_count)):
            follow.append(sorted_bigram_count[i][0][-1])
            prob.append(sorted_bigram_count[i][-1]/unigram_count)
        return follow,prob
        
            

    return [follow_1[-1],follow_2[-1],follow_3[-1]],prob



while True:
    W = str(input("Enter initial word/token W1 \n"))
    W_lower = W.lower()
    if W_lower not in lowercased_words:
        print('The word is NOT in the corpus.')
        answer = str(input("a. ask again \n b. QUIT \n"))
        if answer =='b':
            print("END")
            break
        elif answer !='a':
            print("Invalid option")
            break     

    else:
        S=[W_lower]
        bigram_FreqDist = nltk.FreqDist(nltk.bigrams(lowercased_words))
        while True:
            follow_list,prob = getNext(W_lower, lowercased_words, bigram_FreqDist)
            for i in range(len(S)):
                print(S[i],end=' ')
            print(' ...')
            #print("W_lower :",W_lower)
            for i in range(len(prob)):
                print(f'{i+1}) {follow_list[i]} P({W_lower} {follow_list[i]}) =',prob[i])

            print('4) QUIT')
            choice = str(input())
            if choice =='4':
                print('QUIT')
                break
            elif choice not in ['1','2','3']:
                print('You pick a number other than 1,2,3, and 4, so assume your choice is 1')
                S.append(follow_list[0])
                W_lower= follow_list[0]
            else:
                print(f'You pick {choice}')
                S.append(follow_list[int(choice)-1])
                W_lower =follow_list[int(choice)-1]    
        #print(sorted_bigram_count) 
        break





    


# In[ ]:




