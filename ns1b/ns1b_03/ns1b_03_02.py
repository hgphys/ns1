"""
有向グラフの最大弱連結成分と最大強連結成分の大きさを求めるプログラム
"""

import numpy as np
import pandas as pd
import networkx as nx

# csvファイルを読み込む
df = pd.read_csv("edges/edges02.csv")

# 有向グラフを作成する
G = nx.DiGraph()
G.add_edges_from(df.values)

# 頂点数
print("N=",G.number_of_nodes())

# 最大弱連結成分
gwcc = max(nx.weakly_connected_components(G), key=len)


# 最大強連結成分
gscc = max(nx.strongly_connected_components(G), key=len)