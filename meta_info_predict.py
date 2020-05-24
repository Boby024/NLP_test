import pandas as pd

file = 'C:\\Users\\William\\\Downloads\\twitter_data_processed_506.xlsx'
df = pd.read_excel(file) #(open(file, 'rb'))
#print(df.head(5)['lang'] )

def get_all():
    tweetid = df['tweetid'].values
    signification = df['signification'].values
    return 0
