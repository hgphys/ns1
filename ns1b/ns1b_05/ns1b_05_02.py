"""
Barabasi-Albertモデルでスケールフリーネットワークを生成するプログラム
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Barabasi-Albertモデルでグラフを生成する関数
n = 500
m = 3
G = nx.barabasi_albert_graph(n, m)

#頂点数の計算
N = G.number_of_nodes()
print("頂点数：",N)

# ネットワークの可視化
plt.figure(figsize=(8, 8))
pos = nx.spring_layout(G, k=0.1, seed=1)
nx.draw_networkx(G, pos, node_size=30, node_color='black', with_labels=False, edge_color='gray', width=0.5)
plt.axis('off')
plt.show()

# 次数列の取得
degree_sequence = [d for n, d in G.degree()]

# 次数分布のヒストグラムの描画
bins = range(N + 1)
hist, bins = np.histogram(degree_sequence, bins=bins)
bin_centers = (bins[:-1] + bins[1:]) / 2
plt.loglog(bin_centers, hist, 'o', label='data')

# べき関数の定義
def power_law(x, a, b):
    return a * np.power(x, -b)

# フィッティングの実行
xdata, ydata = np.unique(degree_sequence, return_counts=True)
popt, pcov = curve_fit(power_law, xdata, ydata)

# フィッティング結果のプロット
plt.loglog(xdata, power_law(xdata, *popt), 'r-', label=f'fit: a={popt[0]:.3f}, b={popt[1]:.3f}')

# ラベルの追加
plt.xlabel('Degree $k$')
plt.ylabel('Frequency $N_k=N*p(k)$')

plt.legend()
plt.show()

# 次数中心性が最も高いノードを特定
degree_centralities = nx.degree_centrality(G)
max_degree_centrality_node = max(degree_centralities, key=degree_centralities.get)
max_degree_centrality = degree_centralities[max_degree_centrality_node]
print("次数中心性が最も高い頂点:", max_degree_centrality_node)
print("次数中心性:", max_degree_centrality)

# 平均クラスタ係数を計算
clustering_coefficient = nx.average_clustering(G)
print("クラスタ係数:", clustering_coefficient)

# 平均最短距離を計算
average_shortest_path_length = nx.average_shortest_path_length(G)
print("平均最短距離:", average_shortest_path_length)