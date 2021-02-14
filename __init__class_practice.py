# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 09:25:43 2020

@author: Tomoki Ikegami
"""

class RC: #クラスを宣言

    # rc_name=None #インスタンス変数を定義
    # release_date=None #インスタンス変数を定義
    # dimention=[] #インスタンス変数を定義
        
    def __init__(self,name,dat,dim):
        self.rc_name=name
        self.release_date=dat
        self.dimention=dim
    
        
    def indicate(self): #この関数のことをメソッドと呼ぶ
        
        template_RCinfo="RC_name:{0}、Release_date:{1}" #定型文は関数の中に定義する必要あり
        template_RCdimention="Length={0},Width={1},Height={2}" #定型文は関数の中に定義する必要あり

        '''
        for i in self.dimention:
            self.dimention.append(i)
        '''
        
        print(template_RCinfo.format(self.rc_name,self.release_date))
        print(template_RCdimention.format(self.dimention[0],self.dimention[1],self.dimention[2]))
        
#1つめのインスタンス ※インスタンスはクラスからの戻り値のようなもの。出来上がったもの(その戻り値)は構造体に似ている。

RC_1=RC('OPTIMA','2016',[395,240,120])
RC_1.indicate()        

#2つめのインスタンス

RC_2=RC('GS02 BOM','2018',[515,240,220])
RC_2.indicate()        

