#!/usr/bin/env python3

import pandas as pd
import numpy as np
import sys
# read in all our data
# nfl_data = pd.read_csv("../input/nflplaybyplay2009to2016/NFL Play by Play 2009-2017 (v4).csv")

# set seed for reproducibility
#numpy.random.seed(0) 


def showMe(x):
    #missing_values = ["n/a", "na", "-", "--", "N/a", "n/A"]
    data = pd.read_csv(x, engine = 'python')
    print("***DROP DIRTY***")

    rows_with_na_dropped = data.dropna(axis=0)
    print("Rows in original dataset: %d " % data.shape[0])
    print("Remaining Rows with na's dropped: %d \n" % rows_with_na_dropped.shape[0])
                                    

    # remove all columns with at least one missing value
    columns_with_na_dropped = data.dropna(axis=1)
    columns_with_na_dropped.head()
    
    # just how much data did we lose?
    print("Columns in original dataset: %d " % data.shape[1])
    print("Remaining Columns with na's dropped: %d \n With remaining: " % columns_with_na_dropped.shape[1])    

    print(columns_with_na_dropped.columns)
    
    
if __name__ == "__main__":

    x = sys.argv[1]
    print(showMe(x))
