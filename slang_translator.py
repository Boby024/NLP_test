import string
import pandas as pd
import numpy as np

# repo for the first elemets here
# https://github.com/rishabhverma17/sms_slang_translator/blob/master/slang.txt

# website of many slang's list
# https://digiphile.info/2009/06/11/top-50-twitter-acronyms-abbreviations-and-initialisms/
#https://www.webopedia.com/quick_ref/textmessageabbreviations.asp
#https://www.webopedia.com/quick_ref/Twitter_Dictionary_Guide.asp
def recompile_list_slangs():
    df = pd.read_csv('slang_words.txt', sep="=", header=None, names=["abbreviation", "signification"])
    abbreviation = df['abbreviation'].values
    abbreviation = [item.lower() for item in abbreviation]
    signification = df['signification'].values

    data_dico_slangs = {
        'abbreviation': abbreviation,
        'signification': signification
    }
    df = pd.DataFrame(data_dico_slangs, columns= ['abbreviation','signification'])
    df.to_csv('slangs.csv')

recompile_list_slangs()
data = pd.read_csv('slangs.csv')
global abbreviation
global signification

def replace_slang(_str): # here I get the abbreviation
    if len(_str) < 2:
        return _str.lower()
    else:
        abbreviation = data['abbreviation'].values
        signification = data['signification'].values

        result = np.where(abbreviation == _str.lower())
        _result = result[0]
        if len(_result) > 0:
            translator = str.maketrans('', '', string.punctuation)
            text = signification[_result[0]].lower().translate(translator)
            return text
        else:
            return _str.lower()

txt = 'nfw'
#print(replace_slang(txt))
"""
df = pd.read_csv('slang_words.txt', sep="=", header=None, names=["abbreviation", "signification"])
    # df.to_csv('slang_final.csv')

    abbreviation = df['abbreviation'].values
    signification = df['signification'].values


    result = np.where(abbreviation == _str.upper())
    _result = result[0]
    if len(_result) > 0:
        return signification[_result[0]].lower()
    else:
        return _str.lower()
"""

#element = data.loc[data['abbreviation'] == 'wtf']
#print(element)
#print()
#print(data.isin(['wth']).any().any() )
#print()
#print(element['abbreviation'][0])
#print()
#print(element['signification'][0])
#print(element['Columns'])
