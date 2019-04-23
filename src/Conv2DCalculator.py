import math
import re
from tkinter import messagebox
from tkinter import ttk
from src.Common import entrySelectAllHandler

class Conv2DCalculator:
    def __init__(self, window):
        self.windowLabel = "2D Convolution"
        window.title(self.windowLabel)

        self.window = ttk.Frame(window)
        ttk.Label(window, text="2D Convolution", font=("courier", 15, "bold")).pack()
        self.window.pack()

        self.__add_labels__()
        self.__add_input_fields__()
        self.close_btn = ttk.Button(window, text="Close")
        self.close_btn.pack(padx=5, pady=5)

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
        # calculate button
        self.calculate_btn = ttk.Button(self.window, text="Calculate")
        self.calculate_btn.grid(row=3, column=5, columnspan=2, padx=5, pady=5, sticky="w")
        self.calculate_btn.config(command=self.calculate)

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
        self.output_depth_field.insert(0, "N")
        self.output_depth_field.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky='w')
        self.output_depth_field.bind('<Control-a>', entrySelectAllHandler)

        # stride size field
        self.stride_field = ttk.Entry(self.window)
        self.stride_field.insert(0, "N | M x N, default = 1")
        self.stride_field.grid(row=1, column=5, columnspan=2, padx=5, pady=5, sticky='w')
        self.stride_field.bind('<Control-a>', entrySelectAllHandler)

        # padding size field
        self.padding_field = ttk.Entry(self.window)
        self.padding_field.insert(0, "N | M x N, default = 0")
        self.padding_field.grid(row=0, column=5, columnspan=2, padx=5, pady=5, sticky='w')
        self.padding_field.bind('<Control-a>', entrySelectAllHandler)

        # dilation size field
        self.dilation_field = ttk.Entry(self.window)
        self.dilation_field.insert(0, "N | M x N, default = 1")
        self.dilation_field.grid(row=2, column=5, columnspan=2, padx=5, pady=5, sticky='w')
        self.dilation_field.bind('<Control-a>', entrySelectAllHandler)

        # output filed
        self.output_field = ttk.Entry(self.window)
        self.output_field.insert(0, "Output")
        self.output_field.grid(row=5, column=4, columnspan=2, padx=5, pady=5, sticky="w")
        self.output_field.bind('<Control-a>', entrySelectAllHandler)
        self.output_field.config(state='readonly')

    def calculate(self):
        # parse input size
        raw_input = re.split("X|x", self.input_size_field.get().replace(" ", ""))
        try:
            raw_input = list(map(int, raw_input))
        except ValueError:
            messagebox.showerror(title="Fix Input Size", message="Error: Input size conversion failed!!")
            return
        if len(raw_input) != 3:
            messagebox.showerror(title="Fix Input Size", message="Error: Invalid Input Size!!")
            return
        Cin = raw_input[0]
        Hin = raw_input[1]
        Win = raw_input[2]

        # parse kernel size
        raw_input = re.split("X|x", self.kernel_size_field.get().replace(" ", ""))
        try:
            raw_input = list(map(int, raw_input))
        except ValueError:
            messagebox.showerror(title="Fix Kernel Size", message="Error: Kernel size conversion failed!!")
            return
        print(len(raw_input))
        if len(raw_input) < 1 or len(raw_input) > 3:
            messagebox.showerror(title="Fix Kernel Size", message="Error: Invalid Kernel Size!!")
            return

        kernel_size = None
        if len(raw_input) == 2:
            kernel_size = (raw_input[0], raw_input[1])
        else:
            kernel_size = (raw_input[0], raw_input[0])

        # parse stride
        raw_input = re.split("X|x", self.stride_field.get().replace(" ", ""))
        try:
            raw_input = list(map(int, raw_input))
        except ValueError:
            raw_input = []
            # messagebox.showerror(title="Fix Kernel Size", message="Error: Kernel size conversion failed!!")

        if len(raw_input) > 3:
            messagebox.showerror(title="Fix Stride Size", message="Error: Invalid Stride Size!!")
            return
        stride = (1, 1)
        if len(raw_input) == 2:
            stride = (raw_input[0], raw_input[1])
        elif len(raw_input) == 1:
            stride = (raw_input[0], raw_input[0])

        # parse output depth
        raw_input = self.output_depth_field.get().replace(" ", "")
        print(raw_input)
        try:
            raw_input = int(raw_input)
        except ValueError:
            messagebox.showerror(title="Fix Output Depth", message="Error: Output depth conversion failed!!")
            return

        Cout = raw_input

        # parse padding
        raw_input = re.split("X|x", self.padding_field.get().replace(" ", ""))
        try:
            raw_input = list(map(int, raw_input))
        except ValueError:
            raw_input = []
            # messagebox.showerror(title="Fix Kernel Size", message="Error: Kernel size conversion failed!!")

        if len(raw_input) > 3:
            messagebox.showerror(title="Fix Padding Size", message="Error: Invalid Padding Size!!")
            return
        padding = (0, 0)
        if len(raw_input) == 2:
            padding = (raw_input[0], raw_input[1])
        elif len(raw_input) == 1:
            padding = (raw_input[0], raw_input[0])

        # parse dilation
        raw_input = re.split("X|x", self.dilation_field.get().replace(" ", ""))
        try:
            raw_input = list(map(int, raw_input))
        except ValueError:
            raw_input = []
            # messagebox.showerror(title="Fix Kernel Size", message="Error: Kernel size conversion failed!!")

        if len(raw_input) > 3:
            messagebox.showerror(title="Fix Stride Size", message="Error: Invalid Stride Size!!")
            return
        dilation = (1, 1)
        if len(raw_input) == 2:
            dilation = (raw_input[0], raw_input[1])
        elif len(raw_input) == 1:
            dilation = (raw_input[0], raw_input[0])

        Hout = math.floor((1.0 * (Hin + 2 * padding[0] - dilation[0] * (kernel_size[0] - 1) - 1) / stride[0]) + 1)
        Wout = math.floor((1.0 * (Win + 2 * padding[1] - dilation[1] * (kernel_size[1] - 1) - 1) / stride[1]) + 1)

        self.output_field.config(state="normal")
        self.output_field.delete(0, 'end')
        self.output_field.insert(0, str(Cout) + "X" + str(Hout) + "X" + str(Wout))
        self.output_field.config(state="readonly")
