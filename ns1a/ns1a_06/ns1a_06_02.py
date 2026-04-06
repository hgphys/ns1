"""
政治家関係ネットワークの分析
https://networkrepository.com/fb-pages-politician.php
"""
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# 頂点データの入力
df_nodes = pd.read_csv('data02/nodes02.csv')

# 辺データの入力によるグラフの定義
G = nx.read_edgelist('data02/edges02.csv', delimiter=',',create_using=nx.Graph)

# 次数分布の計算
degrees = [G.degree(node) for node in G.nodes()]

# 次数分布の可視化
plt.hist(degrees, bins=10, alpha=0.5)
plt.xlabel('Degree $k$')
plt.ylabel('Frequency $N_k=N*p(k)$')
plt.yscale('log')  # 縦軸を対数スケールに設定
plt.title('FB-Pages-Politician')
plt.show()


# 最大連結成分の抽出
largest_component = max(nx.connected_components(G), key=len)

# 最大連結成分か否かの列を追加
df_nodes['LC'] = df_nodes['new_id'].apply(lambda x: str(x) in largest_component)

# 次数の計算と列の追加
df_nodes['Degree'] = df_nodes['new_id'].apply(lambda x: G.degree(str(x)))

# クラスタ係数の計算と列の追加
df_nodes['CC'] = df_nodes['new_id'].apply(lambda x: nx.clustering(G, str(x)))

# 頂点データの出力
df_nodes.to_csv('data02/output02.csv', index=False)

# 平均最短経路長の計算
spl = nx.average_shortest_path_length(G)

# 結果の出力
print("平均最短経路長：", round(spl,3))