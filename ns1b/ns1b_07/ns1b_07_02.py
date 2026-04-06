"""
スケールフリーネットワークの頑強性を評価するプログラム
"""

import networkx as nx
import random
import matplotlib.pyplot as plt

def generate_scale_free_network(num_nodes, num_edges):
    # スケールフリーネットワークの生成
    G = nx.barabasi_albert_graph(num_nodes, num_edges)
    return G

def evaluate_network_robustness(G, selective_removal=False):
    # ノードのランダムな削除または次数の多いノードからの選択的な削除によるネットワークの頑強性評価
    original_size = len(G)
    robustness = []
    
    while G.number_of_nodes() > 0:
        largest_connected_component = max(nx.connected_components(G), key=len)
        largest_component_size = len(largest_connected_component)
        robustness.append(largest_component_size / original_size)

        if selective_removal:
            # 次数の多いノードから選択的に削除
            node_degrees = G.degree()
            sorted_degrees = sorted(node_degrees, key=lambda x: x[1], reverse=True)
            node_to_remove = sorted_degrees[0][0]  # 次数の最も大きいノードを選択
        else:
            # ランダムなノードの削除
            node_to_remove = random.choice(list(G.nodes))

        G.remove_node(node_to_remove)

    return robustness

def plot_robustness(robustness):
    # 頑強性評価の結果をプロット
    plt.plot(range(len(robustness)), robustness)
    plt.xlabel("Number of node removals")
    plt.ylabel("Size of largest connected component")
    plt.title("Network Robustness")
    plt.show()

# ネットワークの生成と頑強性評価の実行
num_nodes = 1000  # ノード数
num_edges = 3  # 各ノードが追加するエッジの数

network = generate_scale_free_network(num_nodes, num_edges)
robustness_random_removal = evaluate_network_robustness(network.copy(), selective_removal=False)
robustness_selective_removal = evaluate_network_robustness(network.copy(), selective_removal=True)

# 頑強性評価結果のプロット
plt.plot(range(len(robustness_random_removal)), robustness_random_removal, label="Random Removal")
plt.plot(range(len(robustness_selective_removal)), robustness_selective_removal, label="Selective Removal")
plt.xlabel("Number of node removals")
plt.ylabel("Size of largest connected component")
plt.title("Scale Free Network Robustness")
plt.legend()
plt.show()
