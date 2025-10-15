# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 08:19:23 2025
   ch10-2.py
@author: Feng
"""
# 定義兩個集合
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
print("集合set1 :", set1)
print("集合set2 :", set2)

# 計算交集 (Intersection)
#?
# 交集：兩個集合中都存在的元素
intersection = set1 & set2
# 另一種寫法：set1.intersection(set2)
print("交集 :", intersection)

# 計算聯集 (Union)
#?
# 聯集：兩個集合的所有不重複元素
union = set1 | set2
# 另一種寫法：set1.union(set2)
print("聯集 :",union)

# 計算差集 (Difference)
#?
# 差集：只存在於 set1 但不存在於 set2 的元素
difference = set1 - set2
# 另一種寫法：set1.difference(set2)
print("差集", difference)

# 計算對稱差 (Symmetric Difference)
#?
# 對稱差：存在於任一集合，但不同時存在於兩個集合的元素 (即聯集減去交集)
symmetric_difference = set1 ^ set2
# 另一種寫法：set1.symmetric_difference(set2)
print("計算對稱差", symmetric_difference)