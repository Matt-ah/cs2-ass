import tkinter as tk
from monopoly1920 import controller

if __name__ == "__main__":
    root = tk.Tk()
    game = controller.Controller(root)
    root.mainloop()
