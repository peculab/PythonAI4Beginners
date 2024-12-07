from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

def Select_feature(df):
  x = df[['單價(萬元/坪)', '總面積(坪)', '主建物佔比', '屋齡', '樓別', '樓高', '車位總價(萬元)', '有無電梯', '有無管理組織']]
  # 填補缺失值
  # x.fillna(x.mean(), inplace=True)
  x.loc[:, :] = x.fillna(x.mean())

  # 特徵縮放
  scaler = StandardScaler()
  x_scaled = scaler.fit_transform(x)
  return x_scaled

def Training(x_train, y_train):
  # 超參數調優範例：使用嶺迴歸
  param_grid = {'alpha': [0.1, 1.0, 10.0, 100.0]}  # 可調整的參數
  ridge = Ridge()
  grid_search = GridSearchCV(ridge, param_grid, cv=5, scoring='neg_mean_squared_error')
  grid_search.fit(x_train, y_train)

  # 獲取最佳模型
  best_model = grid_search.best_estimator_

  return best_model