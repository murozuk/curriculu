#test01.py

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
#plt.style.use('seaborn-darkgrid')だとseaborn-darkgridというスタイルが存在しないというエラーが出たため書き換えました。
plt.style.use('seaborn-v0_8-darkgrid')
import pandas as pd

#ここに必要な記述をしましょう


#データ読み込み
df = pd.read_csv("第４章課題用.csv")

#左側の勤務時間のグラフ
plt.subplot(1, 2, 1)
plt.title("「室塚」の直近の3日間の勤務時間", fontname = "MS Gothic")
plt.plot(df["date"], df["worktime"], label = "time(h)")
plt.legend(loc="upper left", prop={"family": "MS Gothic"})

#右側の勉強時間
plt.subplot(1, 2, 2)
plt.plot(df["date"], df["learntime"], label = "time(h)")
plt.title("「室塚」の直近3日間の勉強時間", fontname = "MS Gothic")
plt.legend(loc="upper right", prop={"family": "MS Gothic"})

plt.savefig("勤務・勉強時間.png", dpi = 300, bbox_inches = "tight")
plt.show()
