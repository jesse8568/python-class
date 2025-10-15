
zodiacs = ['鼠', '牛', '虎', '兔', '龍', '蛇', '馬', '羊', '猴', '雞', '狗', '豬']

try:
    # 提示使用者輸入西元年份
    year_str = input("請輸入你出生的西元年（例如 1990 或 2001）：")
    
    # 將輸入的字串轉換為整數
    year = int(year_str)
    
    # 檢查年份是否在合理範圍內
    if 1900 <= year <= 2099:
        index = (year - 1900) % 12
        animal = zodiacs[index]
        
       
        print(f"西元 {year} 年是【{animal}】年。")
    else:
        print("請輸入 19xx 或 20xx 範圍內的有效年份。")

except ValueError:
    print("輸入錯誤，請確保您輸入的是西元年份的數字。")