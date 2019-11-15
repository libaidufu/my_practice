import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# csv文件必须以逗号分隔
dataset = pd.read_csv('~/github/my_practice/watermelon3a.csv')
# 数据预处理
# X、Y是对列进行切片
X = dataset[['密度','含糖率']]
Y = dataset['好瓜']
# good_melon对行进行切片
good_melon = dataset[dataset['好瓜'] == 1]
bad_melon = dataset[dataset['好瓜'] == 0]
#画图
f1 = plt.figure(1)
plt.title('watermelon_3a')
plt.xlabel('density')
plt.ylabel('radio_sugar')
plt.xlim(0,1)
plt.ylim(0,1)
# 绘制散点图
plt.scatter(bad_melon['密度'],bad_melon['含糖率'],marker='o',color='r',s=100,label='bad')
plt.scatter(good_melon['密度'],good_melon['含糖率'],marker='o',color='g',s=100,label='good')
plt.legend(loc='upper right')
#分割训练集和验证集
X_train,X_test,Y_train,Y_test = model_selection.train_test_split(X,Y,test_size=0.5,random_state=0)
#训练
log_model = LogisticRegression()
log_model.fit(X_train, Y_train)
#验证
Y_pred = log_model.predict(X_test)
#汇总
# metrics.confusion_matrix的输出是一个矩阵，行表示真实的输出
print(metrics.confusion_matrix(Y_test, Y_pred))
print(metrics.classification_report(Y_test, Y_pred))
# 线性模型中.coef_属性表示训练模型的系数向量
# 线性模型中.intercept属性是训练模型的偏置
# print(log_model.coef_)
theta1, theta2 = log_model.coef_[0][0], log_model.coef_[0][1]
X_pred = np.linspace(0,1,100)
line_pred = theta1 + theta2 * X_pred
# 绘制分类的直线
plt.plot(X_pred, line_pred)
plt.show()