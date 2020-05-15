from TF_IDF import sentiment_analyse_with_TFIDF
from BoW import sentiment_analyse_with_CountVectorizer
from vader import sentiment_analyse_with_SentimentIntensityAnalyzer
from Text_Processing import new_labeled_dataset

def start():
    # Here test our sentminent analysis programm
    print("DO you want to classify again the dataset... and this will take about 20 minutes for our 25.000 row ")
    query = str(input('with just yes or no: '))
    if query == 'no':
        print('We have 02 methods tf-idf and CountVectorizer')
        query_2 = int(input('with just 0 = tf-idf  and  1 = CountVectorizer and  2 = Vader_SentimentIntensityAnalyzer: '))
        if query_2 == 0:
            print("sentiment with: ", sentiment_analyse_with_TFIDF())
        elif query_2 == 1:
            print("sentiment with: ", sentiment_analyse_with_CountVectorizer())
        else:
            print("sentiment with: ", sentiment_analyse_with_SentimentIntensityAnalyzer())
    else:
        new_labeled_dataset()
        print("restart the programm")

start()

