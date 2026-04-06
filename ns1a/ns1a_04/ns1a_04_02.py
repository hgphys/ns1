"""
辺データを読込とグラフの定義、可視化、
平均最短経路長と平均クラスタ係数を計算するプログラム
以下のコードは誤りを含みます。
"""
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# エッジリストの読み込み
df = pd.read_csv('ここに正しいファイルパスを入力する')

# ネットワークの生成
G = nx.from_pandas_edgelist(df, 'source', 'target')

# グラフを可視化する
nx.draw(G, with_labels=True)
plt.show()

# 平均最短経路長と平均クラスタ係数の計算
spl = nx.average_shortest_path_length(G)
cc = nx.average_clustering(G)

# 結果の出力
print("平均最短経路長：", round(spl,3))
print("平均クラスタ係数：", round(cc,3))
