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