
input_str = input("請輸入5個考試成績（可用空格或逗號分隔）：")

try:
    scores_str_list = input_str.replace(',', ' ').split()
    
    # 檢查使用者是否剛好輸入了5個成績
    if len(scores_str_list) != 5:
        print(f"錯誤：您輸入了 {len(scores_str_list)} 個成績，請剛好輸入5個。")
    else:
        scores = [int(score) for score in scores_str_list]   
        print(f"分數串列       : {scores}")
        scores_desc = sorted(scores, reverse=True)
        print(f"高分往低分排列 : {scores_desc}")
        scores_asc = sorted(scores)
        print(f"低分往高分排列 : {scores_asc}")
        highest_score = max(scores)
        print(f"最高分         : {highest_score}")
        total_score = sum(scores)
        print(f"總分           : {total_score}")

except ValueError:
    print("輸入錯誤，請確保您輸入的是數字，並用正確的分隔符號。")