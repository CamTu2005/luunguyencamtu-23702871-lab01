# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:51:10 2024

@author: PC
"""

ngay = int(input("Nhập ngày sinh: "))
thang = int(input("Nhập tháng sinh: "))
nam = int(input("Nhập năm sinh: "))


dinh_dang_a = f"{ngay}/{thang}/{nam}"
print(f"a) {dinh_dang_a}")


dinh_dang_b = f"{ngay}/{thang}/{str(nam)[-2:]}"
print(f"b) {dinh_dang_b}")


dinh_dang_c = f"{nam}/{thang}/{ngay}"
print(f"c) {dinh_dang_c}")