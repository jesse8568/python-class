# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 08:38:43 2025
# ch9-2HW
@author: Feng
"""
# 用zip快速建立字典
fruits =['apple', 'orange', 'grape','kiwi']
prices = [60, 10, 100, 33]

##?
# 使用 zip() 將兩個列表的元素配對，然後用 dict() 轉換成字典
products = dict(zip(fruits, prices))
print(products)

# 遍歷所有鍵
print('_'*30)
topic = '遍歷所有鍵'
print(topic)

##?
# 字典的 for 迴圈預設就是遍歷所有的鍵 (key)
for key in products:
    print(key)

# 遍歷所有值    
print('_'*30)
topic = '遍歷所有值'
print(topic)

##?
# 使用 .values() 方法遍歷所有的值 (value)
for value in products.values():
    print(value)

# 遍歷所有鍵值對    
print('_'*30)
topic = '遍歷所有鍵值對'  
print(topic)

##?
# 使用 .items() 方法，每次迭代會返回一個 (key, value) 的元組
for key, value in products.items():
    print(key, value)

# 使用keys()方法遍歷所有鍵    
print('_'*30)
topic = '使用keys()方法遍歷所有鍵'
print(topic)

##?
# 使用 .keys() 方法明確遍歷所有的鍵 (key)
for key in products.keys():
    print(key)

# 找出特定value的key
#　找出售價為33的水果
print('_'*30)    
topic = '找出售價為33的水果'
print(topic)
price= 33

##?
# 遍歷鍵值對 (key, value)，檢查 value 是否等於目標 price
fruit = ''
for k, v in products.items():
    if v == price:
        fruit = k
        break # 找到後立即停止迴圈
        
print('售價為{}的水果是{}'.format(price,fruit))