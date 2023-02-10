import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

#CSVファイルを読み込む
df = pd.read_csv("FEH_00200524_210412225130.csv",
    encoding="Shift_jis", index_col="全国・都道府県")

#2018年と2019年の各都道府県の人口データを数値化する
df = df.drop("全国", axis=0)
df["2018年"] = pd.to_numeric(df["2018年"].str.replace(",", ""))
df["2019年"] = pd.to_numeric(df["2019年"].str.replace(",", ""))

#2つの列データの差を新しい列として作り、ソートする
df["人口増減"] = df["2019年"] - df["2018年"]
df = df.sort_values("人口増減", ascending=False)

#人口増減データをグラフ化して表示する
df["人口増減"].plot.bar(figsize=(10,6))
plt.show()

