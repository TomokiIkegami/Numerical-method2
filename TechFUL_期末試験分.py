# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 15:46:19 2021

@author: Tomoki Ikegami
"""

#「[Python]if文①」
'''
a=int(input())

if a==0:
  print('ゼロ')

elif a%2==0:
  print('偶数')

elif a%2==1:
  print('奇数')

#インデントとelifの綴りに注意！

'''

#「[Python]if文②」

'''

A=[]
count=0

for i in range(10):
  A.append(int(input()))
  if A[i]<60:
    count+=1

print('{0}人'.format(count))
for i in range(9):
  print('{0},'.format(A[i]),end='')
#表示形式をそろえるのが難問

print(A[9]) #要素10個のリストの添え字の最大値は9


'''

#「[Python]if文③」

'''

A=[]
B=[0]*5 #リストの長さ重要

for i in range(5):
  A.append(float(input()))
  B[i]=A[i]

for i in range(len(B)):
  for j in range(len(B)-(i+1)): #(i+1)にするのが重要.
     if B[j+1]>B[j]:
       work=B[j+1]
       B[j+1]=B[j]
       B[j]=work

print(B[0]) 

for i in range(len(A)-1):
  print('{0},'.format(A[i]),end='')
print(A[len(A)-1]) #間違えてソート済みのものを出力しないように。



'''

#「[Python]関数①」

'''

N=10

def sum(A):
  s=0
  for i in range(len(A)): #range書き忘れないように
    s+=A[i]
  return s

A=[]

for i in range(N):
  A.append(int(input()))

print(sum(A))


for i in range(N-1):
  print('{0},'.format(A[i]),end='')  #end=がないと改行されてしまう
print(A[N-1])




'''


#「[Python]関数②」

'''
def judge_num(a):
  if a==0:
    return 1
  elif a%2==0:
    return 2
  elif a%2==1:
    return 3

a=int(input())
print(judge_num(a))

'''

#「[Python]関数③」

'''
def func(a,b):
  A=[] #空のリストは本当に大切
  A.append(a+b)
  A.append(a-b)
  A.append(a*b)
  A.append(a/b)
  return A

a=float(input())
b=float(input())

Ans=func(a,b)

print(a,'+',b,'=',Ans[0],sep='')
print(a,'-',b,'=',Ans[1],sep='')
print(a,'*',b,'=',Ans[2],sep='')
print(a,'/',b,'=',Ans[3],sep='')



'''

#「[Python]関数④」

'''
#負の値が入って来るときも考慮する。

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




'''


#「[Python]関数⑤」

'''
def func(a,r):
  a_abs=abs(a)
  b=10**(r)*a_abs
  c=int(b)
  d=b-c
  if d>=0.5:
    Ans=(c/10**(r)+1/10**(r))
  else:
    Ans=(c/10**(r))

  if a<0:
    return -Ans
  else:
    return Ans


r=int(input())
a=float(input())
print(func(a,r))




'''


#「[Python]関数⑥」

'''

def count_f(st):
  A=[0,0]
  for i in range(len(st)): #rangeをつけ忘れない
    if st[i]=='A':
      A[0]+=1
    elif st[i]=='i':
      A[1]+=1
    else:
      pass
  return A

st=input()
res=count_f(st)

print('文字数:',len(st),sep='')
print('A:',res[0],sep='')
print('i:',res[1],sep='')





'''

#「[Python]関数⑦」

'''

def det(a,b,c,d):
 return abs(a*d-b*c)

A=[[0,0],[0,0]] #2次元のリストの宣言が独特

for i in range(2):
  for j in range(2):
    A[i][j]=int(input())

print(det(A[0][0],A[0][1],A[1][0],A[1][1]))


'''

#「[Python]台形則」

'''

def f(x):

  return  x**(4)+2.0*x #returnをつけ忘れていた。

def daikei(A,B,N):
  
  h=(B-A)/N
  S=0

  for i in range(N): #Nの数が多かった
     S+=(h/2)*(f(A+h*i)+f(A+h*(i+1))) #(h/2)の後にアスタリスク＊を忘れていた。

  return S

a=float(input())
b=float(input())
N=int(input())
print('S={:.2f}'.format(daikei(a,b,N))) #S=を忘れていた。



'''


#「[Python]シンプソン則」[誤答例]

'''

def f(x):
  return x**(4)+2.0*x

def simpson(A,B,N):
  h=(B-A)/N
  S=0

  for i in range(N):
    S+=(h/3)*(f(A+h*i)+4*f(A+h*(i+1))+2*f(A+h*(i+2)))

  return S

a=float(input())
b=float(input())
N=int(input())

print('S={:.2f}'.format(simpson(a,b,N)))


'''

#「[Python]シンプソン則」[正答例]

'''

def f(x):
  return x**(4)+2.0*x

def simpson(A,B,N):
  h=(B-A)/N
  S=0

  for i in range(N+1): #台形則とNの値が違うのは、iがNまでいかなければいけないためである。
    if i==0 or i==N:
      S+=(h/3)*f(A+h*i)
    elif i%2==1:
      S+=(h/3)*4*f(A+h*i)
    elif i%2==0:
      S+=(h/3)*2*f(A+h*i)

  return S

a=float(input())
b=float(input())
N=int(input())

print('S={:.2f}'.format(simpson(a,b,N)))



'''
