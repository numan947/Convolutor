from tkinter import *
from tkinter import ttk
from src.Conv2DCalculator import Conv2DCalculator
from src.Maxpool2DCalculator import Maxpool2DCalculator


class ButtonCfg:
    def __init__(self, r, c, text, imagepath=None, compound=LEFT, padx=0, pady=0, ipadx=0, ipady=0, ):
        self.ipady = ipady
        self.ipadx = ipadx
        self.pady = pady
        self.padx = padx
        self.r = r
        self.c = c
        self.text = text
        self.imagepath = imagepath
        self.compound = compound


class ButtonOperation:
    def __init__(self, buttonCfg, root, calculatorFunction):
        self.buttonCfg = buttonCfg
        self.root = root
        self.calculatorFunction = calculatorFunction

        self.image = None
        if buttonCfg.imagepath is not None:
            self.image = PhotoImage(file=self.buttonCfg.imagepath)

        self.window = None
        self.calculator = None
        self.image = None  # PhotoImage(file="../res/conv2d.gif").subsample(7, 7)
        self.button = ttk.Button(master=self.root, text=buttonCfg.text, command=self.buttonClickHandler,
                                 image=self.image, compound=buttonCfg.compound)
        self.button.grid(row=self.buttonCfg.r, column=self.buttonCfg.c, padx=self.buttonCfg.padx,
                         pady=self.buttonCfg.pady)

    def buttonClickHandler(self):
        if self.window is not None:
            self.window.lift()
            return

        def clearWindow():
            self.window.destroy()
            self.window = None
            self.calculator = None

        self.window = Toplevel(self.root)
        self.window.protocol("WM_DELETE_WINDOW", clearWindow)
        self.calculator = self.calculatorFunction(self.window)
        self.window.mainloop()


class Convolutor:
    def __init__(self, rootWindow):
        self.root = rootWindow
        self.root.title("CONVOLUTOR")

        # Conv2D
        self.convolution2DButtonConfig = ButtonCfg(r=0, c=0, padx=10, pady=10, text="Conv2D")
        self.convolution2DCalculator = ButtonOperation(root=self.root, calculatorFunction=Conv2DCalculator,
                                                       buttonCfg=self.convolution2DButtonConfig)
        # Maxpool2D
        self.maxpool2DButtonConfig = ButtonCfg(r=0, c=1, padx=10, pady=10, text="MaxPool2D")
        self.maxpool2DCalculator = ButtonOperation(root=self.root, calculatorFunction=Maxpool2DCalculator,
                                                   buttonCfg=self.maxpool2DButtonConfig)

        # ConvTranspose2D
        self.convtranspose2DButtonConfig = ButtonCfg(r=0, c=2, padx=10, pady=10, text="ConvTranspose2D")
        self.convtranspose2DCalculator = ButtonOperation(root=self.root, calculatorFunction=None,
                                                         buttonCfg=self.convtranspose2DButtonConfig)


def main():
    root = Tk()
    s = ttk.Style()
    s.theme_use('clam')
    s.configure('TButton', font=('courier', 12))
    s.configure('TEntry', font=('courier', 12))
    s.configure('TLabel', font=('courier', 12))
    # #
    mainProgram = Convolutor(root)

    root.mainloop()


if __name__ == "__main__":
    main()
