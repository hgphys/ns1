"""
無向グラフの代表的な中心性求めるプログラム
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# CSVファイルの読み込み
df = pd.read_csv('edges/edges01.csv')

# エッジデータをリストとして取得
edges = df.values.tolist()

# ネットワークの定義
G = nx.Graph()
G.add_edges_from(edges)

# 中心性指標の計算
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)

# ノードの色を中心性の値の大きさでグラデーションさせる
node_colors = [degree_centrality[node] for node in G.nodes()]

# ネットワークの可視化
pos = nx.spring_layout(G)  # ノードの位置を算出

plt.figure(figsize=(5, 5))
nx.draw(G, pos, with_labels=True, node_size=500, node_color=node_colors, cmap='Blues', font_size=10, font_weight='bold', edge_color='gray')
plt.show()