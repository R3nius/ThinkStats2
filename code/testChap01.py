""""
- caseid: ID of respondent
- prglngth: duration of the pregnancy in weeks
- outcome: outcome of the pregnancy (1: live birth)
- pregordr: respondent's first/second/etc. pregnancy
- birthord: serial number for live births (respondent's first child is 1)
- birthwgt_lb and birthwgt_oz contain the pounds and ounce
- agepreg: mother age at end of pregnancy
- finalwgt: weight associated with the respondent
"""

import thinkstats2
import numpy as np
import pandas as pd

def ReadFemPreg(dct_file='2002FemPreg.dct', dat_file='2002FemPreg.dat.gz'):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file,compression='gzip', usecols=['caseid', 'birthwgt_lb', 'birthwgt_oz'])
    #print(df.loc[df.birthwgt_lb, 1])
    #for i in df:
        #if df.loc[i, df.birthwgt_lb] == 97.00:
            #print(df.loc[i, df.birthwgt_lb])
        
    #CleanFemPreg(df)
    FindValue(df)
    #na_vals = [97, 98, 99]
    #df = df.loc[df.birthwgt_lb == na_vals, 'birthwgt_lb']
    return df
""""
def CleanFemPreg(df):
    df.agepreg /= 100.0

    na_vals = [97, 98, 99]
    df['birthwgt_lb'] = df.birthwgt_lb.replace(na_vals, np.nan)
    df['birthwgt_oz'] = df.birthwgt_oz.replace(na_vals, np.nan)

    df['totalwgt_lb'] = df['birthwgt_lb'] + df['birthwgt_oz'] / 16.0
"""

def FindValue(df):
    for i in df.birthwgt_lb:
        if df['birthwgt_lb'] == 97:
            print(df['birthwgt_lb'])
        i += 1

print (ReadFemPreg()['birthwgt_lb'][1])
