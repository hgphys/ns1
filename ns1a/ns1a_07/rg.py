"""
人工ネットワークを作成するモジュール
"""

import networkx as nx
import random

# 次数保存ランダム化
def generate_degree_preserving_random_graph(G):
    H = G.copy()
    # ネットワークの次数情報を取得
    degrees = dict(H.degree())
    
    # 次数順にソートしたノードリストを作成
    sorted_nodes = sorted(H.nodes(), key=lambda x: degrees[x], reverse=True)
    
    # 次数保存ランダム化したグラフを生成するための空のグラフを作成
    random_graph = nx.Graph()
    
    # ノードごとに処理
    for node in sorted_nodes:
        # ノードの次数
        degree = degrees[node]
        
        # ノードの隣接ノードを取得
        neighbors = list(H.neighbors(node))
        
        # ランダムに選ぶ隣接ノードの数
        num_random_neighbors = degree
        
        # ランダムに選ぶ隣接ノードの数がノードの次数を超えないように制限
        if num_random_neighbors > len(neighbors):
            num_random_neighbors = len(neighbors)
        
        # ランダムに選ぶ隣接ノードを抽出
        random_neighbors = random.sample(neighbors, num_random_neighbors)
        
        # ランダムに選んだ隣接ノードとのエッジを追加
        for neighbor in random_neighbors:
            random_graph.add_edge(node, neighbor)
            
            # 選ばれた隣接ノードをグラフから削除
            H.remove_edge(node, neighbor)
    
    return random_graph

#  完全なランダム化（頂点数とリンク数のみ保存）　エルデシュ・レニィ・ネットワークの生成
def erdos_renyi_network(G):
    node_count = G.number_of_nodes()
    edge_count = G.number_of_edges()
    graph = nx.gnm_random_graph(node_count, edge_count)
    return graph