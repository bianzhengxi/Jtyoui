#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/11/7 10:14
# @Author: Jtyoui@qq.com
from jtyoui.ml import sigmoid, error_rate
import numpy as np

__description__ = """
LR(逻辑回归)算法
"""


def lr_train_bgd(feature, label, max_cycle, alpha):
    """利用梯度下降法训练逻辑回归模型（LR）
    :param feature:特征
    :param label:标签
    :param max_cycle:最大迭代次数
    :param alpha:学习率
    :return:w的权重
    """
    n = np.shape(feature)[1]  # 特征个数
    w = np.random.rand(n).reshape((n, 1))  # 随机初始化权重
    i = 0
    while i <= max_cycle:
        i += 1
        h = sigmoid(np.dot(feature, w))  # 做点乘，计算sigmoid值
        err = label - h  # 误差
        if i % 100 == 0:
            print(f'error rate: {error_rate(h, label)}')
        w += alpha * np.dot(feature.T, err)  # wi+ 1= wi+ α·d 梯度下降进行权重修正

    return w


if __name__ == '__main__':
    data = [[6, 23, 32, 56],
            [6, 22, 59, 19],
            [6, 21, 59, 11],
            [6, 20, 59, 44],
            [6, 19, 59, 24],
            [6, 18, 58, 58],
            [6, 17, 59, 43],
            [6, 16, 59, 18],
            [6, 15, 58, 58],
            [6, 14, 59, 43],
            [6, 13, 59, 17],
            [6, 12, 59, 5],
            [6, 11, 59, 46],
            [6, 10, 59, 29],
            [6, 9, 59, 12],
            [6, 8, 59, 8],
            [6, 7, 59, 50],
            [6, 6, 59, 35],
            [6, 5, 59, 24],
            [6, 4, 59, 32],
            [6, 3, 59, 43],
            [6, 2, 59, 51],
            [6, 1, 59, 45],
            [6, 0, 59, 59],
            [5, 23, 59, 51],
            [5, 22, 59, 57],
            [5, 21, 59, 41],
            [5, 20, 59, 31],
            [5, 19, 59, 6],
            [5, 18, 59, 43],
            [5, 17, 59, 14],
            [5, 16, 58, 57],
            [5, 15, 58, 30],
            [5, 14, 59, 16],
            [5, 13, 59, 54],
            [5, 12, 59, 33],
            [5, 11, 59, 7],
            [5, 10, 59, 43],
            [5, 9, 59, 20],
            [5, 8, 59, 11],
            [5, 7, 59, 30],
            [5, 6, 59, 6],
            [5, 5, 59, 53],
            [5, 4, 59, 45],
            [5, 3, 59, 23],
            [5, 2, 59, 4],
            [5, 1, 59, 50],
            [5, 0, 59, 27],
            [4, 23, 59, 17],
            [4, 22, 59, 2],
            [4, 21, 59, 40],
            [4, 20, 59, 25],
            [4, 19, 59, 7],
            [4, 18, 59, 40],
            [4, 17, 59, 21],
            [4, 16, 59, 3],
            [4, 15, 59, 43],
            [4, 14, 59, 20],
            [4, 13, 59, 5],
            [4, 12, 59, 50],
            [4, 11, 59, 46],
            [4, 10, 59, 31],
            [4, 9, 59, 11],
            [4, 8, 59, 48],
            [4, 7, 59, 22],
            [4, 6, 59, 53],
            [4, 5, 59, 29],
            [4, 4, 59, 21],
            [4, 3, 59, 8],
            [4, 2, 59, 9],
            [4, 1, 59, 3],
            [4, 0, 59, 42],
            [3, 23, 59, 42],
            [3, 22, 59, 5],
            [3, 21, 59, 54],
            [3, 20, 59, 33],
            [3, 19, 59, 1],
            [3, 18, 59, 45],
            [3, 17, 59, 14],
            [3, 16, 59, 50],
            [3, 15, 59, 22],
            [3, 14, 59, 0],
            [3, 13, 59, 43],
            [3, 12, 59, 24],
            [3, 11, 59, 15],
            [3, 10, 59, 50],
            [3, 9, 59, 32],
            [3, 8, 59, 12],
            [3, 7, 59, 56],
            [3, 6, 59, 32],
            [3, 5, 59, 14],
            [3, 4, 59, 18],
            [3, 3, 59, 11],
            [3, 2, 59, 4],
            [3, 1, 59, 49],
            [3, 0, 59, 39],
            [2, 23, 59, 26],
            [2, 22, 59, 12],
            [2, 21, 59, 57],
            [2, 20, 59, 59]]
    answer = [0.4934, 0.6134, 0.6048, 0.5927, 0.611, 0.6123, 0.5752, 0.5963,
              0.6072, 0.4905, 0.5977, 0.5007, 0.599, 0.4112, 0.4881, 0.5942,
              0.6097, 0.5691, 0.6065, 0.6065, 0.6039, 0.6078, 0.606, 0.5878,
              0.611, 0.5376, 0.5401, 0.5121, 0.5464, 0.6037, 0.5825, 0.5749,
              0.6111, 0.5183, 0.6115, 0.5077, 0.4909, 0.5374, 0.3784, 0.153,
              0.5164, 0.5874, 0.5765, 0.5185, 0.6128, 0.6063, 0.546, 0.603,
              0.5809, 0.6048, 0.6021, 0.5899, 0.4329, 0.5794, 0.5884, 0.6168,
              0.5919, 0.5527, 0.5912, 0.5123, 0.4262, 0.53, 0.5092, 0.4041,
              0.4995, 0.5244, 0.6055, 0.6027, 0.5985, 0.6149, 0.602, 0.6195,
              0.6022, 0.6028, 0.6095, 0.6024, 0.6027, 0.5768, 0.5085, 0.582,
              0.5244, 0.5064, 0.5781, 0.5517, 0.6157, 0.4818, 0.4643, 0.541,
              0.6436, 0.5208, 0.6092, 0.6048, 0.5695, 0.6115, 0.619, 0.5241,
              0.6137, 0.6121, 0.5645, 0.4468]
    data = np.array(data, dtype=np.float)
    data[:, 0] = data[:, 0] / 7
    data[:, 1] = data[:, 1] / 24
    data[:, 2] = data[:, 2] / 60
    data[:, 3] = data[:, 3] / 60
    answer = np.array(answer).reshape((-1, 1))
    weight = lr_train_bgd(data, answer, 2000, 0.01)
    print(sigmoid(np.dot(np.array([[1, 1 / 24, 10 / 60, 32 / 60]], dtype=np.float), weight)))
