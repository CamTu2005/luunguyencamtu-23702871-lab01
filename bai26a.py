# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:39:50 2024

@author: PC
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
if a > b:
    d = a
    a = b 
    b = d
if a > c:
    d = a
    a = c
    c = d
if b > c: 
    d = b
    b = c
    c = d
print(f"các số theo thứ tự tăng dần là: {a}, {b} , {c}")