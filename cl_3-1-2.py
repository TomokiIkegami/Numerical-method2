# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:48:40 2020

@author: Tomoki Ikegami
"""

i=1
j=2
while i<5:
    while j<4:
        if i>1:
            break
        print ('i=',i,',','j=',j)
        j+=1
    j=0
    i+=1
    
    