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

# Remove hashtag, link, @username, non alphabetic
def hashtag_username_url(text):
    text = re.sub('@[\w\-]+','<hashtag>', text)
    text = re.sub('#[\w\-]+', '<username>', text)
    parsed_text = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '<link>', text)
    #parsed_text = re.sub(r'\d+', '', text)
    return parsed_text

def data_pre_processing_text(text):
    # Only when the text is from Twitter
    #text = hashtag_username_url(text)

    # The performance of this code to remove punctuation
    # is better than using regex
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    tokenized_word = word_tokenize(text)
    filtered_words = []
    for i in range(len(tokenized_word)):
        __str_text = tokenized_word[i]
        __str_text = replace_slang(tokenized_word[i]) # could be a string with length 1, 2 ,3 4 # replace slang, we have to extend this list before eleminate number, text can containt some slang with number that's why replacing slang words firstly
        if len(__str_text) > 1:
            for word in word_tokenize(__str_text):
                if word not in stop_words: # remenber to don't remove 'not' word by this step
                    filtered_words.append(word.lower())
        else:
            if __str_text not in stop_words:  # and word not in list_punctuation:
                filtered_words.append(tokenized_word[i].lower())

    filtered_words = lemmatization(filtered_words)

    # Only for this Review dataset
    if 'amp' in filtered_words:
        filtered_words.remove('amp')

    if len(filtered_words) > 0:
        parsed_text =  ' '.join(filtered_words)
        return re.sub(r'\d+', '', parsed_text)
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
J = """ null wtH a3"""

liste_tweets = [tweet_one,A,B,C,D,E,F,G,H,G,I,input_str,J]
#for tweet in liste_tweets:
    #print( data_pre_processing_text(tweet) )

#print(list(data['Phrase']))
#print(list(data['Sentiment']))
#print(data.keys())


from nltk.corpus import brown

#nltk.download()
#print(brown.words)

#translator = str.maketrans('', '', string.punctuation)
#print(data_pre_processing( input_str.translate(translator)))
