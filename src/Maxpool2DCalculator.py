import math
import re
from tkinter import messagebox
from tkinter import ttk
from src.Common import entrySelectAllHandler

class Maxpool2DCalculator:
    def __init__(self, window):
        self.windowLabel = "2D Maxpooling"
        window.title(self.windowLabel)

        self.window = ttk.Frame(window)
        ttk.Label(window, text="2D Maxpooling Layer", font=("courier", 15, "bold")).pack()
        self.window.pack()

        self.__add_labels__()
        self.__add_input_fields__()

    def __add_labels__(self):
        pass
    def __add_input_fields__(self):
        pass