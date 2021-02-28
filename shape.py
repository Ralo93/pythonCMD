#!/usr/bin/env python3

import pandas as pd
import numpy as np
import sys
# read in all our data
# nfl_data = pd.read_csv("../input/nflplaybyplay2009to2016/NFL Play by Play 2009-2017 (v4).csv")
import missingno as msno

# set seed for reproducibility
#numpy.random.seed(0) 


def showMe(x):
    
    data = pd.read_csv(x, engine = 'python')
    print("SHAPE:")
    print(data.shape)
    print("COLUMNS:")
    print(data.columns)
    #print(data.columns)
    print("DESCRIPTION object vars:")
    print(data.describe(include=np.object)) #maybe ohne object?
#np.object
    print("DESCRIPTION no-object vars:")
    print(data.describe()) #once without objects
    
if __name__ == "__main__":

    x = sys.argv[1]
    print(showMe(x))
