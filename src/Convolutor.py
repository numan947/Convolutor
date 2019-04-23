from tkinter import *
from tkinter import ttk
from src.Conv2DCalculator import Conv2DCalculator


class Convolutor:
    def __init__(self, rootWindow):
        self.root = rootWindow
        self.root.title("CONVOLUTOR")

        # CONV2D Configuration
        self.conv2d_window = None
        self.conv2d_calculator = None
        self.conv2d_image = PhotoImage(file="../res/conv2d.gif").subsample(7, 7)
        self.conv2d_button = ttk.Button(master=self.root, text="Conv2D", command=self.Conv2dHelper,
                                        image=self.conv2d_image, compound=LEFT)
        self.conv2d_button.grid(row=0, column=0, padx=10, pady=10)

    def Conv2dHelper(self):
        if self.conv2d_window is not None:
            self.conv2d_window.lift()
            return

        def clearWindow():
            self.conv2d_window.destroy()
            self.conv2d_window = None
            self.conv2d_calculator = None

        self.conv2d_window = Toplevel(self.root)
        self.conv2d_window.protocol("WM_DELETE_WINDOW", clearWindow)
        self.conv2d_calculator = Conv2DCalculator(self.conv2d_window)
        self.conv2d_window.mainloop()


def main():
    root = Tk()

    mainProgram = Convolutor(root)

    root.mainloop()


if __name__ == "__main__":
    main()
