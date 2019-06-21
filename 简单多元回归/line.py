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
    xx = []
    yy = []
    Y_parameter = []
    for single_x1,single_x2,single_y in zip(data['x1'],data['x2'],data['y']):
        X_parameter.append([float(single_x1), float(single_x2)])
        xx.append(float(single_x1))
        yy.append(float(single_x2))
        Y_parameter.append(float(single_y))
        
    return X_parameter, Y_parameter, xx, yy

# 绘出图像
def show_linear_line(X_parameter,Y_parameter,xx,yy):
    #构造回归对象
    regr = linear_model.LinearRegression()
    regr.fit(X_parameter,Y_parameter)
    
    # 不难得到平面的系数、截距
    a, b = regr.coef_, regr.intercept_

    # 画图
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # 画出真实的点
    ax.scatter(xx, yy, Y_parameter)

    plt.show()


X,Y,xx,yy = get_data('./Data.csv')
show_linear_line(X,Y,xx,yy)
