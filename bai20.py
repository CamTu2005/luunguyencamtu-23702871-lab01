# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:13:57 2024

@author: PC
"""

a =int(input('nhap so nguyen a: '))
b =int(input('nhap so nguyen b: '))
c =int(input('nhap so nguyen c: '))
if a>b and a>c:
    print("số lớn nhất là a = ", a)
elif b>a and b>c:
    print("số lớn nhất là b = ", b)
else:
    print('số lớn nhất là c = ', c)
