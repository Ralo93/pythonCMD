#!/usr/bin/env python3

import pandas as pd
import numpy as np
import sys
# read in all our data
# nfl_data = pd.read_csv("../input/nflplaybyplay2009to2016/NFL Play by Play 2009-2017 (v4).csv")

# set seed for reproducibility
#numpy.random.seed(0) 
import os


def showMe(x):
    #missing_values = ["n/a", "na", "-", "--", "N/a", "n/A"]
    df = pd.read_csv(x, engine = 'python')
    print("***DROP 90***")
    cwd = os.getcwd()

   # row_count = df.shape[0]
   # columns_to_drop = []

   # for column, count in df.apply(lambda column: (column == 0).sum()).iteritems():
       # if count / row_count >= 0.9:
      #      print(count/row_count)
     #       columns_to_drop.append(column)

    #df = df.drop(columns_to_drop, axis=1, inplace=True)
    df = df.drop(columns=df.columns[((df==0).mean()>0.9)],axis=1)

    s = cwd + "/droppedColumns.csv"
    df.to_csv(s)

    #print(df.shape[0])
    #columns_dropped90 = data.drop(columns=data.columns[((data==0).mean()>0.9)],axis=1)
    #print("Columns in original dataset: %d " % data.shape[1])
    #print("Columns with >90 dropped: %d \n" % columns_dropped90.shape[1])
                                    

    # remove all columns with at least one missing value
    #columns_with_na_dropped = data.dropna(axis=1)
    #columns_with_na_dropped.head()
    
    # just how much data did we lose?
    #print("Columns in original dataset: %d " % data.shape[1])
    #print("With remaining: " % columns_dropped90.columns)

    return df
   
if __name__ == "__main__":

    x = sys.argv[1]
    print(showMe(x))
