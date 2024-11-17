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