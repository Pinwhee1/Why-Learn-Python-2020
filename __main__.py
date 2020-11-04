import tkinter as tk
from tkinter.font import Font
import webbrowser

# Constants
BG = "#363732"
FG = "#f76931"
ABG = "#464743"
REL = "flat"

class TWin(tk.Toplevel):
    def __init__(self, title, geometry):
        super().__init__()

        self.title(title)
        self.geometry(geometry)
        self.resizable(False, False)
        self.configure(bg=BG)


class MWin(tk.Tk):
    def __init__(self):
        super().__init__()
        # Windows 
        self.title("Why learn Python in 2020?")
        self.geometry("400x200+730+300")
        self.resizable(False, False)
        self.configure(bg=BG)
        # Labels
        tk.Label(self,
            text="There are lots of reasons to learn Python, but here are some things you can do with it!", bg=BG, fg=FG,
            wraplength=350, font=Font(size=14)).place(anchor="n", relx=0.5, rely=0.05)
        # Buttons
        # Data science toplevel button
        tk.Button(self, text="Data science", bg=BG, fg=FG, relief=REL,
            command=self.tlevel_datascience,
            activebackground=ABG, activeforeground=FG).place(anchor="n", relx=0.3, rely=0.5)
        # Machine learning toplevel button
        tk.Button(self, text="Machine learning", bg=BG, fg=FG, relief=REL,
            command=self.tlevel_machinelearning,
            activebackground=ABG, activeforeground=FG).place(anchor="n", relx=0.7, rely=0.5)
        # Game dev toplevel button
        tk.Button(self, text="Gave dev", bg=BG, fg=FG, relief=REL,
            command=self.tlevel_gamedev,
            activebackground=ABG, activeforeground=FG).place(anchor="n", relx=0.3, rely=0.7)
        # Web dev toplevel button
        tk.Button(self, text="Web dev", bg=BG, fg=FG, relief=REL,
            command=self.tlevel_webdev,
            activebackground=ABG, activeforeground=FG).place(anchor="n", relx=0.7, rely=0.7)


    def tlevel_datascience(self):
        dt_sci = TWin("Data science with Python", "400x200+730+540")
        tk.Label(dt_sci,
            text="Data science with Python is completely possible! There's tons of modules out there to help you, like 'pandas' and 'madplotlib'. Check them out, these modules will allow you to manipulate data, graph data, and more!", bg=BG, fg=FG,
            wraplength=350, font=Font(size=12)).place(anchor="n", relx=0.5, rely=0.05)
        tk.Button(dt_sci, text="pandas.pydata.org", font=Font(size=9),
            bg=BG, fg=FG, activebackground=ABG, activeforeground=FG,
            command=lambda: webbrowser.open("https://pandas.pydata.org/")).place(
            anchor="n", relx=0.3, rely=0.7, relwidth=0.3)
        tk.Button(dt_sci, text="matplotlib.org/", font=Font(size=9),
            bg=BG, fg=FG, activebackground=ABG, activeforeground=FG,
            command=lambda: webbrowser.open("https://matplotlib.org/")).place(
            anchor="n", relx=0.7, rely=0.7, relwidth=0.3)

    def tlevel_machinelearning(self):
        mc_learn = TWin("Machine learning with Python", "400x200+730+540")
        tk.Label(mc_learn, text="Machine learning is very popular in python, lot's of people do it and there's plenty of resources out there to get started doing some machine learning. Here are some links:", bg=BG, fg=FG,
            wraplength=350, font=Font(size=12)).place(anchor="n", relx=0.5, rely=0.05)
        tk.Button(mc_learn, text="Geeks for Geeks", font=Font(size=9),
            bg=BG, fg=FG, activebackground=ABG, activeforeground=FG,
            command=lambda: webbrowser.open(
                "https://www.geeksforgeeks.org/introduction-machine-learning-using-python/")).place(
            anchor="n", relx=0.3, rely=0.7, relwidth=0.3)
        tk.Button(mc_learn, text="pythonbasics.org", font=Font(size=9),
            bg=BG, fg=FG, activebackground=ABG, activeforeground=FG,
            command=lambda: webbrowser.open("https://pythonbasics.org/what-is-machine-learning/")).place(
            anchor="n", relx=0.7, rely=0.7, relwidth=0.3)

    def tlevel_gamedev(self):
        gd = TWin("Game development with Python", "400x200+730+540")
        tk.Label(gd,
            text="Python isn't really the strongest language for game development due to it's slow nature, but it's 100% possible! Pygame is one of the bigger and more used modules and probably the best to get started with!", bg=BG, fg=FG,
            wraplength=350, font=Font(size=12)).place(anchor="n", relx=0.5, rely=0.05)
        tk.Button(gd, text="pygame.org", font=Font(size=9),
            bg=BG, fg=FG, activebackground=ABG, activeforeground=FG,
            command=lambda: webbrowser.open("https://www.pygame.org/news")).place(
            anchor="n", relx=0.5, rely=0.6, relwidth=0.3)

    def tlevel_webdev(self):
        wd = TWin("Web development with Python", "400x200+730+540")
        tk.Label(wd, text="Web development in Python is super fast, clean, and practical with Django! Django is one of the main modules you can use to do web development with Python!", bg=BG, fg=FG,
            wraplength=350, font=Font(size=12)).place(anchor="n", relx=0.5, rely=0.05)
        tk.Button(wd, text="djangoproject.com", font=Font(size=9),
            bg=BG, fg=FG, activebackground=ABG, activeforeground=FG,
            command=lambda: webbrowser.open("https://www.djangoproject.com/")).place(
            anchor="n", relx=0.5, rely=0.6, relwidth=0.3)

if __name__ == "__main__":
    MWin().mainloop()