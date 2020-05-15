import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from nltk.tokenize import RegexpTokenizer

#tokenizer to remove unwanted elements from out data like symbols and numbers
token = RegexpTokenizer(r'[a-zA-Z0-9]+')

data = pd.read_csv('train_dataset.csv', sep=',')

vectorizer = CountVectorizer(ngram_range = (1,1)) #CountVectorizer(lowercase=True,stop_words='english',ngram_range = (1,1),tokenizer = token.tokenize)

from Text_Processing import data_pre_processing_text
def sentiment_analyse_with_CountVectorizer():
    text = input("Enter your text: ")
    nb = MultinomialNB().fit(vectorizer.fit_transform(data['review']), data['sentiment'])
    predicted = nb.predict(vectorizer.transform([data_pre_processing_text(text)]))
    return predicted[0]

def accuracy_score_CountVectorizer():
    text_counts= vectorizer.fit_transform(data['review'])
    X_train, X_test, y_train, y_test = train_test_split(
        text_counts, data['sentiment'], test_size=0.3, random_state = 42) # random_state=1
    nb = MultinomialNB().fit(X_train, y_train)
    predicted = nb.predict(X_test)
    print("CountVectorizer -> MultinomialNB Accuracy:",metrics.accuracy_score(y_test, predicted))

accuracy_score_CountVectorizer()

"""
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    text_counts, data['Sentiment'], test_size=0.3) # random_state=1

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Generation Using Multinomial Naive Bayes
clf = MultinomialNB().fit(X_train, y_train)
#clf = SGDClassifier().fit(X_train, y_train)

#clf = MultinomialNB().fit(data['Phrase'], data['Sentiment'])
#predicted=  clf.predict(X_test)

text = "it was bad, non sense" #"entertaining!"
predicted_2 = clf.predict(cv.transform([ text ]))
#print("MultinomialNB Accuracy:",metrics.accuracy_score(y_test, predicted))
print("test with Bag of Words: ", predicted_2)
print("max on this column is: ",data['Sentiment'].max())
print(data.loc[ data['Sentiment'] == 4 ])

"""
