# index_utils.py

def search_engine(query):
	query = stem_word(query)
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
	    if lst.count(i) >= len(query):
	         result.append(i)
	result = list(set(result))


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
	return df.iloc[:10]
	

#print(search_engine(query))

f =  open('/Users/yves/Desktop/Ex2_DICT_tfidf.json', 'r')
New_Dict = json.load(f)

def tf_idf_query_function(query):
    tf_idf = {}
    len_query = len(query)
    len_dict = len(os.listdir(path))
    DF = {}
    for word in query:# its a count funtion
        if word not in DF.keys():
            DF[word] = 1 
        else:
            DF[word]+=1
    
    for word in query:
        
        # TF = (Frequency of the word in the sentence) / (Total number of words in the sentence)
        count = query.count(word)
        freq = count/len_query
        tf = freq
        
        val_word = DF[word]
        idf = idf = np.log(len_dict/val_word)
        if word in Vocabulary:
            term_id = Vocabulary.index(word)
            if word in tf_idf.keys():
                tf_idf[str(term_id)]+= tf*idf
            else:
                tf_idf[str(term_id)] = tf*idf
    return tf_idf

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return round(float(numerator) / denominator, 4)

def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def search_engine2(query):
	query = stem_word(query)

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
	    if lst.count(i) >= len(query):
	         result.append(i)
	result = list(set(result))


	tf_idf_query = tf_idf_query_function(query) 
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

	to_df = []
	for movie in cos_result:
	    element_in_movie = {}
	    with open(path+movie[0]) as fd:
	        rd = csv.reader(fd, delimiter="\t", quotechar='"')
	        for row in rd:
	            if row[0] == 'Name':
	                element_in_movie['Name'] = row[1]
	            elif row[0] == 'Intro':
	                element_in_movie['Intro'] = row[1]
	            elif row[0] == 'Url':
	                element_in_movie['Url'] = row[1]
	        element_in_movie['Similarity'] = str(movie[1])+' %'
	    to_df.append(element_in_movie)
	df = pd.DataFrame(to_df)
	df = df.reindex(('Name', 'Intro', 'Url', 'Similarity'), axis=1)
	return df.iloc[:10]

#print(search_engine2(query))

f =  open('/Users/yves/Desktop/partial_DICT_tfidf.json', 'r')
New_Dict2 = json.load(f)

def search_engine3(query):
	query = stem_word(query)

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
	    if lst.count(i) >= len(query):
	         result.append(i)
	result = list(set(result))


	tf_idf_query = tf_idf_query_function(query) 
	result_list = []
	for i in range(len(result)):
	    small_dict = {}
	    for word in New_Dict2.keys():
	        for files in New_Dict2[word]:
	            if files[0] == result[i]:
	                small_dict[word] = files[1]
	    result_list.append(small_dict)

	cos_result = {}
	for i in range(len(result)):
	    cosine = get_cosine(tf_idf_query, result_list[i])
	    cos_result[result[i]] = cosine*100
	    
	cos_result = sorted(cos_result.items(), key=operator.itemgetter(1), reverse=True)

	to_df = []
	for movie in cos_result:
	    element_in_movie = {}
	    with open(path+movie[0]) as fd:
	        rd = csv.reader(fd, delimiter="\t", quotechar='"')
	        for row in rd:
	            if row[0] == 'Name':
	                element_in_movie['Name'] = row[1]
	            elif row[0] == 'Intro':
	                element_in_movie['Intro'] = row[1]
	            elif row[0] == 'Url':
	                element_in_movie['Url'] = row[1]
	        element_in_movie['Similarity'] = str(movie[1])+' %'
	    to_df.append(element_in_movie)
	df = pd.DataFrame(to_df)
	df = df.reindex(('Name', 'Intro', 'Url', 'Similarity'), axis=1)
	return df.iloc[:10]
    return Counter(words)

