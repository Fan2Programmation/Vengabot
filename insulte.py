import pandas as pd


def getInsulte():
    df = pd.read_csv('insultes.txt', names=['noms'])
    insulte = df.sample()
    insulte = insulte['noms'].iloc[0]
    return insulte
