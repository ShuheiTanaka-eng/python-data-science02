import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("13TOKYO.CSV",
    header=None, encoding="Shift_jis")
pd.set_option('display.unicode.east_asian_width', True)

#郵便番号から住所を検索
code = 1600023
results = df[df[2] == code]
print(results[[2,6,7,8]])
