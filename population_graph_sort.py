import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

#CSVファイルを読み込む
df = pd.read_csv("FEH_00200524_210412225130.csv",
    encoding="Shift_jis", index_col="全国・都道府県")

#2019年の各都道府県の人口データを数値化する
df = df.drop("全国", axis=0)
df["2019年"] = pd.to_numeric(df["2019年"].str.replace(",", ""))

#人口が多い順に並べ替える
df = df.sort_values("2019年", ascending=False)

#2019年の人口データをグラフ化して表示する
df["2019年"].plot.bar(figsize=(10,6))
plt.show()
