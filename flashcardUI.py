import customtkinter as ctk
import pandas as pd
from flashcard import Flashcard

class FlashcardApp:
    def __init__(self, master, vocab_path):
        """
        Class that handles the Flascard UI
        :param master: the window
        :param vocab_path: the path to the document where the vocabulary is stored
        """
        self.master = master
        self.vocab_path = vocab_path

        # order of pages
        self.pages = [Page0(self.master, self)]
        # current form page to be displayed
        self.current_page = 0
        # function to display the current form page
        self.show_current_page()

    def show_current_page(self):
        """
        Function to display the current page form in a grid format
        """
        self.pages[self.current_page].frame.grid(row=0, column=0, sticky="nsew")

    def show_page(self, idx):
        """
        Display the next form page given the order defined in the init function
        :param idx: the page to be displays
        """
        self.pages[self.current_page].frame.grid_forget()
        self.current_page = idx
        # make sure that the "next" page exists
        if self.current_page < len(self.pages):
            self.show_current_page()
        else:
            self.master.quit()

class Page0:
    def __init__(self, master, app):
        """
        First page makes the connection to the two main functionalities
            a) insert new vocabulary
            b) study session using the existing vocabulary
        :param master: the window
        :param app: the Flashcard UI
        """
        self.master = master
        self.app = app
        # each page is defined as a frame
        self.frame = ctk.CTkFrame(self.master, fg_color="#242424")

        # define font type and size
        large_font = ('Arial', 18)

        # empty label for spacing
        ctk.CTkLabel(self.frame, text=" ", height=self.master.width / 6).grid(row=0, column=0)

        # text to be displayed in the middle of the screen
        intro_text = "Welcome to the Flashcard GUI! \nPlease select what you would like to do:"
        self.label_intro = ctk.CTkLabel(self.frame, text=intro_text, font=large_font, text_color="#FFCC70",
                                        width=self.master.width)
        self.label_intro.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        ###############################################################
        # empty label for spacing
        ctk.CTkLabel(self.frame, text=" ", height=self.master.width / 6).grid(row=2, column=0)

        # button for functionality (a)
        self.add_words_button = ctk.CTkButton(self.frame, text="Add new words", command=self.add_words_func,
                                              font=large_font, fg_color="#4158D0", hover_color="#C850C0",
                                              corner_radius=32)
        self.add_words_button.grid(row=3, column=1, pady=10, sticky='w')

        # button for functionality (b)
        self.study_button = ctk.CTkButton(self.frame, text="Start study session", command=self.study_func,
                                          font=large_font, fg_color="#4158D0", hover_color="#C850C0", corner_radius=32)
        self.study_button.grid(row=3, column=1, pady=10, sticky='e')

    def add_words_func(self):
        """
        Logic for functionality (a): in progress
        """
        pass

    def study_func(self):
        """
        Logic for functionality (b): delete previous content from frame and show the vocab pairs one-by-one. The latter
        is a simplified version, as it does not account for past performance when setting the pair order.
        """
        # destroy frame
        self.frame.destroy()

        # read in the vocab pairs
        self.vocab_pairs = pd.read_csv("vocabulary.csv")
        # for every pair, show both faces
        for (idx,row) in self.vocab_pairs.iterrows():
            card = Flashcard(self.master, row["Face1"], row["Face2"])
            self.master.mainloop()
            card = Flashcard(self.master, row["Face2"], row["Face1"])
            self.master.mainloop()



