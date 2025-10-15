# 使用元組紀錄過去一週的最高溫和最低溫
high_temps = (30, 28, 29, 31, 33, 35, 32)
low_temps = (20, 21, 19, 22, 23, 24, 20)

# 建立一個空列表，用來存放每天的平均溫度
daily_averages = []

# 使用 zip 將高低溫配對，並進行迴圈
for high, low in zip(high_temps, low_temps):
    daily_avg = (high + low) / 2
    daily_averages.append(daily_avg)

print("每日最高溫:", high_temps)
print("每日最低溫:", low_temps)
print("整周最高溫:", max(high_temps))
print("整周最低溫:", min(low_temps))
print("過去一週的平均溫度")
str_averages = [f"{temp:.1f}" for temp in daily_averages]
print(" ".join(str_averages))

