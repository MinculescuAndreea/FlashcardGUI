from customtkinter import CTk, set_appearance_mode
from CTkMessagebox import CTkMessagebox

class Window(CTk):
    def __init__(self, window_title):
        """
        Class that stores general specifications for windows
        :param window_title: the title of the window
        """
        # initialize a CTk window
        CTk.__init__(self)
        # set to dark mode
        set_appearance_mode("dark")
        # set window to fullscreen
        self.after(0, lambda: self.state('zoomed'))
        # store the width and height of the window (the width and height of the screen, for fullscreen)
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        # set window title
        self.title(window_title)

    def change_title(self, text):
        """
        Change title of the window
        :param text: the new text
        """
        self.title(text)
