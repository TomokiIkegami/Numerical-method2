# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 19:40:57 2021

@author:Toma Takei
"""

# @author:Toma Takei
def myr(x):
     absx = abs(x)
     B=100*absx
     C=B+0.5
     ret=int(C)/100
     return ret if x > 0 else -ret
 
a=float(input())

print(myr(a))W