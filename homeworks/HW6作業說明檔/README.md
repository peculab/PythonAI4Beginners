# 第六次作業
### 請同學們務必詳閱此份說明檔

- **目標**: 請參考本次課程範例程式碼、簡報，根據本題提供的 `main.py`，繳交 MNIST 訓練後模型 `my_model.keras`。

#### ※ 使用 MNIST 資料集進行手寫數字訓練。
#### ※ 請訓練你的模型，使其變得更加強健，可以有較好的真實情況手寫的資料的準確率。

## 本次作業已幫大家準備好 `main.py`，可以下載下來做為測試，請同學完成 `my_model.keras` 的訓練。
## 此 `main.py` 不可修改，否則會造成資料格式與模型執行錯誤。
## 請勿上傳老師提供的範例模型，系統會自動偵測並不予計分！

## main.py
```python
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import mnist

# 讀入 MNIST 資料
mnist_load = mnist
(x_train, y_train), (x_test, y_test) = mnist_load.load_data()

# 資料前處理
x_train, x_test = x_train / 255.0, x_test / 255.0

x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

# 輸入模型
model = load_model('my_model.keras')

# 模型測試並列印準確度
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f'Test accuracy: {test_acc:.4f}')
```
    
## 輸入格式

無

## 輸出格式

無

## 格式相關提醒

#### - 請參考本週與上週課程範例程式碼及簡報，作業僅需依照個人程式碼訓練 `my_model.keras` 模型，其餘程式已包含在提供的 `main.py` 中。
#### - MNIST 資料集輸入格式與前處理請參考 `main.py` 作法。
#### - 本題無圖片輸出。
#### - 輸出準確度即為得分，例：準確度 100% 即為 100 分、準確度 96% 即為 96 分，以此類推。

## Hint

#### - 本次作業是要讓同學們對於圖像辨識有初步認識，了解如何建立模型，並進行模型訓練優化。
#### - 雖然完成作業時，請同學們儲存模型權重的檔案名稱為 `my_model.keras`，才可與 `main.py` 結合，但在上傳前請記得改為規定檔名（`學校_學號_姓名.keras`）上傳，才可辨認繳交學生並批改，系統於自動批改時會改回 `my_model.keras`！
#### - 最後還是要再度提醒，在繳交作業前一定要再三檢查，檔案名稱的格式有沒有打對，程式也要測試輸出格式是否與範例完全一致喔！
#### - 本題由於 `main.py` 不可更動，所以不會有輸出格式不符的問題，但請務必確保 `my_model.keras` 訓練過程中 MNIST 資料集格式與 `main.py` 格式相同，否則就會無得分！
#### - 若模型無法載入執行、不符合題目規定或無法執行者則為 0 分。
#### - 更多模型訓練的 hint 請見本週課程簡報。