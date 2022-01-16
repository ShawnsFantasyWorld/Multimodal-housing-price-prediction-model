import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import warnings
# filter warnings
warnings.filterwarnings('ignore')
# 正常显示中文
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
# 正常显示符号
from matplotlib import rcParams
rcParams['axes.unicode_minus']=False

os.chdir('./')

data=pd.read_csv('data_optimized.csv',encoding='gbk')

data['type']=data['type'].astype(str)  #MSSubClass是一个分类变量，所以要把他的数据类型改为‘’str‘’

NAME=data.loc[:,'name']   #ID先提取出来，后面合并表格要用
data=data.drop('name',axis=1)

x=data.loc[:,data.columns!='price']
y=data.loc[:,'price'] 



mean_cols=x.mean()
x=x.fillna(mean_cols)  #填充缺失值
x_dum=pd.get_dummies(x)    #独热编码
x_train,x_test,y_train,y_test = train_test_split(x_dum,y,test_size = 0.3,random_state = 1)

# #--------------------------------------------#
# #--------------------logy--------------------#
# #平滑处理预测值y
# y_log=np.log(y)
# x_train,x_test,y_train_log,y_test_log = train_test_split(x_dum,y_log,test_size = 0.3,random_state = 1)
# #--------------------------------------------#



#------------------------------------------------# 
#---------------------standard-------------------#
#再整理出一组标准化的数据，通过对比可以看出模型的效果有没有提高
x_dum=pd.get_dummies(x)
scale_x=StandardScaler()
x1=scale_x.fit_transform(x_dum)
scale_y=StandardScaler()
y=np.array(y).reshape(-1,1)
y1=scale_y.fit_transform(y)
y1=y1.ravel()
x_train1,x_test1,y_train1,y_test1 = train_test_split(x1,y1,test_size = 0.3,random_state = 1)
#------------------------------------------------# 

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import ExtraTreeRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import BaggingRegressor

from sklearn.metrics import r2_score # R square
# from sklearn.metrics import mean_squared_error


models=[LinearRegression(),KNeighborsRegressor(),SVR(),Ridge(),Lasso(),MLPRegressor(alpha=20),DecisionTreeRegressor(),ExtraTreeRegressor(),XGBRegressor(),RandomForestRegressor(),AdaBoostRegressor(),GradientBoostingRegressor(),BaggingRegressor()]
models_str=['LinearRegression','KNNRegressor','SVR','Ridge','Lasso','MLPRegressor','DecisionTree','ExtraTree','XGBoost','RandomForest','AdaBoost','GradientBoost','Bagging']
score_=[]
score_1=[]

for name,model in zip(models_str,models):
    #--------------------------------------------#
    #-------------------Original-----------------#
    print('开始训练模型：'+name)
    model=model   #建立模型
    model.fit(x_train,y_train)
    print(model.get_params())
    y_pred=model.predict(x_test)  
    score=model.score(x_test,y_test)
    score_.append(str(score)[:5])
    print(name +' 得分:'+str(score))
    #--------------------------------------------#

    # #--------------------------------------------#
    # #--------------------logy--------------------#
    # print('开始训练模型：'+name+' 平滑处理')
    # model=model
    # model.fit(x_train,y_train_log)
    # y_pred=model.predict(x_test)     
    # score=model.score(x_test,y_test_log)
    # score_.append(str(score)[:5])
    # print(name +' 得分:'+str(score))
    # #--------------------------------------------#


# #------------------------------------------------# 
# #---------------------standard-------------------# 
#     print('开始训练模型：'+name+' 标准化处理')
#     model=model
#     model.fit(x_train1,y_train1)
#     y_pred=model.predict(x_test1)
#     ypred_original=scale_y.inverse_transform(y_pred)
#     score=model.score(x_test1,y_test1)
#     score_1.append(str(score)[:5])
#     print(name +' 得分:'+str(score))
# #------------------------------------------------# 
    

    
    
    
    
    
    
    
    
    

    
    # MSE = mean_squared_error(y_test1, y_pred)
    # print(MSE)
    # print(x_test[:5])
    # print(y_pred[:5])
    #R = r2_score(y_test,y_pred)
    #print('R:',R)