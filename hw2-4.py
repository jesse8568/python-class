# 初始化 e 的值（級數的第一項 1）和階乘的初始值
e = 1.0
factorial = 1.0

# 迴圈從 i = 1 到 100
for i in range(1, 101):
    factorial *= i
    e += 1.0 / factorial
    
    # 檢查 i 是否為 10 的倍數，如果是就輸出結果
    if i % 10 == 0:
        print(f"當 i 是 {i:3d} 時 e = {e:.50f}")