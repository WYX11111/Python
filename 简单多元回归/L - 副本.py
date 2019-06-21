#!/usr/bin/python
# coding:utf-8

import pandas as pd
import numpy as np
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# 从csv文件中读取数据，分别为：X列表和对应的Y列表
def get_data(file_name):
    # 1. 用pandas读取csv
    data = pd.read_csv(file_name)
    
    # 2. 构造X列表和Y列表
    X_parameter = []
    Y_parameter = []
    for single_x1,single_x2,single_x3,single_x4,single_y in zip(data['Consumption'],data['M0'],data['EM'],data['Investment'],data['GDP']):
        X_parameter.append([float(single_x1),float(single_x2),float(single_x3),float(single_x4)])
        Y_parameter.append(float(single_y))
        
    return X_parameter, Y_parameter

#绘图
def draw_linear_line(file_name,a,b):
    data = pd.read_csv(file_name)

    X = []
    Y = []
    Z = []
    for single_x1,single_x2,single_x3,single_x4,single_y in zip(data['Consumption'],data['M0'],data['EM'],data['Investment'],data['GDP']):
        X.append(float(single_x1)*a[0]+float(single_x2)*a[1])
        Y.append(float(single_x3)*a[2]+float(single_x4)*a[3]-b)
        Z.append(float(single_y))
    # 画图
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # 画出真实的点
    ax.scatter(X, Y, Z)

    plt.show()


# 方程
def show_linear_line(X_parameter,Y_parameter):
    #构造回归对象
    regr = linear_model.LinearRegression()
    regr.fit(X_parameter,Y_parameter)
    
    # 不难得到系数、截距
    a, b = regr.coef_, regr.intercept_
    print(a,b)
    print("y= %.2f x1 + %.2f x2 + %.2f x3 + %.2f x4 %.2f"%(a[0],a[1],a[2],a[3],b))
    #draw_linear_line('./yeardata.csv',a,b)
    

X,Y = get_data('./yeardata.csv')
show_linear_line(X,Y)
