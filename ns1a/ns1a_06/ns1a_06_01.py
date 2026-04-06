"""
受講生間の友人関係ネットワークの特徴量（次数、クラスタ係数）を計算
"""

import pandas as pd
import networkx as nx

# 頂点データの入力
df_nodes = pd.read_csv('data01/nodes01.csv')

# 辺データの入力によるグラフの定義
G = nx.read_edgelist('data01/edges01.txt', create_using=nx.Graph)

# 次数の計算と頂点データに列を追加
df_nodes['次数'] = df_nodes['姓'].apply(lambda x: G.degree[x])

# クラスタ係数の計算と頂点データに列を追加
df_nodes['クラスタ係数'] = df_nodes['姓'].apply(lambda x: nx.clustering(G,x))

# 列を追加した頂点データを保存
df_nodes.to_csv('data01/output01.csv', index=False)

print(df_nodes['クラスタ係数'].mean())