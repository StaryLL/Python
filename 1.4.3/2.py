from scipy import sparse
import numpy as np
eye = np.eye(4)# 创建一个二维NumPy数组，对角线为1，其余都为0
print("NumPy array:\n{}".format(eye))
sparse_atrix = sparse.csr_matrix(eye)# 将NumPy数组转换为CSR格式的SciPy稀疏矩阵,只保存非零元素
print("\nScipy sparse CSR matrix:\n{}".format(sparse_atrix))
