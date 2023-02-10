import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("FEH_00200524_210412225130.csv",
    encoding="Shift_jis")
pd.set_option('display.unicode.east_asian_width', True)

#データ件数を出力
print("データ件数：", len(df))

#全データを出力
print(df)
