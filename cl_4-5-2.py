# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 16:50:09 2021

@author: Tomoki Ikegami
"""

def func(*NUM):
    print(NUM)

    R=0
    for i in NUM:
        R+=i
        
    return R/len(NUM)

NU1=func(2,5)
NU2=func(1,4,6,1)

print(NU1)
print(NU2)
