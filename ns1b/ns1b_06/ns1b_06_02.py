"""
鉄道路線ネットワーク最大連結成分に対して
各種ネットワーク中心性を計算するプログラム
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# データの読み込み
df_join = pd.read_csv('data/join20230327.csv') # 接続データ
df_line = pd.read_csv('data/line20230327free.csv') # 路線データ
df_station = pd.read_csv('data/station20230327free.csv') # 駅データ

# 駅の住所に名古屋が含まれる路線名の集合を作成
nodes_df =  # ここに正しく抽出できるように記載する
set_nagoya_line = set(nodes_df['line_cd'])

# グラフの定義に利用する名古屋周辺のの接続
edges_df = df_join[df_join["line_cd"].isin(set_nagoya_line)]

# グラフの定義
G = nx.from_pandas_edgelist(df_join, source='station_cd1', target='station_cd2')

# ノード名の変更（駅グループコードを利用）
for _, row in nodes_df.iterrows():
    original_name = row['station_cd']
    new_name = row['station_g_cd']
    G = nx.relabel_nodes(G, {original_name: new_name})

# 最大連結成分の抽出
largest_component = max(nx.connected_components(G), key=len)

# 最大連結成分のノードとエッジのみを取得
G_lc = G.subgraph(largest_component)

# ノードの中心性計算
degree_centrality = nx.degree_centrality(G_lc)
closeness_centrality = nx.closeness_centrality(G_lc)
betweenness_centrality = nx.betweenness_centrality(G_lc)

# ノード情報に中心性を追加
nodes_df = nodes_df[['station_g_cd','station_name']].drop_duplicates()

nodes_df['Degree Centrality'] = nodes_df['station_g_cd'].map(degree_centrality)
nodes_df['Closeness Centrality'] = nodes_df['station_g_cd'].map(closeness_centrality)
nodes_df['Betweenness Centrality'] = nodes_df['station_g_cd'].map(betweenness_centrality)

# 中心性が計算されていないノードはNaNにする
nodes_df.fillna('', inplace=True)

# ノード情報をCSVファイルとして出力
nodes_df.to_csv('output.csv', index=False)