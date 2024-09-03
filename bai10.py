# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:48:44 2024

@author: PC
"""

biensoxe=int(input("nhập số xe gồm 4 chữ số : "))
a = biensoxe %10 #lấy số cuối cùng của biển số xe
x = biensoxe//10  #lấy 3 số đầu tiên của biển số xe
b  =x %10  #láy số cuối cùng của x
y= x//10  #lấy 2 số đầu tiên của biển số xe
c=y%10   #láy số cuối cùng của y
d=y//10   #lấy số đầu tiên của biển số xe

tongsonut= a + b + c + d
sonut = int(tongsonut % 10)
print("số xe của bạn được ", sonut,"nút")