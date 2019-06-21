import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_data(file_name):
    # 1. 用pandas读取csv
    data = pd.read_csv(file_name)
    
    # 2. 构造X列表和Y列表
    X_parameter = []
    Y_parameter = []
    for single_square_feet,single_price_value in zip(data['YearsExperience'],data['Salary']):
        X_parameter.append(float(single_square_feet))
        Y_parameter.append(float(single_price_value))

    return X_parameter,Y_parameter


x,y = get_data('./Salary_Data.csv')

print(x)
# coef 为系数，poly_fit 拟合函数
coef1 = np.polyfit(x,y, 1)
poly_fit1 = np.poly1d(coef1)
plt.plot(x, poly_fit1(x), 'g',label="1")
print(poly_fit1)

coef2 = np.polyfit(x,y, 2)
poly_fit2 = np.poly1d(coef2)
plt.plot(x, poly_fit2(x), 'b',label="2")
print(poly_fit2)

coef3 = np.polyfit(x,y, 3)
poly_fit3 = np.poly1d(coef3)
plt.plot(x, poly_fit3(x), 'y',label="3")
print(poly_fit3)

coef4 = np.polyfit(x,y, 4)
poly_fit4 = np.poly1d(coef4)
plt.plot(x, poly_fit4(x), 'k',label="4")
print(poly_fit4)

coef5 = np.polyfit(x,y, 5)
poly_fit5 = np.poly1d(coef5)
plt.plot(x, poly_fit5(x), 'r:',label="5")
print(poly_fit5)

plt.scatter(x, y, color='black')
plt.legend(loc=2)
plt.show()
