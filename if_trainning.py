#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:10:38 2021

@author: yuanke.tsai
"""

hight = input("請輸入身高（公尺）：")
hight = float(hight)
weight = input("請輸入體重（公斤）：")
weight = float(weight)
bmi = weight / (hight * hight)
print(bmi)
if bmi < 18.5:
    print('過輕')
elif bmi >= 18.8 and bmi < 24:
    print('正常')
elif bmi >= 24 and bmi < 27:
    print('過重')
elif bmi >= 27 and bmi < 30:
    print('輕度肥胖')
elif bmi >= 30 and bmi <35:
    print('中度肥胖')
else:
    print('重度肥胖')