import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score

datas = pd.read_csv('fraudulent.csv')
# 保留至少有17个完整数据的行
datas = datas.dropna(thresh = 17)
# 使用众数填充缺失值
for col in datas.columns:
    datas[col] = datas[col].fillna(datas[col].mode().values[0])

y = datas['y'].values
x = datas.drop(columns = 'y').values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

# 使用决策树模型
for k in range(3, 18):
    model = DecisionTreeClassifier(max_depth = k)
    scores = cross_val_score(model, x_train, y_train, cv = 4)
    # print(k, scores.mean())
    model.fit(x_train,y_train)
    y_pre = model.predict(x_test)
    f1 = f1_score(y_test,y_pre)
    print(k, scores.mean(), f1)
    
# 选择 max_depth = 13
# model = DecisionTreeClassifier(max_depth = 13)
# model.fit(x_train,y_train)
# y_pre = model.predict(x_test)
# f1 = f1_score(y_test,y_pre)
# print(f1)
