"""
グラフの定義（辺の入力）、密度の計算
以下のコードは誤りを含みます。
"""

import networkx as nx
import matplotlib.pyplot as plt

# グラフを作成する
edges = [(1, 2), (3, 4)]
G = nx.Graph()
G.add_edges_from(edges)

# グラフを可視化する
nx.draw(G, with_labels=True)
plt.show()

# 密度を計算する
density = nx.density(G)
print("グラフの密度は：", round(density,3))