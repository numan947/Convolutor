import math
import re
from tkinter import messagebox
from tkinter import ttk
from Common import entrySelectAllHandler


class Maxpool2DCalculator:
    def __init__(self, window):
        self.windowLabel = "2D Maxpooling Layer"
        window.title(self.windowLabel)

        self.window = ttk.Frame(window)
        ttk.Label(window, text="2D Maxpooling Layer", font=("courier", 15, "bold")).pack()
        self.window.pack()

        self.__add_labels__()
        self.__add_input_fields__()

    def __add_labels__(self):
        ttk.Label(self.window, text="Input Size") \
            .grid(row=0, column=1, padx=5, pady=5, sticky="w")
        ttk.Label(self.window, text="Kernel Size") \
            .grid(row=1, column=1, padx=5, pady=5, sticky="w")
        ttk.Label(self.window, text="Output Depth") \
            .grid(row=2, column=1, padx=5, pady=5, sticky="w")
        ttk.Label(self.window, text="Stride") \
            .grid(row=1, column=4, padx=5, pady=5, sticky="w")
        ttk.Label(self.window, text="Padding") \
            .grid(row=0, column=4, padx=5, pady=5, sticky="w")
        ttk.Label(self.window, text="Dilation") \
            .grid(row=2, column=4, padx=5, pady=5, sticky="w")

        ttk.Label(self.window, text="Output") \
            .grid(row=5, column=3, padx=5, pady=5, sticky="w")

    def __add_input_fields__(self):
        # calculateConvolution button
        self.calculate_btn = ttk.Button(self.window, text="Maxpool2D")
        self.calculate_btn.grid(row=3, column=5, columnspan=2, padx=5, pady=5, sticky="w")
        self.calculate_btn.config(command=self.calculateMaxPooling)

        # calculate MaxUnpool2d button
        self.calculate_maxunpool2d_btn = ttk.Button(self.window, text="MaxUnpool2D")
        self.calculate_maxunpool2d_btn.grid(row=3, column=1, columnspan=2, padx=5, pady=5, stick='w')
        self.calculate_maxunpool2d_btn.config(command=self.calculateMaxUnpooling)

        # input size field
        self.input_size_field = ttk.Entry(self.window)
        self.input_size_field.insert(0, "C x H x W")
        self.input_size_field.grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky='w')
        self.input_size_field.bind('<Control-a>', entrySelectAllHandler)

        # kernel size field
        self.kernel_size_field = ttk.Entry(self.window)
        self.kernel_size_field.insert(0, "N | M x N")
        self.kernel_size_field.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky='w')
        self.kernel_size_field.bind('<Control-a>', entrySelectAllHandler)

        # Output depth field
        self.output_depth_field = ttk.Entry(self.window)
        self.output_depth_field.insert(0, "Equal to Input Depth")
        self.output_depth_field.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky='w')
        self.output_depth_field.bind('<Control-a>', entrySelectAllHandler)
        self.output_depth_field.config(state="readonly")

        # padding size field
        self.padding_field = ttk.Entry(self.window)
        self.padding_field.insert(0, "N | M x N, default = 0")
        self.padding_field.grid(row=0, column=5, columnspan=2, padx=5, pady=5, sticky='w')
        self.padding_field.bind('<Control-a>', entrySelectAllHandler)

        # stride size field
        self.stride_field = ttk.Entry(self.window)
        self.stride_field.insert(0, "N | M x N, default = 1")
        self.stride_field.grid(row=1, column=5, columnspan=2, padx=5, pady=5, sticky='w')
        self.stride_field.bind('<Control-a>', entrySelectAllHandler)

        # dilation size field
        self.dilation_field = ttk.Entry(self.window)
        self.dilation_field.insert(0, "N | M x N, default = 1")
        self.dilation_field.grid(row=2, column=5, columnspan=2, padx=5, pady=5, sticky='w')
        self.dilation_field.bind('<Control-a>', entrySelectAllHandler)

        # output filed
        self.output_field = ttk.Entry(self.window)
        self.output_field.insert(0, "Output")
        self.output_field.grid(row=5, column=4, columnspan=2, padx=5, pady=25, sticky="w")
        self.output_field.bind('<Control-a>', entrySelectAllHandler)
        self.output_field.config(state='readonly')

    def __parse_input__(self):
        # parse input size
        raw_input = re.split("[Xx]", self.input_size_field.get().replace(" ", ""))
        try:
            raw_input = list(map(int, raw_input))
        except ValueError:
            messagebox.showerror(title="Fix Input Size", message="Error: Input size conversion failed!!")
            return False
        if len(raw_input) != 3:
            messagebox.showerror(title="Fix Input Size", message="Error: Invalid Input Size!!")
            return False
        self.Cin = raw_input[0]
        self.Hin = raw_input[1]
        self.Win = raw_input[2]

        # parse kernel size
        raw_input = re.split("[Xx]", self.kernel_size_field.get().replace(" ", ""))
        try:
            raw_input = list(map(int, raw_input))
        except ValueError:
            messagebox.showerror(title="Fix Kernel Size", message="Error: Kernel size conversion failed!!")
            return False
        # print(len(raw_input))
        if len(raw_input) < 1 or len(raw_input) > 3:
            messagebox.showerror(title="Fix Kernel Size", message="Error: Invalid Kernel Size!!")
            return False

        if len(raw_input) == 2:
            self.kernel_size = (raw_input[0], raw_input[1])
        else:
            self.kernel_size = (raw_input[0], raw_input[0])

        # parse stride
        raw_input = re.split("[Xx]", self.stride_field.get().replace(" ", ""))
        try:
            raw_input = list(map(int, raw_input))
        except ValueError:
            raw_input = []
            # messagebox.showerror(title="Fix Kernel Size", message="Error: Kernel size conversion failed!!")

        if len(raw_input) > 3:
            messagebox.showerror(title="Fix Stride Size", message="Error: Invalid Stride Size!!")
            return False
        self.stride = (1, 1)
        if len(raw_input) == 2:
            self.stride = (raw_input[0], raw_input[1])
        elif len(raw_input) == 1:
            self.stride = (raw_input[0], raw_input[0])

        # parse padding
        raw_input = re.split("[Xx]", self.padding_field.get().replace(" ", ""))
        try:
            raw_input = list(map(int, raw_input))
        except ValueError:
            raw_input = []
            # messagebox.showerror(title="Fix Kernel Size", message="Error: Kernel size conversion failed!!")

        if len(raw_input) > 3:
            messagebox.showerror(title="Fix Padding Size", message="Error: Invalid Padding Size!!")
            return False
        self.padding = (0, 0)
        if len(raw_input) == 2:
            self.padding = (raw_input[0], raw_input[1])
        elif len(raw_input) == 1:
            self.padding = (raw_input[0], raw_input[0])

        # parse dilation
        raw_input = re.split("[Xx]", self.dilation_field.get().replace(" ", ""))
        try:
            raw_input = list(map(int, raw_input))
        except ValueError:
            raw_input = []
            # messagebox.showerror(title="Fix Kernel Size", message="Error: Kernel size conversion failed!!")

        if len(raw_input) > 3:
            messagebox.showerror(title="Fix Stride Size", message="Error: Invalid Stride Size!!")
            return False
        self.dilation = (1, 1)
        if len(raw_input) == 2:
            self.dilation = (raw_input[0], raw_input[1])
        elif len(raw_input) == 1:
            self.dilation = (raw_input[0], raw_input[0])
        return True

    def calculateMaxPooling(self):
        if self.__parse_input__():
            self.__calculateMaxPooling__()
            self.__show_output__()

    def calculateMaxUnpooling(self):
        if self.__parse_input__():
            self.__calculateMaxUnpooling__()
            self.__show_output__()

    def __calculateMaxPooling__(self):
        self.Hout = math.floor((1.0 * (self.Hin + 2 * self.padding[0] - self.dilation[0] * (self.kernel_size[0] - 1) - 1) / self.stride[0]) + 1)
        self.Wout = math.floor((1.0 * (self.Win + 2 * self.padding[1] - self.dilation[1] * (self.kernel_size[1] - 1) - 1) / self.stride[1]) + 1)
        self.Cout = self.Cin

    def __calculateMaxUnpooling__(self):
        self.Hout = (self.Hin-1)*self.stride[0] - 2*self.padding[0]+self.kernel_size[0]
        self.Wout = (self.Win-1)*self.stride[1] - 2*self.padding[1]+self.kernel_size[1]
        self.Cout = self.Cin

    def __show_output__(self):
        self.output_field.config(state="normal")
        self.output_field.delete(0, 'end')
        self.output_field.insert(0, str(self.Cout) + "X" + str(self.Hout) + "X" + str(self.Wout))
        self.output_field.config(state="readonly")
