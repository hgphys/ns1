"""
グラフを定義して隣接行列を取得、隣接行列の３乗を計算する
以下のコードは未完成です
"""
import pandas as pd
import networkx as nx
import numpy as np

# csvファイルを読み込む
df = pd.read_csv("edges/edges3.csv")

# 無向グラフを作成する
G = nx.Graph()
G.add_edges_from(df.values)

# 隣接行列を取得
adjacency_matrix = nx.to_numpy_matrix(G)

print(adjacency_matrix)

# 隣接行列の3乗を計算
adjacency_matrix_cubed = # ここに隣接行列の３乗を定義する

# 対角成分の和を計算
diagonal_sum = np.trace(adjacency_matrix_cubed)

print("Number of triangles:", diagonal_sum // 6)
