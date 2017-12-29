import pandas as pd
import numpy as np
pd.set_option('display.max_colwidth', 200)

def get_1st_item(s):
    str_corr = s[37:44]
    #  去掉下面不需要字符
    return str_corr.strip('u},\'\'').strip('\'},') 

def read_file(filepath):
    df = pd.read_csv(filepath,encoding='utf-8')
    df.drop(df.columns[[0,1,3]], inplace=True, axis=1) # inplace=True 表示在本df修改 不需要再赋值
    return df

def get_df_by_series(series):
    dataframe  =  pd.DataFrame(data=series, columns=['result'])
    return dataframe
    

    
    
    
    
    