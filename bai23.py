# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:18:31 2024

@author: PC
"""
import math
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
delta=b**2 - 4*a*c
if delta ==0:
    x= -b/(2*a)
    print("Phương trình có nghiệm kép x = ",x)
elif delta<0:
    print("Phương trình vô nghiệm")
else:
    x1= (-b + math.sqrt(delta)) / (2*a)
    x2= (-b - math.sqrt(delta)) / (2*a)
    print(f"Phương trình có 2 nghiệm là x1 = {x1}; x2 = {x2}")