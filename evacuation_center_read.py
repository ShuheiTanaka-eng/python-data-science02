import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("130001_evacuation_center.csv")
pd.set_option('display.unicode.east_asian_width', True)

#データ件数を出力
print("データ件数：", len(df))

#全データを出力
print(df)
