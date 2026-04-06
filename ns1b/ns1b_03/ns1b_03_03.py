"""
無向グラフの最大連結成分の大きさを求めるプログラム
"""

import numpy as np
import pandas as pd
import networkx as nx

# csvファイルを読み込む
df = pd.read_csv("edges/edges03.csv")

# 無向グラフを作成する
G = nx.Graph()
G.add_edges_from(df.values)

# 頂点数
print("N=",G.number_of_nodes())

# 最大連結成分
lcc1 = max(nx.connected_components(G), key=len)

# 次数が最大の頂点
degrees = G.degree()
max_degree_node = max(degrees, key=lambda x: x[1])[0]

# ノード除去のプログラムをここに記載する


# 除去後の最大連結成分
lcc2 = max(nx.connected_components(G), key=len)
