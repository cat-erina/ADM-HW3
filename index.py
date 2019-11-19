# index.py

import json
import numpy as np
import pandas as pd
import os
import csv
import itertools
import re
import csv
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from itertools import chain
from collections import defaultdict
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics.pairwise import cosine_similarity    
import operator

ps = PorterStemmer()
attr = ['Intro', 'Plot']
stop = set(stopwords.words('english'))

# The path to my tsv file
paths = '/Users/yves/Desktop/Data_Science/first_year/first_semester/adm/adm_hw3/tsv_files/'

# I will start by creating a Vocabulary

good_ict = {}
Vocabulary = list()

for filename in os.listdir(paths): # go through all the files in the folder
    if filename.endswith(".tsv"): # take only the tsv
        page_name = filename.rstrip('.tsv') # save the same without extension

        words = [] # this list will contain all the words found in the Intro and Plot
        with open(paths+filename) as fd: # we open the tsv file
            rd = csv.reader(fd, delimiter="\t", quotechar='"')
            for row in rd:  # read each line
                if row[0] in attr:  # if the first column is Intro or Plot, look at the second column
                    for word in row[1].strip().split(): # clean the word
                        word_cl1 = re.sub(r'[^\w\s]','',word)
                        word_cl1 = word_cl1.lower()
                        if word_cl1 not in stop: # check if it is a stop word
                            stemmed_word = ps.stem(word_cl1) # stem the word
                            words.append(stemmed_word) # at the word to the list of words of the file
        words = list(set(words))
        for clean_word in words:
            if clean_word not in Vocabulary:
                Vocabulary.append(clean_word)
            else:
                continue
        for clean_word in words: 
            term_id = Vocabulary.index(clean_word)
            if str(term_id) not in good_dict.keys():
                good_dict[str(term_id)] = [filename]
            else:
                if filename in good_dict[str(term_id)]:
                    continue
                else:
                    good_dict[str(term_id)].append(filename)

print('Done')



## CHECK FOR ALL THE FILES CONTIAINING *ALL* THE WORDS IN THE QUERY
lst = []
for word in query:
    if word in Vocabulary:
        term_id = Vocabulary.index(word)
        docs = good_dict[str(term_id)]
        if docs is None or len(docs) == 0:
            continue
        else:
            for i in docs:
                lst.append(i)
result=[]
for i in lst:
    if lst.count(i) >= len(initial_query)-1:
         result.append(i)
result = list(set(result))




# print the the result

# for each movie we extracted the Name, Intro and Url from the respective tsv
to_df = []
for movie in result:
    element_in_movie = {}
    with open(path+movie) as fd:
        rd = csv.reader(fd, delimiter="\t", quotechar='"')
        for row in rd:
            if row[0] == 'Name':
                element_in_movie['Name'] = row[1]
            elif row[0] == 'Intro':
                element_in_movie['Intro'] = row[1]
            elif row[0] == 'Url':
                element_in_movie['Url'] = row[1]
    to_df.append(element_in_movie)
df = pd.DataFrame(to_df)
df = df.reindex(('Name', 'Intro', 'Url'), axis=1)
df


## CREATE THE INVERTED INDEX

# for each word in the Vocabulary, we will go though the documents havving that word and we will
# compute the tdidf of that word in that in the document.

lst = list(Dict.keys()) # the list of words in my vocabulary
len_dict = len(os.listdir(path)) # the number of all my files
New_Dict = {} # the dictionary that will contain the inverted indexes

for term_id in good_dict:  # for each word in the dictionary
    val_word = list(good_dict[term_id]) # we save the number of documents having that word
    for doc in good_dict[term_id]:  # we go through each document
        file = [] # here we will save the the words contained in the document
        with open(paths+doc) as fd:
            rd = csv.reader(fd, delimiter="\t", quotechar='"')
            for row in rd:
                if row[0] in attr:
                    for word in row[1].strip().split():
                        if word == 'NA':
                            continue
                        else:
                            word_cl1 = re.sub(r'[^\w\s]','',word)
                            word_cl1 = word_cl1.lower()
                            if word_cl1 not in stop:
                                stemmed_word = ps.stem(word_cl1)
                                file.append(stemmed_word)
        if len(file) < 1:
            if word in New_Dict.keys():  # add the word to the new dictioary if the word is not already inside and add the new value if the word is already inside
                New_Dict[word].append((doc, 0))
            else:
                New_Dict[word] = [(doc, 0)]
        else:
            len_file = len(file) # the total number of words
            word = Vocabulary[int(term_id)]
            count = file.count(word) # the number of times that word is repeated in the document
            tf = round(count/len_file, 4) # the frequency of the word in the document
            idf = np.log(len_dict/len(val_word)) # the IDF 
            if term_id in New_Dict.keys():  # add the word to the new dictioary if the word is not already inside and add the new value if the word is already inside
                New_Dict[term_id].append((doc, tf*idf))
            else:
                New_Dict[term_id] = [(doc, tf*idf)]

## GET THE INVERTED INDEX OF THE QUERY

tf_idf_query = tf_idf_query(query) # this function is in index_utils.py



i = []
ps = PorterStemmer()
stop = set(stopwords.words('english'))
len_dict = len(os.listdir(path))
attr = ['Plot', 'Intro']
important = ['Directed by', 'Produced by', 'Written by', 'Screenplay by',
           'Story by', 'Based on', 'Starring', 'Narrated by', 'Music by',
           'Cinematography', 'Edited by', 'Production company', 
            'Distributed by',  'Country',
           'Language']

New_Dict = {}
for term_id in good_dict.keys():
    val_word = list(good_dict[term_id])
    for doc in good_dict[term_id]:

        intro_plot = []
        important1 =[]
        title = []
        with open(path+doc) as fd:
            rd = csv.reader(fd, delimiter="\t", quotechar='"')
            for row in rd:
                if row[0] in attr:
                    for word in row[1].strip().split():
                        if word == 'NA':
                            continue
                        else:
                            word_cl1 = re.sub(r'[^\w\s]','',word)
                            word_cl1 = word_cl1.lower()
                            if word_cl1 not in stop:
                                stemmed_word = ps.stem(word_cl1)
                                intro_plot.append(stemmed_word)
                elif row[0] in important:
                    for word in row[1].strip().split():
                        if word == 'NA':
                            continue
                        else:
                            word_cl1 = re.sub(r'[^\w\s]','',word)
                            word_cl1 = word_cl1.lower()
                            if word_cl1 not in stop:
                                stemmed_word = ps.stem(word_cl1)
                                important1.append(stemmed_word)
                elif row[0] == 'Title':
                    for word in row[1].strip().split():
                        if word == 'NA':
                            continue
                        else:
                            word_cl1 = re.sub(r'[^\w\s]','',word)
                            word_cl1 = word_cl1.lower()
                            if word_cl1 not in stop:
                                stemmed_word = ps.stem(word_cl1)
                                title.append(stemmed_word)


        if len(intro_plot) < 1:
            continue
        else:
            len_file = len(intro_plot) # the total number of words
            word = Vocabulary[int(term_id)]
            count = intro_plot.count(word) # the number of times that word is repeated in the document
            tf_in = count/len_file # the frequency of the word in the document
            idf = np.log(len_dict/len(val_word)) # the IDF 

            tf_title = 0
            if len(title) > 0:
                tf_title = title.count(word)/len(title)
            tf_imp = important1.count(word)/len(important1)
            if tf_title > 0:
                tf = tf_in + tf_imp + (tf_title)**2

                if term_id in New_Dict.keys():  # add the word to the new dictioary if the word is not already inside and add the new value if the word is already inside
                    New_Dict[term_id].append((doc, tf*idf))
                else:
                    New_Dict[term_id] = [(doc, tf*idf)]
            else:
                if tf_imp > 0:
                    tf = tf_in + tf_imp

                    if term_id in New_Dict.keys():  # add the word to the new dictioary if the word is not already inside and add the new value if the word is already inside
                        New_Dict[term_id].append((doc, tf*idf))
                    else:
                        New_Dict[term_id] = [(doc, tf*idf)]
                else:
                    tf = tf_in 

                    if term_id in New_Dict.keys():  # add the word to the new dictioary if the word is not already inside and add the new value if the word is already inside
                        New_Dict[term_id].append((doc, tf*idf))
                    else:
                        New_Dict[term_id] = [(doc, tf*idf)]

result_list = []
for i in range(len(result)):
    small_dict = {}
    for word in New_Dict.keys():
        for files in New_Dict[word]:
            if files[0] == result[i]:
                small_dict[word] = files[1]
    result_list.append(small_dict)

cos_result = {}
for i in range(len(result)):
    cosine = get_cosine(tf_idf_query, result_list[i])
    cos_result[result[i]] = cosine*100
    
cos_result = sorted(cos_result.items(), key=operator.itemgetter(1), reverse=True)

