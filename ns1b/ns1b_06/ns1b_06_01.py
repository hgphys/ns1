"""
名古屋の鉄道路線ネットワークを可視化するためのプログラム
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# データの読み込み
df_join = pd.read_csv('data/join20230327.csv') # 接続データ
df_line = pd.read_csv('data/line20230327free.csv') # 路線データ
df_station = pd.read_csv('data/station20230327free.csv') # 駅データ

# 駅の住所に名古屋が含まれる路線名の集合を作成
nodes_df = # ここに正しく抽出できるように記載する
set_nagoya_line = set(nodes_df['line_cd'])
                      
# グラフの定義に利用する名古屋周辺のの接続
edges_df = df_join[df_join["line_cd"].isin(set_nagoya_line)]

# グラフの定義
G = nx.from_pandas_edgelist(edges_df, source='station_cd1', target='station_cd2')

# 頂点数の出力
print("頂点数：", G.number_of_nodes())

# グラフの可視化
plt.figure(figsize=(6, 6))

# 地理座標の読み込み
node_positions = {row['station_cd']: (row['lon'], row['lat']) for _, row in df_station.iterrows()}

nx.draw_networkx(G, pos=node_positions, with_labels=False,
                 node_color='red', node_size = 3, edge_color='gray')
plt.axis('off')
plt.show()