#!/usr/bin/env python3

import pandas as pd
import numpy as np
import sys
# read in all our data
# nfl_data = pd.read_csv("../input/nflplaybyplay2009to2016/NFL Play by Play 2009-2017 (v4).csv")

# set seed for reproducibility
#numpy.random.seed(0) 
import os


def showMe(csv, column):

    cwd = os.getcwd()
    missing_values = ["n/a", "na", "-", "--", "N/a", "n/A"]
    data = pd.read_csv(csv, na_values = missing_values, engine = 'python')

    data = data.drop(columns = column)
    
    s = cwd + "/dropped.csv"
    data.to_csv(s)
    
if __name__ == "__main__":

    csv = sys.argv[1]
    column = sys.argv[2]
    print(showMe(csv, column))
