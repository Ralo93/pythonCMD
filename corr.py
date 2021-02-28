#!/usr/bin/env python3

import pandas as pd
import numpy as np
import sys
import seaborn as sns
import matplotlib.pyplot as plt


# read in all our data
# nfl_data = pd.read_csv("../input/nflplaybyplay2009to2016/NFL Play by Play 2009-2017 (v4).csv")



def showMe(x):
    
    df = pd.read_csv(x, engine = 'python') #evtl .from_csv
    #sns.set()
    #plot = sns.heatmap(data.corr(, self, method='pearson', min_periods =1),annot=True, cmap='Blues', linewidths=1)
    #plt.show()  

    correlations = df.corr()
#correlations
#sns.heatmap(corr2)
    h = sns.heatmap(correlations, annot=True, linewidth=1, cmap='coolwarm')
    
    #fig, ax = plt.subplots(figsize=(6,6))
    #ax = sns.heatmap(data, linewidths=.5, ax=ax, cbar=False)
    #fig.savefig('heat.pgf')
    plt.show()
    
    #fig, ax = plt.subplots(figsiz
    plt.savefig('corr.png')
    #s = cwd + "/heat.pgf"
    

    
    
if __name__ == "__main__":

    x = sys.argv[1]
    print(showMe(x))
