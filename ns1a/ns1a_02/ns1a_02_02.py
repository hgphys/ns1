"""
辺データを読込と有向グラフの定義、密度の計算
以下のコードは誤りを含みます。
"""
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# csvファイルを読み込む
df = pd.read_csv("edges/edges2.csv")

# 有向グラフを作成する
G = nx.Graph()
G.add_edges_from(df.values)

# グラフを可視化する
nx.draw(G, with_labels=True)
plt.show()

# 密度を計算する
density = nx.density(G)
print("グラフの密度は：", round(density,3))