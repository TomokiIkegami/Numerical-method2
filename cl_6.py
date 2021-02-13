# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 10:07:32 2020

@author: Tomoki Ikegami
"""

def print_mat(num,AA):
    j=0
    for j in range(num):
        print('{0} '.format(AA[j]),end='')
    print("\n")
    
def func(num,AA,BB):
    i=0
    j=0
    work=0
    for i in range(num):
        BB[i]=AA[i]
    
    for i in range(num-1):

        print("step{0}:".format(i+1))
        
        for j in range(num-(i+1)):
            if BB[j]>BB[j+1]:
                work=BB[j+1]
                BB[j+1]=BB[j]
                BB[j]=work
    
        print_mat(num, BB)
    
A=[2,170,50,1,10,3]
B=[0]*6

print('入力:')
print_mat(5+1, A)

func(7-1,A,B)


print('結果:')
print_mat(10-4,B)



