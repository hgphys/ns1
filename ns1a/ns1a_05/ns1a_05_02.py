"""
問題１で作成したファイルを読込み
受講者名と友人リストを元に無向グラフを定義
辺データをTXTファイルとして出力する
"""
import pandas as pd
import networkx as nx

# データの読み込み
df_merged = pd.read_csv('data/data_merged.csv')

# 無向グラフの定義
G = nx.Graph()
for i, row in df_merged.iterrows():
    # 回答者名と友人リストを取得
    name = row['受講者名'].split('　')[0]
    friends = row['友人リスト'].split(', ')
    # エッジの追加
    for friend in friends:
        G.add_edge(name, friend.split(' ')[0])

# 自己ループの削除
G.remove_edges_from(nx.selfloop_edges(G))

# 辺データの出力
nx.write_edgelist(G, 'edges/friend_edges.txt', data = False)