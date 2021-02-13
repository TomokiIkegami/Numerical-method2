# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:12:23 2021

@author: Tomoki Ikegami
"""

#積分したいf(x)
def f(x):
    return x**(2)+10

#シンプソン則を用いて上のf(x)の積分値を求める関数
    
def simp_inte(A,B,N): #A,Bはぞれぞれ積分範囲の上端と下端,Nは分割数
    
    h=(B-A)/N  #分割幅hを計算
    x=[] #分割幅hに基づいたx座標を入れるリスト
    S=0 #積分値Sの初期化
    
    for i in range(N+1) : #積分に使用するx座標を生成するループ文
        x.append(A+h*(i))
        
    for i in range(N+1) : #積分値を計算するループ文
        if i==0 or i==N : #両端部分の添え字の番号i
            S+=(h/3.0)*f(x[i])
        elif i%2==1 : #iが奇数だったとき
            S+=(h/3.0)*4.0*f(x[i])
        elif i%2==0 : #iが偶数だったとき
            S+=(h/3.0)*2.0*f(x[i])
    return S

A=float(input()) #積分範囲の上端
B=float(input()) #積分範囲の下端
N=int(input()) #分割数
ans=simp_inte(A,B,N) #積分値を計算

print( 'S={:.2f}'.format(ans)) #積分結果を表示