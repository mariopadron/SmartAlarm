import tkinter as tk
from time import time, ctime

from PIL import Image, ImageTk


class Screen():

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("{0}x{1}+0+0".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
        self.window.configure(background='white')
        self.width = self.window.winfo_width()
        self.height = self.window.winfo_height()

        self.set_bg('Images/Background/background.png')
        # self.window.
        template = tk.Frame()
        gm = tk.Label(
            text="Good Morning",
            font="Calibri,20",
            fg='white',
            bg='black',
            master=template
        )
        gm.pack()

        template.pack()
        clock = Clock(self.width, self.height,self.canvas)
        clock.draw()
        self.canvas.pack()
        



        # image = Image.open('Images/All images.png')
        # photo = ImageTk.PhotoImage(image)
        #
        # frame_simbol = tk.Label(self.window, width=600, height=400)
        # frame_simbol.pack()
        # frame_simbol.place(anchor='center', relx=0.5, rely=0.5)
        #
        # label = tk.Label(frame_simbol, image=photo)
        # label.pack()

        self.window.mainloop()

    def set_bg(self, name):
        self.bg = tk.PhotoImage(file=name)
        self.bg.zoom(self.width, self.height)

        # # Create a label
        # label1 = tk.Label(self.window, image=self.bg)
        # label1.place(x=-150, y=-100, relwidth=1, relheight=1)

        #
        # resized_image = self.bg.resize((self.width, self.height), Image.ANTIALIAS)
        # new_image = ImageTk.PhotoImage(resized_image)
        # label1 = tk.Label(self.window, self.bg)
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height, bg='white')
        self.canvas.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, anchor='nw', image=self.bg)

    def __add__(self, other):
        pass


class Clock:
    def __init__(self, width, height,canvas):
        self.canvas=canvas
        self.days = {
            'Mon': 'Monday',
            'Tue': 'Tuesday',
            'Wed': 'Wednesday',
            'Thu': 'Thursday',
            'Fri': 'Friday',
            'Sat': 'Saturday',
            'Sun': 'Sunday'
        }
        self.update_time()
        self.update_date()
        self.size = [width, height]

    def update_time(self):
        self.t0 = round(time(), 0)
        self.chars = ctime(self.t0).split(' ')
        self.time = self.chars[3][:5]

    def update_date(self):
        self.day = [self.days[self.chars[0]], self.chars[2]]
        self.month = self.chars[1]
        self.year = self.chars[-1]

    def check(self):
        if (self.t0 - time()) < 60:
            self.update_time()

        if (self.t0 - time()) < 60 * 60 * 24:
            self.update_date()

    def draw(self):

        label = tk.Label(master=self.canvas, text=self.time, font=('Times New Roman', 30), bg='grey')
        label.pack()



class Gadget():
    def __init__(self):
        pass
