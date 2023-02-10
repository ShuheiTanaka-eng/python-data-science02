import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("130001_evacuation_center.csv")

#緯度経度情報だけ取り出し、リスト化する
evac_center = df[["緯度","経度"]].values

#取り出したデータを出力
print(evac_center)
