# 此函數可根據輸入的成績以及對應的權重計算加權總成績
def calculate_weighted_score(grades, weights):
    # 初始化變數(成績、權重)
    total_score = 0
    total_weight = 0
    # 進行成績與權重的相乘計算，並存入變數中
    for grade, weight in zip(grades, weights):
        total_score += grade * weight
        total_weight += weight
    return total_score / total_weight if total_weight > 0 else 0  

# 此函數可根據成績與等第門檻(thresholds)來評估成績等第
def get_grade(score, thresholds):
    # 遍歷等第門檻，若成績大於或等於門檻值，則傳回對應的等第
    for grade, min_score in thresholds.items():
        if score >= min_score:
            return grade
    return 'F' 

# 定義一個字典，用於存入各成績等第的門檻值
def main():
    grade_thresholds = {
        'A+': 90,
        'A': 85,
        'B+': 80,
        'B': 75,
        'C+': 70,
        'C': 65,
        'D': 60,
        'F': 0
    }

    # 定義科目列表與權重列表
    subjects = ['Chinese', 'Math', 'English', 'Science', 'Society']
    weights = [0.1, 0.3, 0.3, 0.2, 0.1]  # 注意所有權重值的總和應為1

    input_str = input()

    # 將輸入的成績分隔並轉換為浮點數
    try:
        grades = [float(score) for score in input_str.split()]
        if len(grades) != len(subjects):
            print("輸入的成績數量不符合科目數量")
            return
        
        # 檢查每個成績是否在有效範圍內
        for score in grades:
            if score < 0 or score > 100:
                print("成績應在0到100之間")
                return

        # 計算加權總成績
        final_score = calculate_weighted_score(grades, weights)
        # 計算成績等第
        final_grade = get_grade(final_score, grade_thresholds)
        # 顯示結果
        print(f"加權總成績: {final_score:.2f}, 成績等第: {final_grade}")

    except ValueError:
        print("輸入的不是有效的數字")

if __name__ == "__main__":
    main()
