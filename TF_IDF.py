import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv('train_dataset.csv', sep=',')

tf = TfidfVectorizer()


from Text_Processing import data_pre_processing_text
def sentiment_analyse_with_TFIDF():
    text = input("Enter your text: ")
    nb = MultinomialNB().fit(tf.fit_transform(data['review']), data['sentiment'])
    predicted = nb.predict(tf.transform([ data_pre_processing_text(text) ]))
    return predicted[0]

#print(sentiment_analyse_with_TFIDF())

def accuracy_score_TfidfVectorizer():
    text_tf = tf.fit_transform(data['review'])

    X_train, X_test, y_train, y_test = train_test_split(
        text_tf, data['sentiment'], test_size=0.3, random_state = 42) # random_state=1

    nb = MultinomialNB().fit(X_train, y_train)

    predicted = nb.predict(X_test)
    print("TfidfVectorizer> MultinomialNB Accuracy:",metrics.accuracy_score(y_test, predicted))

#accuracy_score_TfidfVectorizer()
