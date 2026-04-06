"""
スケールフリーネットワークと期待される辺データを読み込み、グラフを可視化
その後、次数分布をべき分布としてフィッティングを行うプログラム
"""
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# エッジリストの読み込み
df = pd.read_csv('edges/scale_free_network_edges.csv')

# ネットワークの生成
G = nx.from_pandas_edgelist(df, 'source', 'target')

#頂点数の計算
N = G.number_of_nodes()

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