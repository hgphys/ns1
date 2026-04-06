"""
Watts-Strogatzモデルに基づくグラフを生成
平均最短経路長と平均クラスタ係数を計算
"""
import networkx as nx
import matplotlib.pyplot as plt

# ノード数と平均次数を設定
n = 20
k = 4
p = 1

# Watts-Strogatzモデルに基づくグラフを作成
G = nx.watts_strogatz_graph(n, k, p=p)

# グラフを描画
pos = nx.circular_layout(G)
plt.figure(figsize=(4, 4))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
plt.title('p={0}'.format(p))
plt.show()

# 平均最短経路長と平均クラスタ係数の計算
spl = nx.average_shortest_path_length(G)
cc = nx.average_clustering(G)

# 結果の出力
print("平均最短経路長：", round(spl,3))
print("平均クラスタ係数：", round(cc,3))