# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 15:23:25 2021

@author: Tomoki Ikegami
"""

def func(a):
    
  if a<0:
     b=-a*100
  else :
     b=a*100 #b>0のときの処理も忘れずに。
  
  c=int(b)
  d=b-c

  if d>=0.5:
    ans=c/100+(1/100)
  else:
    ans=c/100

  if a<0:
    return -ans

  else:
    return ans



a=float(input())

print(func(a))