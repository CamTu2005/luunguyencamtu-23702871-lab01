# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:35:42 2024

@author: PC
"""

N = int(input("Nhap so nguyen duong N co 2 chu so = "))
if 10 <= N <= 99:
   a = N // 10 
   b =  N % 10
print("Ket qua", a + b)
    