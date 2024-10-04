import thinkstats2
import thinkplot
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def hist():
    hist_value = thinkstats2.Hist([1,2,2,3,4,5])
    print(f"Hist: {hist}")
    #print(f"Frequency of 4: {hist[4]}")
    print("List of hist values:")
    '''for val in sorted(hist.Values()):
        print(val,hist.Freq(val))
    
    print("-----")
    for val, freq in hist.Items():
        print(val,freq)
'''
    thinkplot.Hist(hist_value)
    print(thinkplot.Show(xlabel='value', ylabel='frequency'))
    plt.hist(hist_value)
    plt.show()

def drawHistogram():
    hist = thinkstats2.Hist([1,2,2,3,4,5])
    thinkplot.Hist(hist)
    print(thinkplot.Show(xlabel='value', ylabel='frequency'))

def main(script):
    #print("Test new file")
    print(hist())
    #drawHistogram()

if __name__ == '__main__':
    main(*sys.argv)