"""
辺データを読込と有向グラフの定義、可視化、
入次数と出次数の次数分布を作成し、平均次数を計算するプログラム
以下のコードは誤りを含みます。
"""
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# csvファイルを読み込む
df = pd.read_csv("edges/edges2.csv")

# 有向グラフを作成する
G = nx.DiGraph()
G.add_edges_from(df.values)

#頂点数の計算
num_nodes = G.number_of_nodes()

# グラフを可視化する
nx.draw(G, with_labels=True)
plt.show()

# 入次数と出次数の次数分布を計算
in_degree_sequence = sorted([d for n, d in G.in_degree()], reverse=True)
out_degree_sequence = sorted([d for n, d in G.out_degree()], reverse=True)


# グラフを横に並べるためにsubplot関数を使用
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 4))

# 入次数分布を可視化
ax1.hist(in_degree_sequence, bins=max(in_degree_sequence)+1)
ax1.set_xlabel('In-degree $k^{in}$')
ax1.set_ylabel('Frequency $N*p(k^{in})$')
ax1.set_title('In-degree Distribution')

# 出次数分布を可視化
ax2.hist(out_degree_sequence, bins=max(out_degree_sequence)+1)
ax2.set_xlabel('Out-degree $k^{out}$')
ax2.set_ylabel('Frequency $N*p(k^{out})$')
ax2.set_title('Out-degree Distribution')

plt.show()

# 平均入次数と平均出次数を計算して出力
avg_in_degree = sum(in_degree_sequence) / len(in_degree_sequence)
avg_out_degree = sum(out_degree_sequence) / len(out_degree_sequence)
print("平均入次数:", avg_in_degree)
print("平均出次数:", avg_out_degree)
