
# 題目一
def calculate_leibniz_pi(max_denominator_plus_one):
    pi_sum = 0
    sign = 1
    
    for k in range(1, max_denominator_plus_one, 2):
        term = sign * (1 / k)
        pi_sum += term
        sign *= -1
        
    pi = 4 * pi_sum
    return pi

pi_a = calculate_leibniz_pi(11)
pi_b = calculate_leibniz_pi(13)
pi_c = calculate_leibniz_pi(15)

print("-" * 35)
print(f"題目 (a) 的 PI 近似值 (到 1/9):   {pi_a}")
print(f"題目 (b) 的 PI 近似值 (到 1/11): {pi_b}")
print(f"題目 (c) 的 PI 近似值 (到 1/13): {pi_c}")


print("-" * 30)
    

# 題目二

# 初始資料
DISTANCE_KM = 384400  # 地球和月球的距離 (公里)
SPEED_KMPH = 250      # 火箭速度 (公里/分鐘)

# 單位常數
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24

total_minutes_float = DISTANCE_KM / SPEED_KMPH
total_minutes = round(total_minutes_float) 
total_hours = total_minutes // MINUTES_PER_HOUR
days = total_hours // HOURS_PER_DAY

# 3. 計算剩餘的小時數：總小時數除以 24 後的餘數
remaining_hours = total_hours % HOURS_PER_DAY

# 4. 計算剩餘的分鐘數：總分鐘數除以 60 後的餘數
remaining_minutes = total_minutes % MINUTES_PER_HOUR

days = total_minutes // (HOURS_PER_DAY * MINUTES_PER_HOUR)
minutes_after_days = total_minutes % (HOURS_PER_DAY * MINUTES_PER_HOUR)

remaining_hours = minutes_after_days // MINUTES_PER_HOUR
remaining_minutes = minutes_after_days % MINUTES_PER_HOUR


# --- 3. 輸出結果 ---
print(f"--- 火箭飛行時間計算 ---")
print(f"總距離：{DISTANCE_KM} 公里")
print(f"飛行速度：{SPEED_KMPH} 公里/分鐘")
print(f"總共需要 {total_minutes_float:.2f} 分鐘 (含小數)")
print(f"依據捨去秒鐘（四捨五入）後，總共約 {total_minutes} 分鐘。")
print("-" * 30)
print(f"從地球飛到月球所需時間為：")
print(f"{days} 天")
print(f"{remaining_hours} 小時")
print(f"{remaining_minutes} 分鐘")

#題目三
print("-" * 30)
value = input("請輸入三位數: ")
reversed_value = value[::-1]
print(f"反轉後的數字為: {reversed_value}")
print("-" * 30)

#題目四


x1, y1 = map(float, input("請輸入第一點座標 (x1 y1，用空格分隔): ").split())
x2, y2 = map(float, input("請輸入第二點座標 (x2 y2，用空格分隔): ").split())
# 計算距離公式
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f"兩點之間的距離為: {distance}")
print("-" * 30)

#題目五
apple = 100
students = 23
apples_per_student_day = apple // students
not_apple_day = apples_per_student_day+1
remaining_apples = apple - (not_apple_day * students)
remaining_apples = -remaining_apples

print(f"有蘋果吃的天數 {apples_per_student_day} ")
print(f"第幾天蘋果不足 {not_apple_day} ")
print(f"不足的數量 {remaining_apples} ")
print("-" * 30)