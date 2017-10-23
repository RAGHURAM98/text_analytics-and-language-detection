import matplotlib.pyplot as plt
import numpy as np
import re
try:
    from nltk import wordpunct_tokenize
    from nltk.corpus import stopwords
except ImportError:
    print '[!] You need to install nltk (http://nltk.org/index.html)'
def get_data():
    file = open("sample.txt","r")
    tokens=file.read().lower()
    tokens = re.sub('[^a-z]', ' ', tokens)
    tokens = wordpunct_tokenize(tokens)
    return [word for word in tokens]
def _calculate_languages_ratios(words):
    languages_ratios = {}
    # Compute per language included in nltk number of unique stopwords appearing in analyzed data
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)
        languages_ratios[language] = len(common_elements) # language "score"
    return languages_ratios
def detect_language(data):
    ratios = _calculate_languages_ratios(data)
    most_rated_language = max(ratios, key=ratios.get)
    return most_rated_language
def get_stopwords(data, language):
    return [word for word in data if word in set(stopwords.words(language))]

def build_histogram(data):
    d={}
    #counting the no of word occurence
    for w in data:
        if w in d:
            d[w]+=1
        else:
            d[w]=1
    lst = [(d[w],w) for w in d]
    lst.sort()
    lst.reverse()
    data = np.array(lst)
    c=len(data)
    x,y=data.T
    count=range(c)
    plt.plot(x)
    plt.xticks(count,y,rotation=90)
    plt.xlabel('stopwords in the snippet')
    plt.ylabel('frequency')    
if __name__=='__main__':
    test_data=get_data()
    language = detect_language(test_data)
    print ("detected language : "+ str(language))
    stopwordsdata=get_stopwords(test_data, language)
    build_histogram(stopwordsdata)
