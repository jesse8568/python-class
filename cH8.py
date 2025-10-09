# 3個元組 tup1~3
tup1 = ('a01', 'a02', 'a03')
tup2 = (80, 90, 75)
tup3 = (70, 85, 90)

print('元組1:', tup1)
print('元組2:', tup2) 
print('元組3:', tup3)
print('-'*40)

# 打包 tup1~3
x1 = zip(tup1, tup2, tup3)
print('打包 tup1~3: \n', tuple(x1))
print('-'*40)

# 或者直接存成另一個 zip
x2 = zip(tup1, tup2, tup3)
print('打包 tup1~3: \n', tuple(x2))
print('-'*40)
print('在測試打包 tup1~3: \n', tuple(x2))

# 將已打包的 x2 先解包再分配
x2 = zip(tup1, tup2, tup3)   # zip 只能遍歷一次，要重新生成
x3 = zip(*x2)
print('x2 先解包再分配:', tuple(x3))
print('-'*40)

# 解包回三個 tuple
x2 = zip(tup1, tup2, tup3)
utup1, utup2, utup3 = zip(*x2)
print(f"解包後的 tup1~3:\n{utup1}\n{utup2}\n{utup3}")
print('-'*40)
