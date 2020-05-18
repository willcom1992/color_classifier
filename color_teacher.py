import tkinter
import tkinter.ttk
from PIL import Image, ImageTk
import pandas as pd


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Mr. 1 or 0    by willcom  ')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # ボタン
        self.like_button = tkinter.ttk.Button(self, text='1')
        self.like_button.grid(row=0, column=1)
        self.like_button.bind('<Button-1>', btn_yes)

        self.hate_button = tkinter.ttk.Button(self, text='0')
        self.hate_button.grid(row=1, column=1)
        self.hate_button.bind('<Button-1>', btn_no)

        # canvas
        self.canvas = tkinter.Canvas(self, width=color_image.width, height=color_image.height)
        self.canvas.grid(row=0, column=0, rowspan=3)

        # 初期画像表示
        self.canvas.photo = ImageTk.PhotoImage(color_image)
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor='nw', image=self.canvas.photo)


df = pd.read_csv('created_colors.csv', index_col=0)
df_sample = df.sample(n=300)  # n = トレーニングする画像数

image_list = []
for row in df_sample.itertuples():
    r, g, b = row[1], row[2], row[3]
    img = Image.open(f'colors/{r}_{g}_{b}.png')
    image_list.append(img)

color_image = image_list[0]
learned_lst = []
counter = 0
csv_name = 'learned_colors_myfavorites.csv'

def btn_yes(event):
    global counter
    learned_lst.append(1)
    counter += 1
    if counter == len(image_list):
        print(counter - 1, 'Classified 1')
        df_sample['y'] = learned_lst
        print(df_sample)
        df_sample.to_csv(csv_name)
        quit()
    color_image = image_list[counter]
    set_image(event, color_image)
    print(counter - 1, 'Classified 1')



def btn_no(event):
    global counter
    learned_lst.append(0)
    counter += 1
    if counter == len(image_list):
        print(counter - 1, 'Classified 0')
        df_sample['y'] = learned_lst
        print(df_sample)
        df_sample.to_csv(csv_name)
        quit()
    color_image = image_list[counter]
    set_image(event, color_image)
    print(counter - 1, 'Classified 0')


def set_image(event, img):
    # canvasの書き換え
    app.canvas.photo = ImageTk.PhotoImage(img)
    app.canvas.itemconfig(app.image_on_canvas, image=app.canvas.photo)


# アプリケーション起動
root = tkinter.Tk()
app = Application(master=root)
app.mainloop()
