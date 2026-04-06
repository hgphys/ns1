"""
有向グラフのPageRankを求めるプログラム
データ：web-edu
https://networkrepository.com/web-edu.php
"""

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# エッジデータを読み込む
G = nx.read_edgelist('edges/web-edu.mtx', delimiter=' ', comments='%', create_using=nx.DiGraph)

# PageRankの計算
pagerank = nx.pagerank(G, alpha=0.5)

# PageRankが最大の頂点とその値を取得
max_node = max(pagerank, key=pagerank.get)
max_value = pagerank[max_node]

# 結果の出力
print("最大の頂点:", max_node)
print("ページランクの値:", max_value)
