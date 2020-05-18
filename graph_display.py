import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D



sns.set_style("darkgrid")

# グラフの枠
fig = plt.figure()
ax = Axes3D(fig)

# 軸のラベル
ax.set_xlabel("r")
ax.set_ylabel("g")
ax.set_zlabel("b")

# .plotで描画
df = pd.read_csv('learned_colors_myfavorites.csv')
green = df[df['y'] == 1]
not_green = df[df['y'] == 0]
ax.plot(green['red'], green['green'], green['blue'], marker="o", linestyle='None', color='green')
ax.plot(not_green['red'], not_green['green'], not_green['blue'], marker="o", linestyle='None', color='red')
# グラフ表示
plt.show()
