#test01.py

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
#plt.style.use('seaborn-darkgrid')だとseaborn-darkgridというスタイルが存在しないというエラーが出たため書き換えました。
plt.style.use('seaborn-v0_8-darkgrid')


#ここに必要な記述をしましょう

#データ
date = [0.0, 1.0, 2.0]
worktime = [8.0, 9.0, 8.0]
learntime = [1.0, 1.0, 3.0]

#左側の勤務時間のグラフ
plt.subplot(1, 2, 1)
plt.title("「室塚」の直近の3日間の勤務時間", fontname = "MS Gothic")
plt.plot(date, worktime, label = "time(h)")
plt.legend(loc="upper left", prop={"family": "MS Gothic"})

#右側の勉強時間
plt.subplot(1, 2, 2)
plt.plot(date, learntime, label = "time(h)")
plt.title("「室塚」の直近3日間の勉強時間", fontname = "MS Gothic")
plt.legend(loc="upper right", prop={"family": "MS Gothic"})

plt.show()