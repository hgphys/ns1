"""
辺データを読込と有向グラフの定義
隣接行列を取得するプログラム
"""
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# csvファイルを読み込む
df = pd.read_csv("edges/edges2.csv")

# 有向グラフを作成する
G = nx.DiGraph()
G.add_edges_from(df.values)

# グラフを可視化する
nx.draw(G, with_labels=True)
plt.show()

# 隣接行列を取得
adjacency_matrix = nx.to_numpy_matrix(G)

print(adjacency_matrix)