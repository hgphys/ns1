"""
受講生間の友人関係ネットワークのスモールワールド性の検証
"""

import networkx as nx
import matplotlib.pyplot as plt
import rg

# 辺データの入力によるグラフの定義
G = nx.read_edgelist('data01/edges01.txt', create_using=nx.Graph)
G = nx.convert_node_labels_to_integers(G)
N = G.number_of_nodes()
L = G.number_of_edges()

# 次数保存ランダム化
G_rand = rg.generate_degree_preserving_random_graph(G)
N_rand = G_rand.number_of_nodes()
L_rand = G_rand.number_of_edges()

# 完全なランダム化（頂点数とリンク数のみ保存）
G_comp = rg.erdos_renyi_network(G)
N_comp = G_comp.number_of_nodes()
L_comp = G_comp.number_of_edges()


# グラフの可視化
plt.figure(figsize=(12, 4))

# ノードの配置を取得
pos = nx.spring_layout(G)

plt.subplot(131)
nx.draw_networkx(G, pos, with_labels=False, node_color='lightblue', node_size=500)
plt.title('Data N={0}, L={1}'.format(N,L))

plt.subplot(132)
nx.draw_networkx(G_rand, pos, with_labels=False, node_color='lightblue', node_size=500)
plt.title('Degree Preserving Random N={0}, L={1}'.format(N_rand,L_rand))

plt.subplot(133)
nx.draw_networkx(G_comp, pos, with_labels=False, node_color='lightblue', node_size=500)
plt.title('Complete Random N={0}, L={1}'.format(N_comp,L_comp))

plt.tight_layout()
plt.show()


# 最短経路長の計算
shortest_paths = nx.all_pairs_shortest_path_length(G)
shortest_path_lengths = []
for _, paths in shortest_paths:
    shortest_path_lengths.extend(paths.values())

random_shortest_paths = nx.all_pairs_shortest_path_length(G_rand)
random_shortest_path_lengths = []
for _, paths in random_shortest_paths:
    random_shortest_path_lengths.extend(paths.values())
    
comp_shortest_paths = nx.all_pairs_shortest_path_length(G_comp)
comp_shortest_path_lengths = []
for _, paths in comp_shortest_paths:
    comp_shortest_path_lengths.extend(paths.values())

# 最短経路長の分布の可視化
plt.hist(shortest_path_lengths, bins=10, alpha=0.5, label='Data')
plt.hist(random_shortest_path_lengths, bins=10, alpha=0.5, label='Degree Preserving Random')
plt.hist(comp_shortest_path_lengths, bins=10, alpha=0.5, label='Complete Random')
plt.xlabel('Distance $d$')
plt.ylabel('Frequency $L_d=L*p(d)$')
plt.legend()
plt.show()


# 平均クラスタ係数の計算と出力
print("CC (Complete Random):", round(nx.average_clustering(G_comp),3))