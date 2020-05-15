import nltk
import string
import re
from  nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from nltk.stem.wordnet import WordNetLemmatizer
import matplotlib.pyplot as plt

from slang_translator import replace_slang

import pandas as pd

lem = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))
#print(len(stop_words))


def lemmatization(array_word):
    post_tag = nltk.pos_tag(array_word)

    final_array_words = []
    for word, tag in post_tag:
        wntag = tag[0].lower()
        wntag = wntag if wntag in ['a', 'r', 'n', 'v'] else None
        if not wntag:
            final_array_words.append(word)
        else:
            final_array_words.append(lem.lemmatize(word,wntag))
    return final_array_words


def data_pre_processing_text(text):
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    # replace slang, we have to extend this list
    # before eleminate number, text can containt some slang with number,
    #that's why replacing slang words firstly
    rs = text.split(' ')
    for i in range(len(rs)):
        if rs[1] != ' ':
            rs[i] = replace_slang(rs[i])
    text = ' '.join(rs)
    text = re.sub(r'\d+', '', text)

    tokenized_text = sent_tokenize(text)

    tokenized_word_by_sent = []
    for phrase in tokenized_text:
        tokenized_word = word_tokenize(phrase)
        tokenized_word_by_sent.append(tokenized_word)

    list_punctuation = ['.', '?', ',', '!', '"', ':', ';', "'", '-', '/', '...', '(', ')']
    punctuation = '!”#$%&’()*+,-./:;<=>?@[\]^_`{|}~'

    filtered_sent = []
    for sent in tokenized_word_by_sent:
        for word in sent:
            if word not in stop_words: # and word not in list_punctuation:
                filtered_sent.append(word.lower())

    new_filtered_sent = lemmatization(filtered_sent)

    if 'amp' in new_filtered_sent:
        new_filtered_sent.remove('amp')

    if len(new_filtered_sent) > 0:
        return ' '.join(new_filtered_sent)
    else:
        return None

def new_labeled_dataset(string_dataset):

    data = pd.read_csv(string_dataset, sep='\t', usecols=['sentiment', 'review'])
    data_1 = data.head(1000)
    # data.to_csv('train_test.csv')
    data_new = {
        'sentiment': [],
        'review': []
    }
    print('start data pre-processing...')
    counter = 0
    for i, element in data.iterrows():
        data_new['sentiment'].append(element['sentiment'] )
        data_new['review'].append(data_pre_processing_text(element['review']))

        counter += 1
        print(counter)

    df = pd.DataFrame(data_new)
    df.to_csv('train_dataset.csv')

    print(data_new)

string_dataset =  'labeledTrainData.tsv' #'train.tsv'
#new_labeled_dataset(string_dataset)



def show_graph():
    data = pd.read_csv(string_dataset, sep='\t', usecols=['sentiment', 'review'])
    Sentiment_count = data.groupby('sentiment').count()
    print(Sentiment_count)
    plt.bar(Sentiment_count.index.values, Sentiment_count['review'])
    plt.xlabel('Review Sentiments')
    plt.ylabel('Number of Review')
    plt.show()


tweet_one = """Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard! That's great men"""
A = """ nothing 1234what the fuck as a woman  345 you shouldn't complain about cleaning up your house. &amp; as a man you should always take the trash out... sharing WTF wth"""
B = """ boy dats cold...tyga dwn bad for cuffin dat hoe in the 1st place!!"""
C = """You ever fuck a bitch and she start to cry? You be confused as shit """
D = """@viva_based she look like a tranny"""
E = """The shit you hear about me might be true or it might be faker than the bitch who told it to ya &#57361;"""
F = """The shit just blows me..claim you so faithful and down for somebody but still fucking with hoes! &#128514;&#128514;&#128514;"""
G = """I can not just sit up and HATE on another bitch .. I got too much shit going on!"""
H = """cause I'm tired of you big bitches coming for us skinny girls!!&#8221;"""
G = """you might not get ya bitch back &amp; thats that"""
I = """hobbies include: fighting Mariam"""
input_str = """This &is [an] example? {of} string. with.? punctuation!!!!"""
J = """ null"""

#print(data_pre_processing_text(A))

liste_tweets = [tweet_one,A,B,C,D,E,F,G,H,G,I,input_str,J]
#for tweet in liste_tweets:
 #   print( data_pre_processing_text(tweet) )

#print(list(data['Phrase']))
#print(list(data['Sentiment']))
#print(data.keys())


from nltk.corpus import brown

#nltk.download()
#print(brown.words)

#translator = str.maketrans('', '', string.punctuation)
#print(data_pre_processing( input_str.translate(translator)))
