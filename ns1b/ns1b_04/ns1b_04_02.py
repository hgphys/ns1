"""
有向グラフの代表的な中心性求めるプログラム
応用例：消防署の最適な配置
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# 隣接行列（距離行列）の定義
adjacency_matrix = np.array([[0, 2, 4, 3, 0, 0, 0, 0],
                             [2, 0, 0, 0, 0, 5, 0, 0],
                             [4, 0, 0, 0, 0, 1, 0, 0],
                             [3, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 3, 2, 0],
                             [0, 5, 1, 0, 3, 0, 0, 0],
                             [0, 0, 0, 0, 2, 0, 0, 4],
                             [0, 0, 0, 0, 0, 0, 4, 0]])


# 隣接行列を有向グラフに変換
G = nx.convert_matrix.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)

# 中心性の計算
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G, distance='weight')
betweenness_centrality = nx.betweenness_centrality(G, weight='weight')
eigenvector_centrality = nx.eigenvector_centrality(G, weight='weight')

# ノードの色を中心性の値の大きさでグラデーションさせる
node_colors = [degree_centrality[node] for node in G.nodes()]

# エッジの太さを重みとして取得
edge_weights = nx.get_edge_attributes(G, 'weight').values()

# ネットワークの可視化
pos = nx.spring_layout(G)  # ノードの位置を算出

plt.figure(figsize=(5, 5))
nx.draw(G, pos, with_labels=True, node_size=500, node_color=node_colors, cmap='Greens', font_size=10, font_weight='bold', width=list(edge_weights), edge_color='gray', arrows=True)
plt.show()
