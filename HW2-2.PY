try:
    a = float(input("請輸入第一個邊長："))
    b = float(input("請輸入第二個邊長："))
    c = float(input("請輸入第三個邊長："))

    # 檢查所有邊長是否為正數
    if a > 0 and b > 0 and c > 0:
        # 檢查是否滿足三角形的條件：任意兩邊之和大於第三邊
        if (a + b > c) and (a + c > b) and (b + c > a):
            # 如果滿足條件，計算並輸出周長
            perimeter = a + b + c
            print(f"這三個邊長可以形成三角形，周長為：{perimeter}")
        else:
            print("這不是三角形的邊長。")
    else:
        print("三角形的邊長必須是正數。")

except ValueError:
    print("輸入錯誤，請確保您輸入的是數字。")