#!/usr/bin/python
# coding:utf-8

# 一元回归分析实例：预测工作经验与年薪的关系
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# 从csv文件中读取数据，分别为：X列表和对应的Y列表
def get_data(file_name):
    # 1. 用pandas读取csv
    data = pd.read_csv(file_name)
    
    # 2. 构造X列表和Y列表
    X_parameter = []
    Y_parameter = []
    for single_square_feet,single_price_value in zip(data['YearsExperience'],data['Salary']):
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append(float(single_price_value))
        
    return X_parameter, Y_parameter

# 绘出图像
def show_linear_line(X_parameter,Y_parameter):
    # 1. 构造回归对象
    regr = LinearRegression()
    regr.fit(X_parameter,Y_parameter)
    
    # 2. 绘出已知数据散点图
    plt.scatter(X_parameter,Y_parameter,color = 'blue')
    
    # 3. 绘出预测直线
    plt.plot(X_parameter,regr.predict(X_parameter),color = 'red',linewidth = 4)
    
    #工作经验与年薪的关系
    plt.xlabel('YeasExperience')
    plt.ylabel('Salary')
    plt.show()


X,Y = get_data('./Salary_Data.csv')
show_linear_line(X,Y)
