from scipy import sparse
import numpy as np
import matplotlib.pyplot as plt
# 在-10和10之间生成一个数列，共100个数
x = np.linspace(-10, 10, 100)
# 用正弦函数创建第二个数组
y = np.sin(x)
# plot函数绘制一个数组关于另一个数组的折线图
plt.plot(x, y, marker="x")
# 此代码实在jupyter上面实现的
plt.show()