import numpy as np

# 配列生成
a = np.array([1, 2, 3, 4, 5])
b = np.arange(0, 10, 2)
c = np.linspace(0, 1, 6)
print("a:", a)
print("b:", b)
print("c:", c)

# 乱数配列
rng = np.random.default_rng(42)
rand_mat = rng.standard_normal((3, 4))
print("\nrand_mat:\n", rand_mat)

# 基本統計
print("\nmean:", rand_mat.mean())
print("std :", rand_mat.std())
print("max :", rand_mat.max())
print("min :", rand_mat.min())

# 行列演算
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
print("\nx @ y:\n", x @ y)
print("x.T:\n", x.T)
print("det(x):", np.linalg.det(x))

# ブロードキャスト
row = np.array([10, 20, 30])
col = np.array([[1], [2], [3]])
print("\nbroadcast result:\n", row + col)

# インデックス・スライス
arr = np.arange(12).reshape(3, 4)
print("\narr:\n", arr)
print("arr[1:, 2:]:\n", arr[1:, 2:])
print("arr[arr > 7]:", arr[arr > 7])
