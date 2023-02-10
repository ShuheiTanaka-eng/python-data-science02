import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("13TOKYO.CSV",
    header=None, encoding="Shift_jis")
pd.set_option('display.unicode.east_asian_width', True)

#住所から郵便番号を検索（部分一致）
address = "西新宿"
results = df[df[8].str.contains(address)]
print(results[[2,6,7,8]])
