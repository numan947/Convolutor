from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Convolutor:
    def __init__(self, rootWindow):
        self.root = rootWindow

        self.conv2d_image = PhotoImage(file="../res/conv2d.gif").subsample(7,7)
        self.conv2d_button = ttk.Button(master=self.root, text="Conv2D", command=self.Conv2dHelper, image = self.conv2d_image, compound = LEFT)
        self.conv2d_button.grid(row=0, column=0)



    def Conv2dHelper(self):
        print("Hello World")


def main():
    root = Tk()

    mainProgram = Convolutor(root)

    root.mainloop()


if __name__ == "__main__":
    main()
