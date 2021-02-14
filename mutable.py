# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 20:55:22 2021

@author: Tomoki Ikegami
"""

def func(A):
    A[0]=0
    print('in_func=',A)


A=[1023]
print('before_func',A)
func(A)
print('after_func',A)
