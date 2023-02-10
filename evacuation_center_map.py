import pandas as pd
import folium

#CSVファイルを読み込む
df = pd.read_csv("130001_evacuation_center.csv")

#緯度経度情報だけ取り出し、リスト化する
evac_center = df[["緯度","経度"]].values

#TOUを中心とする地図を作成する（ズーム倍率=15）
pos = [35.69158, 139.69696]
map = folium.Map(location=pos, zoom_start=15)

#避難所1件1件にマーカーを追加する
for data in evac_center:
    folium.Marker([data[0],data[1]]).add_to(map)

#地図を書き出す
map.save("東京都避難所MAP.html")
