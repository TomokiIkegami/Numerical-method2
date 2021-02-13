# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 21:23:22 2021

@author: Tomoki Ikegami
"""

class primitive_info:
    disp_temp="図形:{0} 体積:{1} 表面積:{2}"
    name=None

    def cone(self,r,h):
        self.name="円柱"
        V=3.14*r**2*h 
        S=3.14*(2*r)*h+2*(3.14)*r**2
        ans=self.disp_temp.format(self.name,V,S)
        
        return ans
    
    def cube(self,l):
        self.name="立方体"
        V=l**3 
        S=6*l**2
        ans=self.disp_temp.format(self.name,V,S)
        
        return ans   
    
r=2    
h=4
l=3

culc=primitive_info()

cone_info=culc.cone(r,h)
cube_info=culc.cube(l)

print(cone_info)
print(cube_info)
