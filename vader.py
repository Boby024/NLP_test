from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
#print(sia.polarity_scores('shit'))

from Text_Processing import data_pre_processing_text
def sentiment_analyse_with_SentimentIntensityAnalyzer():
    text = input("Enter your text: ")
    result = sia.polarity_scores(data_pre_processing_text(text))
    print(result)
    pos = result['pos']
    neg = result['neg']
    neu = result['neu']
    if pos - neg > 0:
        return {'sentiment': 'positiv', 'score': pos}
    elif neg - pos > 0:
        return {'sentiment': 'negativ', 'score': neg}
    elif pos - neg == 0:
        return {'sentiment': 'neutral', 'score': neu}

text = ' '.join(['drasko', 'steve', 'need', 'hate', 'fuck', 'get', 'mkr'])
print(sia.polarity_scores(text))
