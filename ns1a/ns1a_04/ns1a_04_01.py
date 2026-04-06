"""
グラフの定義（辺の入力）、平均最短経路長と平均クラスタ係数の計算
以下のコードは誤りを含みます。
"""

import networkx as nx
import matplotlib.pyplot as plt

# グラフを作成する
edges = [(1, 3), (2, 3)]
G = nx.Graph()
G.add_edges_from(edges)

# グラフを可視化する
nx.draw(G, with_labels=True)
plt.show()

# 平均最短経路長と平均クラスタ係数の計算
spl = nx.average_shortest_path_length(G)
cc = nx.average_clustering(G)

# 結果の出力
print("平均最短経路長：", round(spl,3))
print("平均クラスタ係数：", round(cc,3))