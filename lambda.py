# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 21:01:55 2021

@author: Tomoki Ikegami
"""
L=[4,9,100]

A=list(map(lambda x:x**(1/2),L)) #Lの中身をlambdaのところに移している。そしてlistでリスト化,map関数は各要素に対して一定の処理
print(A)