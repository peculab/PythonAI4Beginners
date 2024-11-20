# 第六次作業
### 請同學們務必詳閱此份說明檔

- **目標**: 請參考本次課程範例程式碼、簡報，根據本題提供的 `main.py` 及 `utils.py`，繳交 MNIST 訓練後模型 `my_model.keras`。

#### ※ 使用 MNIST 資料集進行手寫數字訓練，並以助教準備的資料集批閱測試。
#### ※ 請訓練你的模型，使其變得更加強健，可以有較好的真實情況手寫的資料的準確率。
#### ※ 作業測試並非使用 MNIST 資料集，為助教另外準備資料集，請務必注意。
#### ※ 作業區提供的測試資料 `data/` 內僅包含部分內容，部分資料集測試結果並不代表實際分數。

## 本次作業已幫大家準備好 `main.py` 及讀取資料的 `utils.py`，可以下載下來做為測試，請同學完成 `my_model.keras` 的訓練。
## `main.py` 及 `utils.py` 皆不可修改，否則會造成資料格式與模型執行錯誤。
## 請勿上傳老師提供的範例模型，系統會自動偵測並不予計分！

## main.py
```python
from tensorflow.keras.models import load_model
from utils import load_custom_mnist_data

# 輸入資料
data_dir = "data"
x_test, y_test = load_custom_mnist_data(data_dir)

# 載入模型
model = load_model('my_model.keras')

# 模型測試
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
from tensorflow.keras.models import load_model
from utils import load_custom_mnist_data

# 輸入資料
data_dir = "data"
x_test, y_test = load_custom_mnist_data(data_dir)

# 載入模型
model = load_model('my_model.keras')

# 模型測試
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f'{test_acc*100:.4f}')
```

## utils.py

```python
import os
import numpy as np
import cv2

def load_custom_mnist_data(data_dir):
    """
    載入個人資料並以 MNIST 資料集架構呈現

    Args:
        data_dir (str): 資料集路徑，以 label 進行資料夾整理
    
    Returns:
        images, labels: 影像與標籤
    """
    images = []
    labels = []

    # 讀取資料集路徑
    for label in os.listdir(data_dir):
        label_path = os.path.join(data_dir, label)
        if not os.path.isdir(label_path):
            continue

        for image_name in os.listdir(label_path):
            image_path = os.path.join(label_path, image_name)
            
            # 以灰階讀入資料
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            if img is None:
                continue  # 跳過非影像或不符合格式之檔案

            # 將影像縮放為 28x28
            img = cv2.resize(img, (28, 28))
            # 反轉影像顏色
            img = abs(255 - img)

            # 將資料集打包為 list
            images.append(img)
            labels.append(int(label))

    # 將資料集 list 轉換為 numpy array
    images = np.array(images)
    labels = np.array(labels)

    # 將資料集 reshape 以符合 MNIST 資料集
    images = images.reshape(-1, 28, 28, 1)

    return images, labels
```
    
## 輸入格式

無

## 輸出格式

無

## 格式相關提醒

#### - 請參考本週與上週課程範例程式碼及簡報，作業僅需依照個人程式碼訓練 `my_model.keras` 模型，其餘程式已包含在提供的 `main.py` 中。
#### - 資料集輸入格式與前處理請參考 `utils.py` 內資料讀入方法。
#### - 本題無圖片輸出。
#### - 輸出準確度即為得分，例：準確度 100% 即為 100 分、準確度 96% 即為 96 分，以此類推。

## Hint

#### - 本次作業是要讓同學們對於圖像辨識有初步認識，了解如何建立模型，並進行模型訓練優化。
#### - 雖然完成作業時，請同學們儲存模型權重的檔案名稱為 `my_model.keras`，才可與 `main.py` 結合，但在上傳前請記得改為規定檔名（`學校_學號_姓名.keras`）上傳，才可辨認繳交學生並批改，系統於自動批改時會改回 `my_model.keras`！
#### - 最後還是要再度提醒，在繳交作業前一定要再三檢查，檔案名稱的格式有沒有打對。
#### - 本題由於 `main.py` 及 `utils.py` 不可更動，所以不會有輸出格式不符的問題，但請務必確保 `my_model.keras` 訓練過程中資料及格式符合 MNIST 資料集格式，否則就會無得分！
#### - 若模型無法載入執行、不符合題目規定或無法執行者則為 0 分。
#### - 更多模型訓練的 hint 請見本週課程簡報。