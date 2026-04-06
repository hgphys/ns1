"""
カリフォルニアの道路交通ネットワークの分析
https://snap.stanford.edu/data/roadNet-CA.html
"""
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# 辺データの入力によるグラフの定義
G = nx.read_edgelist('data03/edges03.txt', delimiter=',',create_using=nx.Graph)

# 次数分布の計算
degrees = [G.degree(node) for node in G.nodes()]

# 次数分布の可視化
plt.hist(degrees, bins=10, alpha=0.5)
plt.xlabel('Degree $k$')
plt.ylabel('Frequency $N_k=N*p(k)$')
plt.yscale('log')  # 縦軸を対数スケールに設定
plt.title('California road network')
plt.show()

# 頂点リストの作成
node_data = [{'ID': node} for node in G.nodes()]

# 頂点リストをDataFrameに変換
df = pd.DataFrame(node_data)

# 最大連結成分の抽出
largest_component = max(nx.connected_components(G), key=len)

# 最大連結成分か否かの列を追加
df['LC'] = df['ID'].apply(lambda x: x in largest_component)

# 次数の計算と列の追加
df['Degree'] = df['ID'].apply(lambda x: G.degree(x))

# クラスタ係数の計算と列の追加
df['CC'] = df['ID'].apply(lambda x: nx.clustering(G, x))

# 頂点データの出力
df.to_csv('data03/output03.csv', index=False)