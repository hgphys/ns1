"""
無向グラフの最大連結成分の大きさを求めるプログラム
"""

import numpy as np
import pandas as pd
import networkx as nx

# csvファイルを読み込む
df = pd.read_csv("edges/edges01.csv")

# 無向グラフを作成する
G = nx.Graph()
G.add_edges_from(df.values)

# 頂点数
print("N=",G.number_of_nodes())

# 最大連結成分
lcc = max(nx.connected_components(G), key=len)