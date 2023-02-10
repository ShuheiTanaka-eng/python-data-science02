import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("13TOKYO.CSV",
    header=None, encoding="Shift_jis")

#データ件数を表示
print("データ件数：", len(df))

#項目名の一覧を表示
print("項目名一覧：", df.columns.values)
