# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:31:47 2024

@author: PC
"""

a = input("Nhập một chữ cái: ")
if a.islower():
    a1 = a.upper()
    print(f"Chữ cái sau khi chuyển đổi: {a1}")
elif a.isupper():
    a2 = a.lower()
    print(f"Chữ cái sau khi chuyển đổi: {a2}")
else:
    print("Bạn không nhập một chữ cái hợp lệ")