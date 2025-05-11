import tkinter as tk

root = tk.Tk()
root.title("Timer")
root.geometry("1500x600")


class Timer():
    def __init__(self):
        self.label = tk.Label(root, text="Sample text")
        self.label.pack()


timer = Timer()
root.mainloop()