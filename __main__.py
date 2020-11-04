import tkinter as tk
from tkinter.font import Font

# Constants
BG = "#363732"
FG = "#f76931"
ABG = "#464743"

class TWin(tk.Toplevel):
    def __init__(self, title, geometry):
        super().__init__()

        self.title(title)
        self.geometry(geometry)
        self.configure(bg=BG)


class MWin(tk.Tk):
    def __init__(self):
        super().__init__()
        # Windows 
        self.title("Why learn Python in 2020?")
        self.geometry("400x200+730+300")
        self.configure(bg=BG)
        # Labels
        tk.Label(self,
            text="Same text to show foreground color on background color", bg=BG, fg=FG,
            wraplength=300, font=Font(size=14)).place(anchor="n", relx=0.5, rely=0.05)
        # Buttons
        tk.Button(self, text="Data science", bg=BG, fg=FG, relief="groove",
            command=self.tlevel_datascience,
            activebackground=ABG, activeforeground=FG).place(anchor="n", relx=0.3, rely=0.35)


    def tlevel_datascience(self):
        dt_sci = TWin("Python data science", "400x200+730+540")
        tk.Label(dt_sci, text="Another sample label.", bg=BG, fg=FG,
            wraplength=500, font=Font(size=14)).place(anchor="n", relx=0.5, rely=0.05)


if __name__ == "__main__":
    MWin().mainloop()