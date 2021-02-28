#!/usr/bin/env python3

import pandas as pd
import numpy as np
import sys
# read in all our data
# nfl_data = pd.read_csv("../input/nflplaybyplay2009to2016/NFL Play by Play 2009-2017 (v4).csv")

# set seed for reproducibility
#numpy.random.seed(0) 


def showMe(x):

    #setting decimal to 2
    
    
    #defining missing values all kinds of na
    missing_values = ["n/a", "na", "-", "--", "N/a", "n/A"]
    data = pd.read_csv(x, na_values = missing_values, engine = 'python')

    columns = data.shape[1]
    #pd.set_option("display.precision", 2)
    #setting decimal to 2
    #pd.option_context('display.float_format', '{:0.2f}'.format):
    print(data.head())
    print(data.info())

    missingCount = data.isnull().sum()
    
    # how many total missing values do we have?
    total_cells = np.product(data.shape)
    total_missing = missingCount.sum()

    # percent of data that is missing
    percent_missing = (total_missing/total_cells) * 100
    print("Percent missing: " + str(percent_missing))

    print("Missing count:")
    print(missingCount[0:columns])

    #data.columns
    
if __name__ == "__main__":

    x = sys.argv[1]
    print(showMe(x))
