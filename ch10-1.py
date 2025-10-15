# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 08:19:23 2025
   ch10-1.py
@author: Feng
"""

# 去除串列中的重複值
# 建立一個串列
list1 = [1, 2, 3, 1, 2, 4]
print("新建立的串列 :", list1)

# 使用集合來去除重複值
#?
set1 = set(list1) 
print("去除重複值後的集合:", set1)

# 將去除重複值後的集合轉換為列表
#?
list2 = list(set1)
# 列印出去除重複值後的列表
print("去除重複值後的列表", list2)

# 去除字串中的重複字元
# 建立一個字串
str1 = "Hello world! I like Python"
print("新建立的字串:", str1)
# 將字串內字元(不重複)轉為集合
#? 
set2 = set(str1)
print("字串內的(不重複)字元:", set2)


# 去除統計資料中的重複值
# 建立一個統計資料 (這裡是一個包含列表的字典)
data = {
    "name": ["John", "Mary", "John", "Peter", "Mary"],
    "age": [20, 25, 20, 22, 25],
}
print("新建立的統計資料 :", data)

# 使用集合來去除重複的 name值
#?
# 取得 'name' 列表的值，並轉換為集合
set3 = set(data['name'])
print("去除重複 name 後的集合:", set3) # 這裡額外印出檢查

# 將去除重複值後的集合轉換為列表
#?
names = list(set3)
print("去除重複 name 後的列表:", names) # 這裡額外印出檢查

# 重新建立統計資料 (只保留去重後的 names，age 列表可能需要調整，但作業只要求更新 name)
# 如果只需要更新 name 欄位
#?
data = {
    "name": names,
    "age": list(set(data['age'])) # 順帶將 age 也去重，如果需要保持長度一致，這一步要小心處理
}


print("去除統計資料中的重複name後 :", data)