import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer

import joblib

data = pd.read_csv('train_dataset.csv', sep=',')
#data['label'] = data['sentiment'].map({'Negativ': 0, 'Positiv': 1})
X = data['review']
y = data['sentiment']

tf = TfidfVectorizer()


from Text_Processing import data_pre_processing_text
def sentiment_analyse_with_TFIDF():
    text = input("Enter your text: ")
    nb = MultinomialNB().fit(tf.fit_transform(X), y)

    nb_review_tfidf = open('NB_tfidf.pkl', 'rb')
    nb = joblib.load(nb_review_tfidf)

    predicted = nb.predict(tf.transform([ data_pre_processing_text(text) ]))
    return predicted[0]

#print(sentiment_analyse_with_TFIDF())

def accuracy_score_TfidfVectorizer():
    text_tf = tf.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        text_tf, y, test_size=0.3, random_state = 42) # random_state=1

    nb = MultinomialNB().fit(X_train, y_train)

    predicted = nb.predict(X_test)
    print("TfidfVectorizer accuracy -> MultinomialNB Accuracy:",metrics.accuracy_score(y_test, predicted))
    print()
    print(metrics.classification_report(y_test, predicted))
    joblib.dump(nb,'NB_tfidf.pkl')
#accuracy_score_TfidfVectorizer()

#nb = MultinomialNB()
#nb_review_tfidf = open('NB_tfidf.pkl', 'rb')
#g = joblib.load(nb_review_tfidf)
#print(g)
