import numpy as np
import cv2 as cv
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.window.geometry("400x200")

        self.numpy_button = Button(window, text="Numpy Version", command=self.print_numpy_version)
        self.tk_button = Button(window, text="Tkinter Version", command=self.print_tk_version)
        self.cv_button = Button(window, text="OpenCV Version", command=self.print_cv_version)
        self.pil_button = Button(window, text="Pillow Version", command=self.print_pil_version)

        self.numpy_button.pack()
        self.tk_button.pack()
        self.cv_button.pack()
        self.pil_button.pack()

        self.window.mainloop()

    def print_numpy_version(self):
        self.numpy_button.configure(text=f'numpy version is {np.__version__}')
        print(np.__version__)

    def print_cv_version(self):
        self.cv_button.configure(text=f'opencv version is {cv.__version__}')
        print(cv.__version__)

    def print_tk_version(self):
        self.tk_button.configure(text=f'tkinter version is {tk.TkVersion}')
        print(tk.TkVersion)

    def print_pil_version(self):
        self.pil_button.configure(text=f'Pillow version is {Image.__version__}')
        print(Image.__version__)


if __name__ == '__main__':
    root = Tk()
    app = App(root, "Example App")
