import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from model import Select_feature, Training 
import re

file_path = 'Price.xls' 
df = pd.read_excel(file_path, skiprows=1)

# 選擇適合的處理方式，這裡選擇直接刪除包含 NaN 的行
df = df.dropna()

df['樓別/樓高'] = df['樓別/樓高'].str.replace('夾層', '')

# 假設 df 是你的資料框，先定義一個函數來處理不同的樓別/樓高格式
def extract_levels(row):
   # 使用正規表示式擷取層數，支援數字和中文數字，並忽略多餘的部分
   match = re.match(r'(\D*)(\d+|\w+)層.*?(\d+|\w+)層', row)
   if match:
      lower_level = match.group(2)  # 樓別（lower level）
      upper_level = match.group(3)  # 樓高（upper level）
      return pd.Series([lower_level, upper_level])
   else:
      return pd.Series([None, None])  # 如果無法匹配則傳回 None

# 應用提取函數，並新增列
df[['樓別', '樓高']] = df['樓別/樓高'].apply(extract_levels)

# 轉換為數值類型，處理中文數字
def chinese_to_number(chinese_str):
    chinese_numerals = {
        '零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5,
        '六': 6, '七': 7, '八': 8, '九': 9, '十': 10
    }
    number = 0
    if '十' in chinese_str and len(chinese_str)>1:
        #print(chinese_str)
        parts = chinese_str.split('十')
        number += chinese_numerals[parts[0]] * 10 if parts[0] else 10
        if len(parts) > 1:
            #print(parts)
            number += chinese_numerals[parts[1]]
    else:
        number = chinese_numerals.get(chinese_str, None)
    return number

# 將樓別和樓高轉換為數值
df['樓別'] = df['樓別'].apply(chinese_to_number)
df['樓高'] = df['樓高'].apply(chinese_to_number)

# 確保類型為浮點數
df['樓別'] = df['樓別'].astype(float)
df['樓高'] = df['樓高'].astype(float)

# 去掉百分比號並將"主建物佔比"轉換為浮點數
df['主建物佔比'] = df['主建物佔比'].str.replace('%', '').astype(float) / 100

# 選擇特徵和目標變數
# 需要選擇適合的特徵列，並進行適當的資料清理，例如將「總價(萬元)」和「單價(萬元/坪)」的數值去掉逗號
# 確保這些列是字串類型，以便使用 .str.replace
df['總價(萬元)'] = df['總價(萬元)'].astype(str).str.replace(',', '').astype(float)
df['單價(萬元/坪)'] = df['單價(萬元/坪)'].astype(str).str.replace(',', '').astype(float)

# 對所有可能為數值的欄位進行相同的清理操作
def clean_column(column):
    return column.str.replace(',', '').astype(float)

# 如果列中有其他需要處理的數值列，可以在這裡新增
df['車位總價(萬元)'] = clean_column(df['車位總價(萬元)'].astype(str))

# 將'有無電梯'轉換為二進制數值（0表示沒有電梯，1表示有電梯）
df['有無電梯'] = df['電梯'].apply(lambda x: 1 if x == '有' else 0)
df['有無管理組織'] = df['管理組織'].apply(lambda x: 1 if x == '有' else 0)
# print(df.head(5))

x = Select_feature(df)
y = df['總價(萬元)']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = Training(x_train, y_train)

y_pred = model.predict(x_test)

# print("R-squared (R²):", r2_score(y_test, y_pred))

# R-Squared 值判斷
r2 = r2_score(y_test, y_pred)
threshold = float(input())
print(r2>threshold)