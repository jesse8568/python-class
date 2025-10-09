# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 08:20:27 2025

ch2, ch3
@author: Feng

"""
#
# 秒數換算
print('*' * 40)
second = 888888
print(second, '秒數等於 :')

minute = second // 60
hour = minute // 60
day = hour // 24

print(day, '天', hour, '時', minute, '分', second, '秒')

# 求 ax**2 + b*x + c = 0 的解, a=1, b=5, c=12
print('*' * 40)

a = 1
b = 5
c = 12
x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

print(f'{a}*x**2 + {b}*x + {c} =0 的解')
print(' x1 =', x1, '\n', 'x2 =', x2)

# 不同的進位方式
n = 205
print('10進位 :', n)
print('2進位 :', bin(n))
print('8進位 :', oct(n))
print('16進位 :', hex(n))

# 中文字 Unicode 和 bytes 編碼
print('*' * 40)
name = '盧敬翔'
print(name[0], '的 Unicode 以 16 進位表示 :', hex(ord(name[0])))
print(name[1], '的 Unicode 以 16 進位表示 :', hex(ord(name[1])))
print(name[2], '的 Unicode 以 16 進位表示 :', hex(ord(name[2])))
print(name, '的 bytes 的 utf-8 編碼 :', name.encode('utf-8'))
