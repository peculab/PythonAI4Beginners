# 第五次作業
### 請同學們務必詳閱此份說明檔

- **目標**: 請根據提供的 xls 檔 `Price.xls`，並參考本題提供的 `main.py`，撰寫出要求的函式於`model.py`中。

    1. 函式一：`Select_feature`
       - 功能要求：從 xls 檔中篩選出與 `總價`相關的特徵，選取越相關的特徴其結果會越好。
       - 傳入參數為從xls讀到的並完成清理的DataFrame。
       - 回傳值為選擇好要用來訓練與預測的特徵欄位(x)。
       - 函式參數型態Type Hints：`def Select_feature(df: DataFrame) -> ndarray:`

    2. 函式二：`Training`
       - 功能要求：創建線性回歸模型並訓練。
       - 傳入參數為用來訓練的特徵與答案(Label)。
       - 回傳值為訓練好的模型，並在後續的主程式中測試與評估此模型。
       - 函式參數型態Type Hints：`def Training(x_train: ndarray, y_train: ndarray) -> Union[BaseEstimator, LinearRegression, ...]:`
         
#### ※ 請完成上述的兩個函式於`model.py`中以求得更好的R-Squared 值。
#### ※ 以分別在兩個函式內使用課程學所的方法，來提升最後的 R-Squared 值，同學們可以想想有哪些方法可以使用。

## 本次作業會幫大家準備好`main.py`，大家可以下載下來做為測試，請同學完成`model.py`。
## 此`main.py`不可修改，否則會造成與批改答案不同而無法通過批改。

## main.py
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from model import Select_feature, Training 
import re

### 讀取檔案
file_path = 'Price.xls' 
df = pd.read_excel(file_path, skiprows=1)

# 選擇適合的處理方式，這裡選擇直接刪除包含 NaN 的行
df = df.dropna()

### 分離樓別與樓高
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

### 其他資料清理與型態轉換

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

### 主程式
x = Select_feature(df) #這裡呼叫同學們寫的選擇特徵函式
y = df['總價(萬元)']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = Training(x_train, y_train) #這裡呼叫同學們寫的訓練函式

y_pred = model.predict(x_test)

# print("R-squared (R²):", r2_score(y_test, y_pred)) #自己測試的時候可以把R²印出來。

# R-Squared 值判斷
r2 = r2_score(y_test, y_pred)
threshold = float(input())
print(r2>threshold)
```

## 同學們需完成的`model.py`
```python
def Select_feature(df):
    ...
    return x

def Training(x_train, y_train):
    ...
    return model
```
    
## 輸入格式

### 輸入有一行，為一整數

該整數代表 R-Squared 的目標值，以此來判斷同學們訓練的模型是否有超過此目標值。

## 輸出格式

### 輸出有一行，為一布林值 ( True or False )
根據輸入的目標值，判斷模型實際的 R-Squared 值是否大於該目標值而印出True/False。


## 範例
### 假設最終算出的 R-Squared 值為 0.689 
### 輸入範例 1

```text
0.5
```

### 輸出範例 1

```text
True
```

### 輸入範例 2

```text
0.6
```

### 輸出範例 2

```text
True
```


### 輸入範例 3

```text
0.7
```

### 輸出範例 3

```text
False
```

## 格式相關提醒

### - 作業只需要完成兩個函式於`model.py`即可 ( 請參照 `同學們需完成的部分` )，其餘程式都已包含在提供的 `main.py` 中。

### - 本題無圖片輸出。

## Hint

#### - 本次作業是要讓同學們對於機器學習有一些初步的認識，了解如何建立一個模型，並進行線性回歸的預測。

#### - 雖然在練習時請同學們完成的程式叫`model.py`，這樣才組合得起來，但在上傳前記得要改成規定的檔名(`學校_學號_姓名.py`)上傳喔，這樣才能知道這份程式是誰傳的，系統在自動批改時會幫你改回`model.py`！

#### - 最後還是要再度提醒，在繳交作業前一定要再三檢查，檔案名稱的格式有沒有打對，程式也要測試輸出格式是否與範例完全一致喔！

#### - 本題由於`main.py` 不可更動，所以不會有輸出格式不符的問題，但請務必確保`model.py`中的兩個函數的參數與回傳值型式與題要要求一致才能成功被`main.py` 呼叫，否則就會無無得分喔！

#### - `model.py`中的兩個函式請依題目要求作答，請勿在其中有任何的輸入(`input()`)或輸出(`print()`)。

## 配分

|  R² | 得分 |
|-----|-----|
| 0.4 | 30  |
| 0.5 | 55  |
| 0.6 | 80  |
| 0.65| 95  |
| 0.7 | 100 |

#### ※ 若無法與`main.py`組合、不符合題目規定或無法執行者則為0分。