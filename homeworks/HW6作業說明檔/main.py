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