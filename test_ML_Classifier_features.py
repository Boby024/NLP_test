import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split

from sklearn.metrics import classification_report, accuracy_score

data = pd.read_csv('train_dataset.csv', sep=',')
X = data['review']
y = data['sentiment']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

def accuracy_test_NB():
    nb = Pipeline([('vect', CountVectorizer()),
                   ('tfidf', TfidfTransformer()),
                   ('clf', MultinomialNB()),
                   ])

    nb.fit(X_train, y_train)

    y_pred = nb.predict(X_test)
    print('MultinomialNB accuracy %s' % accuracy_score(y_pred, y_test))
    search_words = ['mediocre','uninteresting']
    #print(classification_report(y_test, y_pred, target_names = search_words )) #,target_names = my_tags))

def accuracy_test_SGD():
    nb = Pipeline([('vect', CountVectorizer()),
                   ('tfidf', TfidfTransformer()),
                   ('clf', SGDClassifier()),
                   ])

    nb.fit(X_train, y_train)

    y_pred = nb.predict(X_test)
    print('SGDClassifier accuracy %s' % accuracy_score(y_pred, y_test))
    search_words = ['mediocre','uninteresting']
    #print(classification_report(y_test, y_pred, target_names = search_words )) #,target_names = my_tags))

accuracy_test_NB()
accuracy_test_SGD()
