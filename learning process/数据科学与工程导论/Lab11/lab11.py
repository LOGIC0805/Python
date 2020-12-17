import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from numpy import sqrt

datas = pd.read_csv('bike.csv')
datas = datas.drop(columns = 'id')
datas = datas.loc[datas['city'] == 1].drop(columns = 'city')
datas['hour'] = datas['hour'].apply(lambda x : 1 if (x >= 6 and x <= 18) else 0)
y = datas['y'].to_numpy()
x = datas.drop(columns = 'y').to_numpy()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, shuffle = True)

min_max_scaler = MinMaxScaler()
x_train = min_max_scaler.fit_transform(x_train)
x_test = min_max_scaler.fit_transform(x_test)
y_train = min_max_scaler.fit_transform(y_train.reshape(-1, 1))
y_test = min_max_scaler.fit_transform(y_test.reshape(-1, 1))

model = LinearRegression()
model.fit(x_train, y_train)
y_predict = model.predict(x_test)
rmse = sqrt(mean_squared_error(y_test, y_predict))
print(y_predict)
print(rmse)