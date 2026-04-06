"""
グラフの定義（辺の入力）、次数分布の可視化と平均次数の計算
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

# 次数の計算
degree_sequence = [d for n, d in G.degree()]

# 入次数分布を可視化
plt.hist(degree_sequence, bins=max(degree_sequence))
plt.xlabel('Degree $k$')
plt.ylabel('Frequency $N_k=N*p(k)$')
plt.show()


# 平均次数の計算
avg_degree = sum(degree_sequence) / len(degree_sequence)

# 結果の出力
print("平均次数：", avg_degree)