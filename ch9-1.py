# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 08:38:43 2025
# ch9-1HW
@author: Feng
"""
#
students = {
    'John Doe': 30,
    'Jane Doe': 25,
    'Peter Smith': 20,
}

products = {
    'iPhone 13 Pro': 1000,
    'iPad Pro': 900,
    'Apple Watch S7': 399,
}

print(students)
print(products)

# 使用 [] 運算子讀取鍵對應的值 : John Doe age? iPhone 13 Pro price ?
print('使用 [] 運算子讀取鍵對應的值')
name = 'John Doe'
print(f"The age of {name} is {students[name]}")
product = 'iPhone 13 Pro'

##?
price = products[product]
print('The price {} is {}.'.format(product, price))
print('_'*30)


# 使用 dict.get() 方法讀取鍵對應的值，如果鍵不存在，則返回指定的默認值。
# iPhone 13 Pro price? iPhone 14 Pro price?
print('使用 dict.get() 方法讀取')
product = 'iPhone 13 Pro'

##?
# .get() 方法，如果找到鍵則返回對應的值
price = products.get(product)
print('The price of {} is {}'.format(product,price))
product = 'iPhone 14 Pro'

##?
# .get(key, default_value) 方法，'iPhone 14 Pro' 不存在，會返回指定的默認值 None
price = products.get(product)
print('The price of {} is {}'.format(product,price))
print(products)
print('_'*30)

# 使用 dict.setdefault() 方法新增一個鍵值對，如果鍵已存在，則返回鍵對應的值
# 新增 'AppleTV', price=111 & 222
print('使用 dict.setdefault() 方法')
product = 'AppleTV'

##?
# 'AppleTV' 不存在，會被新增，並返回設定的值 111
price = products.setdefault(product, 111)
print('The price of {} is {}'.format(product,price))
product = 'AppleTV'

##?
# 'AppleTV' 已存在，不會被修改，並返回它已有的值 111 (而不是 222)
price = products.setdefault(product, 222)
print('The price of {} is {}'.format(product,price))
print(products)
print('_'*30)

# 使用 dict.pop() 方法刪除鍵值對，並返回鍵對應的值
# 讀取並刪除'iPhone 13 Pro'
print('使用 dict.pop() 讀取並刪除 iPhone 13 Pro方法後')

##?
# .pop(key) 會刪除鍵值對並返回其值
price = products.pop('iPhone 13 Pro')
print(price)
print(products)
print('_'*30)

# del 刪除字典特定元素
# 刪除'AppleTV'
print('del 刪除 AppleTV 後')
##?
del products['AppleTV']


print(products)
print('_'*30)

# 用解包新增一個或多個鍵值對
# 新增 'iphone 16': 2000, 'Apple Watch S9': 500
print('新增一個或多個鍵值對')
print('before:', products)
newproducts = {'iphone 16': 2000, 'Apple Watch S9': 500}

##? 
# 使用 ** 解包運算子將新字典的內容合併到舊字典中
products = {**products, **newproducts}

print('after:',products)