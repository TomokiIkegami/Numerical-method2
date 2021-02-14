# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 18:18:22 2020

@author: Tomoki Ikegami
"""

'''
work=15

def func():
    func_1=1
    work=21
    print(func_1)
    print(work)


func()
print(work)

'''

# def func():
#     func_1=1
#     global work
#     work=10
#     print(func_1)
#     print(work)

# work=2
# func()
# print(work)


#以後先生のプログラムを参考にしています。

def func(A):
    B=A*100
    C=int(B)
    D=B-C
    if D>=0.5:
        E=float(C/100+1/100)
    else:
        E=float(C/100)
    return E




A=float(input())

Ans=func(A)

#print(A)
print(Ans)