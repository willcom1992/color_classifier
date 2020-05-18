import cv2
import numpy as np
import pandas as pd


# 単色画像を作る関数（https://qiita.com/yukisn0w/items/28a64f570cd519b2f04e）より
def create_color(color, size):
    r = color[0] * np.ones((size[1], size[0], 1), dtype=np.uint8)
    g = color[1] * np.ones((size[1], size[0], 1), dtype=np.uint8)
    b = color[2] * np.ones((size[1], size[0], 1), dtype=np.uint8)
    return np.concatenate([r, g, b], axis=2)


created_rgb_lst = []  # 作った画像のrgbの各値を格納するリスト
for r in range(0, 256, 20):  # 20飛ばしで値を変化
    for g in range(0, 256, 20):
        for b in range(0, 256, 20):
            color = [r, g, b]  # [r,g,b]
            size = [400, 400]  # 画像のサイズ
            img = create_color(color, size)  # 画像を作成
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # cv2で読み込めるようにrgbをbgrに変換
            created = cv2.imwrite(f'colors/{r}_{g}_{b}.png', img)  # 名前を付けて、画像をcolorsフォルダに保存
            created_rgb_lst.append({'red': r, 'green': g, 'blue': b})  # 保存した画像のrgbの各値をリストに追加

df = pd.DataFrame(created_rgb_lst)  # リストをデータフレームに変換
print(df.info())  # データフレームの情報表示
df.to_csv('created_colors.csv')  # データをcsvに保存
