"""
回答データと受講生リストを読み込み
メールアドレスを元に結合したもの出力するプログラム
以下のコードは未完成です。
"""

import pandas as pd

# 回答データの読込
df1 = pd.read_csv('data/data.csv')
print('++++回答データの読込結果の出力++++')
print(df1.head())

# 受講生リストの読込
df2 = pd.read_csv('data/受講生リスト（２０２３）.csv')
print('++++受講生リストの読込結果の出力++++')
print(df2.head())

# メールアドレスで結合
df_merged = pd.merge(df1,df2, on = "メールアドレス")

# 列名の修正
df_merged = df_merged.rename(columns={'あなたの名前（金沢　太郎）': '回答者名',
                                     'あなたの友人に全てチェックを入れてください。': '友人リスト',
                                     '氏名':'受講者名'})
# 列の抽出
df_merged = df_merged[["メールアドレス","回答者名","受講者名","友人リスト"]]

# 結合したものをCSVファイルとして出力
df_merged.to_csv('data/data_merged.csv', index=False)

# 出力結果の確認
df_merged = pd.read_csv('data/data_merged.csv')
print('++++結合した結果の出力++++')
print(df_merged.head())