# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:22:13 2024

@author: PC
"""

a =int(input('nhap so nguyen a: '))
b =int(input('nhap so nguyen b: '))
c =int(input('nhap so nguyen c: '))
d =int(input('nhap so nguyen d: '))
if a<b and a<c and a<d:
    print('Số có giá trị nhỏ nhất là a: ', a)
elif b<a and b<c and b<d:
    print('Số có giá trị nhỏ nhất là b: ', b)
elif c<a and c<b and c<d:
    print('Số có giá trị nhỏ nhất là c: ', c)
else:
    print('Số có giá trị nhỏ nhất là d: ', d)
    
    
    