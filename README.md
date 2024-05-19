# N-gram language model

**Summary**
These tasks involve utilizing Python's NLTK package along with the Brown corpus to perform various language modeling and text analysis tasks. From analyzing word frequency distributions to calculating probabilities based on N-gram models, these tasks aim to explore the linguistic properties of the corpus and provide interactive features for user input and exploration.

## Part A
NLTK Word Frequency Analysis and Probability Calculation
1. Word Frequency Distribution: Utilize Python's NLTK package to analyze the Brown and Reuters corpora. Remove stop words using the stopwords corpora and obtain the word frequency distribution for both corpora.
2. Top Ten Words: Display the top ten words (ranks 1 through 10) for both corpora on screen and place them in a table.
3. Log(Rank) vs Log(Frequency) Plots: Generate log(rank) vs log(frequency) plots for the first 1000 words (ranks 1 through 1000) for both corpora using a plotting package like Matplotlib. Place both plots in a table.
4. Unigram Occurrence Probability: Calculate the unigram occurrence probability for two specific words ("technical" and not technical) using the frequency counts obtained earlier. Display all relevant counts and probabilities on screen and enter final values in the table.
## Part B
1. N-gram Language Model Calculation
2. User Input Sentence: Prompt the user to enter a sentence S from the keyboard.
3. Lowercasing: Apply lowercasing to the input sentence S.
4. Calculate P(S): Calculate the probability P(S) assuming a 2-gram language model, where the probability of any bigram starting or ending a sentence is 0.25.
5. Display Results: Display the sentence S, list all the individual bigrams and their probabilities, and the final probability P(S) on screen.
## Part C
1. N-gram Language Model with User Interaction
2. Initial Word Entry: Start by asking the user for the initial word/token W1 and apply lowercasing to W1 and all future entries. If the word is not in the corpus, offer options to ask again or quit.
3. Menu with Top 3 Likely Words: Assuming a 2-gram language model, present a menu with the top 3 most likely words to follow W1, according to the W1-NEXT WORD probability estimate.
4. Repeat Sentence Construction: Repeat the process of selecting subsequent word choices to construct a sentence until the user selects to quit.
