# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 15:38:49 2025
ch 7
@author: Feng
"""

# 計算 1 到 100 的奇數整數總和至sum
sum = 0
##
for i in range(1, 101, 2):
    sum += i


print(f'計算 1 到 100 的奇數整數總和 = {sum}')
print('*'*40)

# 列出 1 到 100 中所有質數
print('找出 1 到 100 中所有質數:')
##
for i in range(2, 101):
    #拿 2 到 √i 的整數來測試，看看 i 能不能整除，來判斷 i 是否是質數
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i, end=' ')

print()  
print('*'*40)

# 將串列nlist由小排至大
nlist = [10, 5, 2, 7, 3, 8]
print('排序前列表 :', nlist)
for i in range(len(nlist)-1):
    for j in range(i+1, len(nlist)):
        if nlist[i] > nlist[j]:
            nlist[i], nlist[j] = nlist[j], nlist[i]

print('排序後列表 :', nlist)
# nlist = sorted(nlist)
print('*'*40)


# 使用 enumerate() 函數來遍歷一個列表的列表，並在每次迭代中將索引和子列表一起打印出來
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('用enumerate函數遍歷串列 :\n', list_of_lists)
##
for idx, sublist in enumerate(list_of_lists):
    print(f'索引 {idx} -> {sublist}')


print('*'*40)

# 用while模擬一個簡單的猜數字遊戲  回應: "你不猜了","猜小了","猜大了","猜對了"
print('{:^30s}'.format('----猜數字遊戲----'))
secret_number = 29
guess = -1
while guess != secret_number:
    guess = input("請輸入您猜的數字(1~100),按q離開：")
    if guess.lower() == 'q':
        print('你不猜了')
        break
    try:
        guess = int(guess)
    except ValueError:
        print('請輸入數字或q離開')
        continue
    if guess < secret_number:
        print('猜小了')
    elif guess > secret_number:
        print('猜大了')
    else:
        print('猜對了')
print("*"*40)






