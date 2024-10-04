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
import thinkplot
import readDataFile
import numpy as np
import pandas as pd
import sys


def ReadFemPreg(dct_file='2002FemPreg.dct', dat_file='2002FemPreg.dat.gz'):
    dct = readDataFile.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file,compression='gzip', usecols=['caseid', 'agepreg', 
    'pregordr', 'prglngth', 'outcome', 'birthwgt_lb', 'birthwgt_oz'])
    
    #print(FindValue(df))
    #CleanFemPreg(df)
    #print(firstBabyArrival(df))
    return(df)

def CleanFemPreg(df):
    df.agepreg /= 100.0

    na_vals = [97, 98, 99]
    df['birthwgt_lb'] = df.birthwgt_lb.replace(na_vals, np.nan)
    df['birthwgt_oz'] = df.birthwgt_oz.replace(na_vals, np.nan)

    df['totalwgt_lb'] = df['birthwgt_lb'] + df['birthwgt_oz'] / 16.0


def FindValue(df):
    some_values = [97, 98, 99]
    df = df.loc[df['birthwgt_lb'].isin(some_values) | df['birthwgt_oz'].isin(some_values)]
    return df

## check percentage of mother who give birth to first baby alive arrive late and 
# is more than 40 years old
def firstBabyArrival(df):
    row_count = len(df)

    df['mother_age'] = df.agepreg/48
    df = df.loc[(df['mother_age'] > 40) & (df['pregordr'] == 1) & 
                (df['outcome'] == 1) & (df['prglngth'] > 39)]
    
    compare_row = len(df)
    result = compare_row/row_count *100

    print(f"Percentage of mother who is more than 40 years old and give birth to first baby alive, arrive late: {round(result,2)} %")
    return df


def main(script):
    ReadFemPreg()

if __name__ == '__main__':
    main(*sys.argv)