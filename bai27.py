# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:28:12 2024

@author: PC
"""

loaihinh = input("Nhập hình (v: vuông ; n: hình chữ nhật ; t:tròn): ")
if loaihinh== 'v':
    canh = float(input('Nhập cạnh hình vuông: '))
    P1 = canh*4
    S1 = canh*canh
    print(f" Chu vi của hình vuông: P = {P1}\n Diện tích hình vuông: S= {S1}")
elif loaihinh == 'n':
    dai = float(input("Nhập chiều dài hcn: "))
    rong = float(input("Nhập chiều rộng hcn: "))
    P2 = 2*(dai + rong)
    S2 = dai*rong
    print(f" Chu vi hcn: P = {P2}\n Diện tích hcn: S = {S2}")
elif loaihinh == 't':
    r = float(input("Nhập bán kính hình tròn: "))
    P3 = 2*3.14*r
    S3 = 3.14 *r *r
    print(f"Chu vi hình tròn: P = {P3}\nDiện tích hình tròn: S ={S3} ")
else:
    print("Lựa chọn không hợp lệ. Vui lòng chọn v, n, hoặc t.")