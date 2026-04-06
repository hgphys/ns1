"""
受講生の友人関係ネットワークと次数分布の可視化
平均次数と最大次数、その頂点を求める
"""
import networkx as nx
import matplotlib.pyplot as plt

# 辺データの入力によるグラフの定義
G = nx.read_edgelist('edges/edges.txt', create_using=nx.Graph)

# グラフを描画
pos = nx.spring_layout(G)
plt.figure(figsize=(5, 5))
nx.draw(G, pos, node_color='lightblue', node_size=500)
plt.show()

# 次数の計算
degree_sequence = [d for n, d in G.degree()]

# 次数分布を可視化
plt.hist(degree_sequence, bins=max(degree_sequence))
plt.xlabel('Degree $k$')
plt.ylabel('Frequency $N_k=N*p(k)$')
plt.show()

# 平均次数の計算
avg_degree = sum(degree_sequence) / len(degree_sequence)

# 結果の出力
print("平均次数：", round(avg_degree,2))

# 各頂点の次数を取得
degree_dict = dict(G.degree())

# 最大次数を取得
max_degree = max(degree_dict.values())

# 最大次数を持つノードを取得
max_degree_nodes = [node for node, degree in degree_dict.items() if degree == max_degree]

# 最大次数を持つ頂点の名前を表示
for node in max_degree_nodes:
    print(f"次数が最大の頂点は {node} で、次数は {max_degree} です。")