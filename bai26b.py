# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:52:34 2024

@author: PC
"""

N = int(input("Nhập số nguyên N: "))
# Chuyển số nguyên thành chuỗi và sắp xếp các chữ số theo thứ tự tăng dần
sapxep = ''.join(sorted(str(N)))
# Chuyển chuỗi đã sắp xếp thành số nguyên
ketqua = int(sapxep)
print(f"Số có các chữ số theo thứ tự tăng dần là: {ketqua}")