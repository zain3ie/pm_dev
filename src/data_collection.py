import pandas as pd


def data_collection():
    df1 = pd.read_excel('./data/ar-2010-2014-xlsb.xlsb', engine='pyxlsb')
    df2 = pd.read_excel('./data/ar-2015-2016-xlsb.xlsb', engine='pyxlsb')
    df = pd.concat([df1.copy(), df2.copy()])

    return df
