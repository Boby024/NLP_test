#detect hate keyword
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

text = """That was so bad guys"""
text_2 = """Donald Trump’s administration: “Government by the worst men."""

stat =  {'negative': 0.0, 'neutral': 0.0, 'positive': 0.0}
result = sid.polarity_scores(text_2)
stat['positive'] = result['pos'] * 100
stat['neutral'] = result['neu'] * 100
stat['negative'] = result['neg'] * 100
print(text_2 + '\n','  ', stat)
