# This is a comment in python.
# Comments can be placed anywhere in Python code and the computer ignores them - they are intended to be read by humans.
# Any line with a # in front of it is a comment.

# ------------------------- spaCy -------------------------------------
# spaCy is a Python natural language processing library specifically designed with
# the goal of being a useful library for implementing production-ready systems.
# It is particularly fast and intuitive, making it a top contender for NLP tasks.

# ------------------------- IMPORTANT -------------------------------------
#	Please make sure you have read and understand the instructions for this task.
#	We will be working with the *spaCy* which is an EXTERNAL Python module.
#	YOU MUST INSTALL IT BEFORE YOU CAN COMPLETE THIS TASK. 

# ************************** INSTALLATION **************************************
# Before doing anything, you need to have spaCy installed, as well as its English language model.

# Type the following commands in command line
# pip3 install spacy
# python3 -m spacy download en

# ======= Working with the spaCy ===== #

import spacy #This statement should work if you have spaCy installed 

nlp = spacy.load('en_core_web_sm')

sample = u"Build your data science skills to launch an in-demand, valuable career in six months."

doc = nlp(sample)

# Tokenisation

# Tokenisation is a foundational step in many NLP tasks. Tokenising text is the
# process of splitting a piece of text into words, symbols, punctuation, spaces,
# and other elements, thereby creating “tokens”. A naive way to do this is to
# simply split the string on white space:

doc.text.split()

output = ['Build', 'your', 'data', 'science', 'skills', 'to', 'launch', 'an', 'in-demand,'
, 'valuable', 'career', 'in', 'six', 'months.']

# On the surface, this looks fine. But, note that a) it disregards the punctuation and
# Put differently, it is naive, it fails to recognise elements of the text that help
# us (and a machine) to understand its structure and meaning. Let’s see how spaCy handles this:
[token.orth_ for token in doc]

output = ['Build', 'your', 'data', 'science', 'skills', 'to', 'launch', 'an', 'in', '-',
'demand', ',', 'valuable', 'career', 'in', 'six', 'months', '.']

# Here we access the each token’s .orth_ method, which returns a string representation
# of the token rather than a spaCy token object, this might not always be desirable,
# but worth noting. SpaCy recognises punctuation and is able to split these punctuation
# tokens from word tokens. Many of spaCy’s token methods offer both string and integer
# representations of processed text – methods with an underscore suffix return strings,
# methods without an underscore suffix return integers. For example:
print([(token, token.orth_, token.orth) for token in doc])

'''
output= [(Build, 'Build', 5389077834083678306),
(your, 'your', 1572612192562026184),
(data, 'data', 6645506661261177361), ]
...
'''
# If you want to avoid returning tokens that are punctuations or white space, spaCy
# provides convienient methods for this

print([token.orth_ for token in doc if not token.is_punct | token.is_space])
'''
['Build', 'your', 'data', 'science', 'skills', 'to', 'launch', 'an', 'in', 'demand',
 'valuable', 'career', 'in', 'six', 'months']
'''

# Let's identify stop words. We imported the word list above, so it's just a
# matter of iterating through the tokens stored in the Doc object and performing
# a comparison:

for word in doc:
    if word.is_stop == True:
        print(word)
'''
your
to
an
in
in
six   '''


# Lemmatisation

# A related task to tokenisation is lemmatisation. Lemmatisation is the process
# of reducing a word to its base form, its mother word if you like. Different
# uses of a word often have the same root meaning. For example, practice, practised
# and practising all essentially refer to the same thing. It is often desirable
# to standardise words with similar meaning to their base form. With spaCy we can
# access each word’s base form with a token’s .lemma_ method:

sing = "sang singing sing"
nlp_practice = nlp(sing)
print([word.lemma_ for word in nlp_practice])

''' ['sing', 'sing', 'sing'] '''

# Why is this useful? An immediate use case is in machine learning, specifically
# text classification. Lemmatising the text prior to, for example, creating a
# “bag-of-words” avoids word duplication and, therefore, allows for the model to
# build a clearer picture of patterns of word usage across multiple documents.


# Entity recognition

# Entity recognition is the process of classifying named entities found in a text
# into pre-defined categories, such as persons, places, organisations, dates,
# etc. spaCy uses a statistical model to classify a broad range of entities,
# including persons, events, works-of-art and nationalities / religions (see the
# documentation for the full list https://spacy.io/docs/usage/entity-recognition).

# For example, let’s take the first two sentences from Priyanka Chopra's wikipedia
# entry. We will parse this text, then access the identified entities using the
# Doc object’s .ents method. With this method called on the Doc we can access
# additional Token methods, specifically .label_ and .label:

wiki_priyanka = """known by her married name Priyanka Chopra Jonas, is an Indian actress,
singer, film producer, philanthropist, and the winner of the Miss World 2000 pageant.
One of India's highest-paid and most popular celebrities, Chopra has received numerous
awards, including a National Film Award and five Filmfare Awards. In 2016, the Government
of India honoured her with the Padma Shri, and Time named her one of the 100 most influential people in the world."""

nlp_priyanka = nlp(wiki_priyanka)
print([(i, i.label_, i.label) for i in nlp_priyanka.ents])

''' [(Priyanka Chopra Jonas, 'PERSON', 378), (Indian, 'NORP', 379), (
, 'GPE', 382), (2000, 'CARDINAL', 394), (
, 'GPE', 382), (One, 'CARDINAL', 394), (India, 'GPE', 382), (Chopra, 'ORG', 381), (
, 'GPE', 382), (a National Film Award, 'EVENT', 385), (five, 'CARDINAL', 394),
(Filmfare Awards, 'FAC', 9191306739292312949), (2016, 'DATE', 388), (the Government
, 'ORG', 381), (India, 'GPE', 382), (Padma Shri, 'PERSON', 378), (Time, 'ORG', 381),
(one, 'CARDINAL', 394), (100, 'CARDINAL', 394)]'''

# === Your task ==============================================================
# Let's have some 'fun'.
# Go to http://en.wikipedia.org/wiki/Garden_path_sentence and have a brief read 
# at what a 'Garden Path sentence' is (at the top) and look at the 'Examples'

# Create the file garden.py for this task.
# 1. Use some Garden Path sentences or think up your own (at least 5).
# 2. Tokenise and perform Entity recognition for each of the sentences 
#    after you have stored them in a list called gardenpathSentences.
# 3. See how spaCy has categorised these sentences and look up the entities you
#    don't understand
# 4. At the bottom of your file, write a comment about two unusual entities 
# you found that spaCy gave one of the words of your sentences - did you expect this?
