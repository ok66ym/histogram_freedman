import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Freedman-Disconisの公式を適応して適切なbin数を算出
def freedman_diaconis_bins(data):
    q25, q75 = np.percentile(data, [25, 75])
    iqr = q75 - q25
    h = 2.0 * iqr * len(data) ** (-1.0/3.0)
    bins = int(np.ceil((data.max() - data.min()) / h))
    return bins

# csvファイルを読み込み、1行目と2行目をスキップして、スペース区切りでデータを取得する
#目的のcsvファイルを指定してから，実行する．
data = pd.read_csv("normal1_1.84785_0.735642.csv", delim_whitespace=True, header=None, skiprows=[0, 1], usecols=[1])

# データの準備
data_bins = np.random.normal(size=118003)

# Freedman-Diaconisの公式を使用してビン数を求める
bins = freedman_diaconis_bins(data_bins)
bins = int(bins) # ビン数を整数に変換する
print("Number of bins:", bins) # ビン数を出力する

# ヒストグラムの描画
plt.hist(data.values, bins=bins, alpha=0.5)
plt.xlabel('Value bins:{}'.format(bins))
plt.ylabel('Frequency')
plt.title('normal1 1.84785_0.735642')
plt.xlim(-100, 50)
#plt.ylim(0, 5000)
plt.show()
