# -*- coding: utf-8 -*-
"""
主程式選單範例
@author: Feng
"""

# ---------------- Function 區 ----------------
def calc_score():
    """輸入姓名與成績，計算平均"""
    name = input('請輸入姓名 : ')
    eng, math, phy = map(float, input('請輸入英文、數學、物理成績(以逗號分隔) : ').split(','))
    avg = (eng + math + phy) / 3

    print(f'姓名 : {name:<5}英文 : {eng:<5.1f}數學 : {math:<5.1f}物理 : {phy:<5.1f} 平均 : {avg:<5.1f}')



#output
'''
PS E:\Desktop\python class> & C:/Users/asd10/AppData/Local/Microsoft/WindowsApps/python3.11.exe "e:/Desktop/python class/ch4_5_6hw.py"
請輸入姓名 : 盧敬翔
請輸入英文、數學、物理成績(以逗號分隔) : 54.56486,87.4562,98.5466
姓名 : 盧敬翔  英文 : 54.6 數學 : 87.5 物理 : 98.5  平均 : 80.2 
姓名 : 盧敬翔  英文 : 54.6 數學 : 87.5 物理 : 98.5  平均 : 80.2
姓名 : 盧敬翔  英文 : 54.6 數學 : 87.5 物理 : 98.5  平均 : 80.2
'''


def calc_ticket():
    """票價計算"""
    PRICE = 850
    age = int(input('歡迎光臨，請輸入你的年紀 ? '))

    if age <= 6 or age >= 75:
        PRICE *= 0.5
    elif 7 <= age <= 12 or 60 <= age <= 74:
        PRICE *= 0.8
    else:
        PRICE *= 0.9

    print(f'你的實際票價是 {int(PRICE)} 元')

'''
PS E:\Desktop\python class> & C:/Users/asd10/AppData/Local/Microsoft/WindowsApps/python3.11.exe "e:/Desktop/python class/ch4_5_6hw.py"
歡迎光臨，請輸入你的年紀 ?21
你的實際票價是 765 元
PS E:\Desktop\python class> & C:/Users/asd10/AppData/Local/Microsoft/WindowsApps/python3.11.exe "e:/Desktop/python class/ch4_5_6hw.py"
歡迎光臨，請輸入你的年紀 ?111
你的實際票價是 425 元
PS E:\Desktop\python class> & C:/Users/asd10/AppData/Local/Microsoft/WindowsApps/python3.11.exe "e:/Desktop/python class/ch4_5_6hw.py"
歡迎光臨，請輸入你的年紀 ?3
你的實際票價是 425 元
'''


def fruit_list():
    # list的操作
    # fr1, fr2 兩家水果行賣的水果
    fr1 = ['apple', 'kiwi', 'pear', 'grape']
    fr2 = ['mango', 'grape', 'pear']
    

    print('第1家水果行賣:{}\n第2家水果行賣:{}'.format(fr1, fr2))
    print('-' * 40)

    fre = fr1 + fr2   # 先用 + 直接合併
    fra = []

    # combine 2 list by '+'
    print('兩家水果行賣(用+):\n{}'.format(fr1 + fr2))
    print('-' * 40)

    # combine 2 list by 'extend' to fre
    fre = fr1.copy()      # 先複製一份，不然會改到原本的 fr1
    fre.extend(fr2)       # extend 會把 fr2 的元素逐一加入 fre
    print('兩家水果行賣(用extend):\n{}'.format(fre))
    print('-' * 40)

    # combine 2 lists by append() to fra
    for fruit in fr1:
        fra.append(fruit)
    for fruit in fr2:
        fra.append(fruit)
    print('兩家水果行賣(用append):\n{}'.format(fra))
    print('-' * 40)

    # remove duplicated fruits 'pear'和 'grape' from fra
    fra = list(set(fra))   # 轉成集合 set 去重，再轉回 list
    print('兩家水果行的水果種類(不重覆):\n{}'.format(fra))
    print('-' * 40)

    # find index of 'grape' in list
    search = 'grape'
    pos = fra.index(search)
    print('{}是水果清單中的第{}種水果'.format(search, pos + 1))
    print('-' * 40)

    # remove element 'grape' at specific location from list
    search = 'grape'
    pos = fra.index(search)   # 找出位置
    _ = fra.pop(pos)          # pop 刪掉該位置的元素
    print('移除{}後，兩家水果行賣的水果種類{}'.format(search, fra))
    print('-' * 40)

    # check if 'mango' 和 'lemon' element exist in a list fre
    nfr1 = 'mango'
    nfr2 = 'lemon'
    if nfr1 in fre:
        print('二家水果行有賣{}'.format(nfr1))
    else:
        print('二家水果行沒有賣{}'.format(nfr1))

    if nfr2 in fre:
        print('二家水果行有賣{}'.format(nfr2))
    else:
        print('二家水果行沒有賣{}'.format(nfr2))
    print('-' * 40)

    """水果清單操作"""
    fr1 = ['apple', 'kiwi', 'pear', 'grape']
    fr2 = ['mango', 'grape', 'pear']

    print('第1家水果行賣:', fr1)
    print('第2家水果行賣:', fr2)

    fre = fr1.copy()
    fre.extend(fr2)

    fra = []
    for f in fr1:
        fra.append(f)
    for f in fr2:
        fra.append(f)

    fra = list(set(fra))  # 去重

    print('兩家水果行合併(不重複):', fra)

    if 'grape' in fra:
        pos = fra.index('grape')
        print(f'grape 在清單的第 {pos+1} 項')

    if 'mango' in fre:
        print('有賣 mango')
    else:
        print('沒有賣 mango')

    if 'lemon' in fre:
        print('有賣 lemon')
    else:
        print('沒有賣 lemon')

#output
'''
PS E:\Desktop\python class> & C:/Users/asd10/AppData/Local/Microsoft/WindowsApps/python3.11.exe "e:/Desktop/python class/ch4_5_6hw.py"
第1家水果行賣:['apple', 'kiwi', 'pear', 'grape']
第2家水果行賣:['mango', 'grape', 'pear']
----------------------------------------
兩家水果行賣(用+):
['apple', 'kiwi', 'pear', 'grape', 'mango', 'grape', 'pear']
----------------------------------------
兩家水果行賣(用extend):
['apple', 'kiwi', 'pear', 'grape', 'mango', 'grape', 'pear']
----------------------------------------
兩家水果行賣(用append):
['apple', 'kiwi', 'pear', 'grape', 'mango', 'grape', 'pear']
----------------------------------------
兩家水果行的水果種類(不重覆):
['apple', 'kiwi', 'grape', 'mango', 'pear']
----------------------------------------
grape是水果清單中的第3種水果
----------------------------------------
移除grape後，兩家水果行賣的水果種類['apple', 'kiwi', 'mango', 'pear']
----------------------------------------
二家水果行有賣mango
二家水果行沒有賣lemon
----------------------------------------
'''


# ---------------- 主程式區 ----------------
def main():
    while True:
        print("\n=== 主選單 ===")
        print("1. 成績計算")
        print("2. 票價計算")
        print("3. 水果清單操作")
        print("0. 離開")

        choice = input("請輸入選項 (0-3): ")

        if choice == "1":
            calc_score()
        elif choice == "2":
            calc_ticket()
        elif choice == "3":
            fruit_list()
        elif choice == "0":
            print("程式結束")
            break
        else:
            print("輸入錯誤，請重新輸入。")


if __name__ == "__main__":
    main()
