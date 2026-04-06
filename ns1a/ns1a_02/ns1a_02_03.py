"""
辺データの読込と無向グラフの定義、頂点数と辺数の計算
以下のコードは誤りを含みます。
"""
import pandas as pd
import networkx as nx

# csvファイルを読み込む
df = pd.read_csv("edges/edges3.csv")

# 無向グラフを作成する
G = nx.Graph()
G.add_edges_from(df.values)

# 頂点数と辺数を計算する
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

# 結果を出力する
print("辺数:", num_edges)
