# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:41:45 2022

@author: tolaifa
"""

import pandas as pd
import numpy as np

def max_number (n,x):
    negative= False
    if int(n)<0:
        negative = True
    nstr = str(abs(int(n)))
    xstr = str(x)
    possibility = []
    possibility.extend([xstr+nstr,nstr+xstr])
    for i in range(len(nstr)):
        if i<len(nstr)-1:
            possibility.append(nstr[:i+1]+xstr+nstr[i+1:])
    print(possibility)
        
    for i in range(len(possibility)):
        possibility[i] = int(possibility[i])
    
    if negative == False:
        print(max(possibility))
    else:
        print(min(possibility))
        
    
    

max_number("-956",2)