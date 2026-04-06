"""
グラフの定義（辺の入力）、密度の計算
以下のコードは誤りを含みます。
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# 隣接行列を定義
adjacency_matrix = np.array([[0, 1, 0, 0],
                             [1, 0, 0, 0],
                             [0, 0, 0, 1],
                             [0, 0, 1, 0]])
# 隣接行列の出力
print(adjacency_matrix)

# 隣接行列を用いてグラフを定義する
G = nx.Graph(adjacency_matrix)
G = nx.convert_node_labels_to_integers( G, first_label=1)

# グラフを可視化する
nx.draw(G, with_labels=True)
plt.show()

# 密度を計算する
density = nx.density(G)
print("グラフの密度は：", round(density,3))


