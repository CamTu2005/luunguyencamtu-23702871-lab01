# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:51:18 2024

@author: PC
"""

a=float(input('nhap so a: '))
b=float(input('nhap so b: '))

x=((((a+b)/(a**(1/3)+b**(1/3)))-(a*b)**(1/3)))
y=((a**(1/3))-(b)**(1/3))
z=(x/(y**2))
print('ket qua = ', z)