import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
# 讀取旅館資料
with open('HotelList.json', 'r', encoding='utf-8-sig') as file:
    data = json.load(file)

# 將資料轉換為 DataFrame
hotels_df = pd.json_normalize(data['Hotels'])

# 使用者選擇想住的城市/地點
user_input_city = input()

# 根據城市篩選符合的旅館
matching_hotels = hotels_df[hotels_df['PostalAddress.City'] == user_input_city]

if matching_hotels.empty:
    print("未找到符合地點的旅館/民宿")
else:
    # 詢問是否有特殊需求，直接按enter或輸入'無'可以跳過，即代表無需求
    user_input_special_condition = input()
    
    if user_input_special_condition.lower() and user_input_special_condition.lower()!='無':
        matching_hotels = matching_hotels[matching_hotels['ServiceInfo'].str.contains(user_input_special_condition, case=False, na=False)]

    if matching_hotels.empty:
        print("未找到符合地點和特殊需求的旅館/民宿")
    else:
        # 使用者輸入預算範圍
        user_input_budget = int(input())

        # 根據預算篩選符合的旅館
        final_matching_hotels = matching_hotels[
            (matching_hotels['LowestPrice'] <= user_input_budget) & 
            (matching_hotels['CeilingPrice'] >= user_input_budget)
        ]

        if not final_matching_hotels.empty:
            # 使用 Pandas 內建方法輸出前五個結果
            columns_to_display = ['HotelName', 'LowestPrice', 'CeilingPrice', 'Description', 'PostalAddress.Town', 'PostalAddress.StreetAddress']
            print(final_matching_hotels[columns_to_display].head(5).to_string(index=False))
        else:
            print("未找到符合預算的旅館/民宿")

# 繪製觀光數據的箱型圖
# 讀取數據
df = pd.read_csv('觀光遊憩據點按縣市及遊憩據點交叉分析.csv')

# 將月份列轉換為數值並匯總
months = df.columns[4:-1]  # 獲取所有月份的列
df[months] = df[months].apply(pd.to_numeric, errors='coerce')  # 轉換為數值

# 將縣市的中文名稱替換為英文名稱
county_name_mapping = {
    '金門縣': 'Kinmen',
    '臺東縣': 'Taitung',
    '澎湖縣': 'Penghu',
    "連江縣": "Lianjiang"
}
df['縣市'] = df['縣市'].replace(county_name_mapping)

# 按縣市匯總遊客數
county_summary = df.groupby('縣市')[months].sum().reset_index()

# 將數據轉換為長格式，方便繪製箱型圖
long_format = county_summary.melt(id_vars='縣市', value_vars=months, var_name='月份', value_name='遊客數')

# 創建圖形
plt.figure(figsize=(12, 6))

# 使用 Seaborn 繪製箱型圖，不使用 palette
boxplot = sns.boxplot(x='縣市', y='遊客數', data=long_format)

# 計算中位數、最大值
stats = long_format.groupby('縣市')['遊客數'].agg(['median', 'max'])

for i, county in enumerate(stats.index):
    plt.text(i, stats['median'][county], f'Median: {int(stats["median"][county])}',
             ha='center', va='bottom', fontsize=10, color='black')
    plt.text(i, stats['max'][county], f'Max: {int(stats["max"][county])}',
             ha='center', va='bottom', fontsize=10, color='blue')

plt.xlabel('County', fontsize=14)
plt.ylabel('Tourists', fontsize=14)
plt.grid(axis='y')
plt.xticks(rotation=45)
plt.tight_layout()
#plt.show()
plt.savefig('001.jpg') 
