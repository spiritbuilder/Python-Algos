# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:41:45 2022

@author: tolaifa
"""

import pandas as pd
import numpy as np

def max_number (n,x):
    negative= False
    nstr = str(abs(int(n)))
    xstr = str(x)
    
    if int(n)<0:
        negative = True
        
    possibility = []
    possibility.extend([int(xstr+nstr),int(nstr+xstr)])
    
    for i in range(len(nstr)):
        if (i<len(nstr)-1) and (len(nstr)>1):
            possibility.append(int(nstr[:i+1]+xstr+nstr[i+1:]))
    
    print("absolutes of possibilities are", possibility)
        
    if negative == False:
        print("Maximum is: ",max(possibility))
    else:
        print("Maximum is: ", min(possibility))
        
    
    

max_number("0",2)
print("==================")
max_number("23", 5)
print("==================")
max_number("-458", 3)