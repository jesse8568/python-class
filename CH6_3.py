# -*- coding: utf-8 -*-
"""
創建於 2025 年 9 月 24 日星期三 15:38:49
第 6-3 章
@作者：馮
"""

title = ['人名', '數學', '中文', '國文']
scores = [['Leo', 80, 92, 80],
          ['丹', 75, 90, 70],
          ['Ann', 90, 30, 80]]
newstu = ['Lu', 80, 85, 88]

# 把盧的成績加到分數中
scores.append(newstu)

# 印出表頭與所有成績
print(title)
print(scores[0], scores[1], scores[2], scores[3], sep='\n')
print('*' * 40)

# 讀取擁有者名稱為 name 序列
i = 0
name = [row[i] for row in scores]
print(title[i], name)

# 讀取所有數學成績為 math 串列
i = 1
math = [row[i] for row in scores]
print(title[i], math)

# 找出數學最高分與最低分
maxScore = max(math)
maxIdx = math.index(maxScore)
minScore = min(math)
minIdx = math.index(minScore)

print(f"{name[maxIdx]} 的數學最高分，分數為 {math[maxIdx]}")
print(f"{name[minIdx]} 的數學最低分，分數為 {math[minIdx]}")
