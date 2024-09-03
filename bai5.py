# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:46:45 2024

@author: PC
"""

time = input("Nhập thời gian theo định dạng hh:mm:ss: ")

hh, mm, ss = map(int, time.split(':'))

tongsogiay = hh * 3600 + mm * 60 + ss

print(f"Tổng số giây là: {tongsogiay}")