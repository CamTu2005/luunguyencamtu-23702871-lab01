# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:26:17 2024

@author: PC
"""

h=int(input('Nhập giờ: '))
m=int(input('Nhập phút: '))
s=int(input('Nhập giây: '))
if 0<=h<=24 and 0<=m<=60 and 0<=s<=60:
    print(f"Thời gian {h:02}:{m:02}:{s:02} là hợp lệ.")
else:
    print(f"Thời gian {h:02}:{m:02}:{s:02} không hợp lệ.")