import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

#CSVファイルを読み込む
df = pd.read_csv("FEH_00200524_210412225130.csv",
    encoding="Shift_jis", index_col="全国・都道府県")

#カンマを削除して数値データに変換する
df["2019年"] = pd.to_numeric(df["2019年"].str.replace(",", ""))
#2019年の人口データをグラフ化して表示する
df["2019年"].plot.bar()
plt.show()
