#!/usr/bin/env python
# -*- coding:utf-8 -*-  
__author__ = 'IT小叮当'
__time__ = '2020-09-23 10:03'

# -*- coding: utf-8 -*-
import numpy as np
np.random.seed(2020)  # for reproducibility
import matplotlib.pyplot as plt # 可视化模块
#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

def getData():
    # 创建数据
    # create some data
    X = np.linspace(0, 1, 200)
    Y = -(X-0.5)**2 + np.random.normal(0, 0.05, (200, ))
    return X,Y

# B = [0,1]
def drawLine(Y,B = 0.9):
    plt.title('指数加权平均线，B = {}'.format(B))
    # 超参数 B = 0.9, y = 0
    y = 0
    newY = []
    for thet in Y:
        y = B * y + (1 - B) * thet
        newY.append(y.copy())
    return newY
X, Y = getData()
# plot data 绘制散点图
plt.scatter(X, Y,s = 15)

# 绘制【指数加权平均线】, B 值越大，则越平滑,为 0.9 时，为10天平均，
newY = drawLine(Y,B = 0.5)
newY1 = drawLine(Y,B=0.9)
plt.plot(X, newY, c = 'r', linewidth = '2')
plt.plot(X, newY1, c = 'green', linewidth = '2')
plt.show()
