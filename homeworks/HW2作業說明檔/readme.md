# 第二次作業

- **目標**: 請根據給定的 csv 檔，完成以下的分析
  1. 找出消費金額前十高的品項，並生成直方圖。
  2. 列印出消費最高的品項名稱以及金額。
  3. 分別找出星期一到日的消費比例，並生成圓餅圖。
  4. 分別找出星期一到日消費最高的日子，並列印出日期。

- **輸出檔名**: 直方圖與圓餅圖都請匯出成 ` jpg 檔 `，並且依照指定名稱命名
  1. 消費金額前十高的品項直方圖: `001.jpg`
  ![001.jpg](001ans.jpg)
  2. 星期一到日的消費比例圓餅圖: `002.jpg`
  ![002.jpg](002ans.jpg)

## 部分圖表設定
  1. 直方圖:
```
plt.xlabel("Item") # x軸的標籤
plt.ylabel("Total Amount Spent") # y軸的標籤
```
  2. 圓餅圖:
```
df =                  

# 注意在取比例的時候不要有小數點，一律四捨五入到整數位 
plt.pie(data=df, labels=df.day, x='Amount',autopct='%.0f%%')
```

## 輸出格式
- 圖表不用設定標題。
- 圖表一律以預設格式生成 **(不要修改圖像大小以及顏色)**。
- 數據輸出要完全符合格式 **(格式請參照輸出範例)**，否則會判定為 0 分。 
- 注意在列印數據時，兩個不同目標的數據要以空行隔開。

如下所示:
```
  #列印出消費最高的品項名稱以及金額
  Item with the highest spending is apple
  Total amount spent is 500
                                              ← (這裡是空行)
  #分別找出星期一到日消費最高的日子，並列印出日期
  Highest spending day on Monday is 2023-05-27
                          .
                          .
                          .
```
## 數據輸出範例
```
Item with the highest spending is apple
Total amount spent is 500

Highest spending day on Monday is 2024-05-27
Highest spending day on Tuesday is 2024-05-07
Highest spending day on Wednesday is 2024-05-08
Highest spending day on Thursday is 2024-05-16
Highest spending day on Friday is 2024-05-03
Highest spending day on Saturday is 2024-05-11
Highest spending day on Sunday is 2024-05-05
```


## Hint
- 本次的作業是要讓各位可以更認識 `pandas` 以及 `matplotlib`，了解該如何
從 csv 檔中擷取出需要的數據，並生成圖表，以及如何根據這些數據以及圖表去進
行分析。
- 最後還是要再度提醒，在繳交作業前一定要再三檢查，檔案名稱的格式有沒有打對，程式也要測試輸出格式是否與範例完全一致喔！
- 記得程式中不可以有`plt.show()`喔！否則會造成自動批改因顯示圖表卡住而超時得到0分喔！