"""
金沢学院大学の教員名をスクレイピングするためのプログラム
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# スクレイピング対象のURL
url = ""

# ページのHTMLを取得
response = requests.get(url)
html = response.text

# BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(html, "html.parser")

# データを格納するリストを作成
data = []

# データを抽出してリストに追加
for item in soup.find_all("li", class_="archiveTeacherbox__item"):
    name = item.find("span", class_="archiveTeacherbox__name").text.strip()
    specialty = item.find("span", class_="archiveTeacherbox__senmonsp").text.strip()
    data.append([name, specialty])

# pandasのDataFrameにデータを格納
df = pd.DataFrame(data, columns=["Name", "Specialty"])

# 重複を削除する

print(len(df))

# CSVファイルにデータを書き込む
df.to_csv("data/data.csv", index=False, encoding="utf-8")