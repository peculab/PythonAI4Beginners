# 第三次作業

- **目標**: 請撰寫一python程式讀取`觀光遊憩據點按縣市及遊憩據點交叉分析.csv`及`HotelList.json`完成以下目標
  
   **1**.利用csv檔將四個縣的所有年月的觀光人數加總並生成箱型圖，並標註Max、Medium。
 
   **2**.利用json檔，使用者可以自行輸入`縣市`、`特殊需求`、`價位`來檢索是否有符合需求的旅館，並將結果印出HotelName、LowestPrice、 CeilingPrice、 Description、 PostalAddress.Town、 PostalAddress、StreetAddress等欄位的資訊。(請乎視結果的排版很醜，將原生的結果輸出即可。)，且輸入5筆資料即可


-輸出檔名: 箱型圖請匯出成 jpg 檔，並且依照指定名稱命名

四個縣觀光人數箱型圖:     001.jpg 

## 輸入格式
- 輸入有三行。
- 第一行為`縣市`是一字串。
- 第二行為`特殊需求`是一字串，若無可輸入`無`或是直接按`enter`不輸入來跳過。
- 第三行為`價位`是一整數範圍為1~20000。

## 輸出格式
1.圖表不用設定標題。

2.圖表一律以預設格式生成 (不要修改圖像大小以及顏色)。

3.數據輸出要完全符合格式 (格式請參照輸出範例)，否則會判定為 0 分。

4.建議補上
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)
防止版本太舊



- **部分圖表設定**:
 ```
#為防止中文亂碼出現，將縣市的中文名稱替換為英文名稱

county_name_mapping = {
    '金門縣': 'Kinmen',
    '臺東縣': 'Taitung',
    '澎湖縣': 'Penghu',
    "連江縣": "Lianjiang"

}
```
```
#需要固定這些尺寸，以防測資出現錯誤
plt.figure(figsize=(12, 6))
plt.xlabel('County', fontsize=14)
plt.ylabel('Tourists', fontsize=14)
plt.grid(axis='y')
plt.xticks(rotation=45)  
plt.tight_layout()

```

## 數據輸入範例
```
臺北市
無
5000

```

## 數據輸出範例
```
HotelName  LowestPrice  CeilingPrice                                                                                                                                                                                                                     Description PostalAddress.Town PostalAddress.StreetAddress
  丰居旅店忠孝館         2420         20000                                                                                                                                                                                                                        位於臺北市的旅館                大安區 復興南路1段126巷1號3樓(含3樓、3樓夾層、4樓)
     松河璞旅         2600         13000                                                                                                                                                                                                                        位於臺北市的旅館                松山區                松河街112號1樓至8樓
 二十輪旅店大安店         4500          5000                                SWIIO以優雅質感生活為主軸、舒適住宿空間為前提，在大安區建造了一個專屬品味生活旅人的住所。由設計師方序中操刀的旅館品牌識別，內部空間則是擅長電影美術設計的郭志達負責。幾何形狀的白色建築外觀是經營者董鴻林的設計發想，在密布灰色建物的都市裡，醒目得彷彿是座落於質感象限內的風格指標，用純淨潔白的色澤說著故事，架構出一個獨立於空間之外的旅行思維，成為每個旅人停留過後都會想再次入住的家。                大安區    大安路一段183號，185號，185號2樓至7樓
  城市商旅南東館         3000         20000 城市商旅南東館以低調奢華、時尚沉穩的設計理念，於台北市東區再造另一頂級精品旅館，全館融合東西調性，佐以顏色、光線、線型等元素，變化出獨特的旅居空間。全館客房為挑高三米六的舒適高度，融合金箔的建材元素完美呈現精品旅館之典範，讓旅客，體驗典雅溫馨的住房服務。便利的交通網絡，距離松山機場、松山火車站、小巨蛋、信義商圈及 101大樓、松山文創園區等，僅須5-10分鐘車程，距離內湖科技園區、南港軟體科技園區、世貿、南港展覽館等商務重地，僅15分鐘車程。                松山區           南京東路五段411號地下三樓至7樓
     在家行旅         1000          6200                                                                                       在家行旅於台北市中山區，鄰近台北火車站，周圍有市立美術館、中正紀念堂、行天宮、小巨蛋、台北古城(北門)、西門町夜市、迪化老街(大稻埕)、萬華西門紅樓、國家音樂廳、華山藝文特區等等。台北雙連商圈的新地標，不只是提供來台旅客的平價休憩選擇，更是台北市裡充滿個性時尚的街頭藝術品。                中山區      中山北路二段65巷2弄3號1-4樓  

```

## 小提示: 

1.箱型圖
```
#箱形圖算中位數、最大數的語法
for i, county in enumerate(stats.index):
    plt.text(i, stats['median'][county], f'Median: {int(stats["median"][county])}',
             ha='center', va='bottom', fontsize=10, color='black')
    plt.text(i, stats['max'][county], f'Max: {int(stats["max"][county])}',
             ha='center', va='bottom', fontsize=10, color='blue')
```
## 箱型圖要求模樣:
![image](https://github.com/user-attachments/assets/53bd19eb-861c-43bd-85a6-c920e32571f5)
2.json


## 提醒

### `根據城市篩選符合的旅館`參考程式碼
```
matching_hotels = hotels_df[hotels_df['PostalAddress.City'] == user_input_city]
```

### 若一開始輸入`縣市`就找不到任何一間符合的旅館，請輸出`未找到符合地點的旅館/民宿`。
```
if matching_hotels.empty:
    print("未找到符合地點的旅館/民宿")
```

### 若輸入的`特殊需求`無法被滿足，沒有旅館符合的請輸出 `未找到符合地點和特殊需求的旅館/民宿`。
```
if matching_hotels.empty:
        print("未找到符合地點和特殊需求的旅館/民宿")
```

### `詢問是否有特殊需求，直接按enter或輸入'無'可以跳過，即代表無需求`的參考式碼
```
else:
    # 詢問是否有特殊需求，直接按enter或輸入'無'可以跳過，即代表無需求
    user_input_special_condition = input()
    
    if user_input_special_condition.lower() and user_input_special_condition.lower()!='無':
        matching_hotels = matching_hotels[matching_hotels['ServiceInfo'].str.contains(user_input_special_condition, case=False, na=False)]from tabulate import tabulate
```

### 若輸入的`價位`無法被滿足，沒有旅館符合的請輸出 `未找到符合地點和特殊需求的旅館/民宿`。
```
if not final_matching_hotels.empty:
            # 使用 Pandas 內建方法輸出前五個結果
            columns_to_display = ['HotelName', 'LowestPrice', 'CeilingPrice', 'Description', 'PostalAddress.Town', 'PostalAddress.StreetAddress']
            print(final_matching_hotels[columns_to_display].head(5).to_string(index=False))
        else:
            print("未找到符合預算的旅館/民宿")
```

## Hint
- 本次的作業是要讓各位可以更活用 pandas 以及 matplotlib，同時再增加了json的使用
還是要再度提醒，在繳交作業前一定要再三檢查，檔案名稱的格式有沒有打對，程式也要測試輸出格式是否與範例完全一致喔！
記得程式中不可以有plt.show()喔！否則會造成自動批改因顯示圖表卡住而超時得到0分喔！
