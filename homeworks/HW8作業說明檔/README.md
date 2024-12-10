# 第八次作業

- 目標: 根據給定的 [`index.html`](https://github.com/peculab/PythonAI4Beginners/blob/main/homeworks/HW8%E4%BD%9C%E6%A5%AD%E8%AA%AA%E6%98%8E%E6%AA%94/index.html)，讀入網頁後以 BeautifulSoup 抓取卡片內容文字，運用 jieba`、`collections.Counter 斷詞並統計詞頻，輸出下列分析結果：

    1. 根據使用者輸入，分析該詞出現次數。
    2. 利用 jieba.analyse 來找到前十五個關鍵詞。

## 輸入格式

- 輸入有一行，使用者輸入單一詞語，完成後輸出分析該詞出現次數。

## 輸入範例

```
程式
```

## 標準輸出文字格式

- 輸出共有兩行
- 根據使用者輸入詞語，分析該詞出現次數，輸出為單一整數。
- 利用 jieba.analyse 依序以**包含權重**的 list 輸出前十五個關鍵詞（請參考 jieba.analyse.extract_tags 參數）。

## 輸出範例

```
157
[('高中', 0.35650300016220854), ('程式', 0.33587313912767947), ('AI', 0.2733143004778235), ('學習', 0.1557891512723594), ('希望', 0.13209706185299042), ('這門', 0.13119086422935528), ('高一', 0.10201555670355966), ('高工', 0.09727687057398263), ('未來', 0.09292686216245999), ('鼓山', 0.08612721606598078), ('設計', 0.08472743314812528), ('知識', 0.07926114713856881), ('附中', 0.07109192748660265), ('中山', 0.07009022821811614), ('108', 0.06832857511945588)]
```

## 模組內容

```python
import jieba
import jieba.analyse
from bs4 import BeautifulSoup
from collections import Counter

jieba.setLogLevel(jieba.logging.INFO)
```

## Hint

- 本次的作業是要讓各位練習使用 BeautifulSoup 進行網頁爬蟲解析，並使用 jieba、Counter 針對詞頻做統計。
- 最後還是要再度提醒，在繳交作業前一定要再三檢查，檔案名稱的格式有沒有打對，程式也要測試輸出格式是否與範例完全一致喔！
- 由於 requests 無法讀取 local 檔案，請直接以 open() 與 file.read() 讀取後輸入 `BeautifulSoup`。
- 第一行請輸入 `jieba.setLogLevel(jieba.logging.INFO)`，以避免模組 logging 輸出影響作業批改。

## 提示-詞頻

```python
# 排除停用詞
stop_words = set(['所以', '好', '因為', '大家', '的', '是', '了', '我', '也', '在', '和', '就', '不', '有', '他', '她', '你', '我們', '這個', 'https', 'colab', 'com', 'research', 'google', 'drive', 'usp', 'sharing', 'scrollTo'])```