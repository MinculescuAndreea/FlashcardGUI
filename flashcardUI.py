import customtkinter as ctk
import pandas as pd
from flashcard import Flashcard
from CTkMessagebox import CTkMessagebox
from functools import partial


class FlashcardApp:
    def __init__(self, master, vocab_path):
        """
        Class that handles the Flascard UI
        :param master: the window
        :param vocab_path: the path to the document where the vocabulary is stored
        """
        self.master = master
        self.vocab_path = vocab_path
        self.df_words = pd.read_csv(self.vocab_path)

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

    @staticmethod
    def show_warning(title):
        """
        Define standard format of warnings
        @param title: title of warning
        """
        msg = CTkMessagebox(title="Warning", message=title, icon="warning.png")
        # if the message is not closed manually, it disappears after 10 seconds
        msg.after(10_000, msg.destroy)


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
        self.large_font = ('Arial', 18)

        # empty label for spacing
        ctk.CTkLabel(self.frame, text=" ", height=self.master.width / 6).grid(row=0, column=0)

        # text to be displayed in the middle of the screen
        intro_text = "Welcome to the Flashcard GUI!"
        self.label_intro = ctk.CTkLabel(self.frame, text=intro_text, font=self.large_font, text_color="#FFCC70",
                                        width=self.master.width)
        self.label_intro.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        ###############################################################
        # empty label for spacing
        ctk.CTkLabel(self.frame, text=" ", height=self.master.width / 6).grid(row=2, column=0)

        # button for functionality (a)
        self.edit_deck_button = ctk.CTkButton(self.frame, text="Edit deck", command=self.edit_deck_func,
                                              font=self.large_font, fg_color="#4158D0", hover_color="#C850C0",
                                              corner_radius=32)
        self.edit_deck_button.grid(row=3, column=1, pady=10, sticky='w')

        # button for functionality (b)
        self.study_button = ctk.CTkButton(self.frame, text="Start study session", command=self.study_func,
                                          font=self.large_font, fg_color="#4158D0", hover_color="#C850C0",
                                          corner_radius=32)
        self.study_button.grid(row=3, column=1, pady=10, sticky='e')

    def edit_deck_func(self):
        """
        Logic for functionality (a): create popup window and add to or delete from vocabulary
        """
        # place window in the middle of the screen
        x = int(self.master.width / 2)
        y = int(self.master.height / 2)
        # define popup window as top level
        self.top_deck = ctk.CTkToplevel(width=x, height=y)
        self.top_deck.geometry(f"+{x - int(self.master.width / 5)}+{y - int(self.master.height / 5)}")
        # make top level the main window
        self.top_deck.transient(self.master)

        ###############################################################
        # label for instruction text
        self.ask_action = ctk.CTkLabel(self.top_deck, text="What would you like to do?", font=self.large_font)
        self.ask_action.grid(row=0, column=0, columnspan=2, padx=10, pady=50, sticky="nsew")

        ###############################################################
        # button for Add words funtionality
        self.add_words_button = ctk.CTkButton(self.top_deck, text="Add words", command=self.add_words_func,
                                              font=self.large_font, fg_color="#4158D0", hover_color="#C850C0",
                                              corner_radius=32)
        self.add_words_button.grid(row=1, column=0, pady=self.master.height / 12, padx=self.master.width / 12,
                                   sticky='e')

        ###############################################################
        # button for Delete words functionality
        self.delete_words_button = ctk.CTkButton(self.top_deck, text="Delete words", command=self.delete_words_func,
                                                 font=self.large_font, fg_color="#4158D0", hover_color="#C850C0",
                                                 corner_radius=32)
        self.delete_words_button.grid(row=1, column=1, pady=self.master.height / 12, padx=self.master.width / 12,
                                      sticky='w')

    def add_words_func(self):
        """
        Create popup window and store text in vocabulary.csv
        """
        # destroy previous window
        self.top_deck.destroy()

        # place window in the middle of the screen
        x = int(self.master.width / 2)
        y = int(self.master.height / 2)
        # define popup window as top level
        self.top_add = ctk.CTkToplevel(width=x, height=y)
        self.top_add.geometry(f"+{x - int(self.master.width / 5)}+{y - int(self.master.height / 5)}")
        # make top level the main window
        self.top_add.transient(self.master)

        ###############################################################
        # label and text box for one face of the flashcard
        self.label_face_one = ctk.CTkLabel(self.top_add, text="Please enter text for face one:", font=self.large_font)
        self.label_face_one.grid(row=0, column=0, pady=10, padx=10)

        self.text_face_one = ctk.CTkTextbox(self.top_add, font=self.large_font, width=self.master.width / 2, height=50,
                                            text_color="#FFCC70", scrollbar_button_color="#4158D0",
                                            scrollbar_button_hover_color="#C850C0")
        self.text_face_one.grid(row=1, column=0, pady=20, padx=10)

        ###############################################################
        # label and text box for the other face of the flashcard
        self.label_face_two = ctk.CTkLabel(self.top_add, text="Please enter text for face two:", font=self.large_font)
        self.label_face_two.grid(row=2, column=0, pady=20, padx=10)

        self.text_face_two = ctk.CTkTextbox(self.top_add, font=self.large_font, width=self.master.width / 2, height=50,
                                            text_color="#FFCC70", scrollbar_button_color="#4158D0",
                                            scrollbar_button_hover_color="#C850C0")
        self.text_face_two.grid(row=3, column=0, pady=20, padx=20)

        ###############################################################
        # ok button: when pressed, it stores the text in vocabulary.csv (not functional yet)
        self.ok_button = ctk.CTkButton(self.top_add, text="OK", font=self.large_font, fg_color="#4158D0",
                                       command=self.save_words_to_csv, hover_color="#C850C0", corner_radius=32)
        self.ok_button.grid(row=4, column=0, pady=20, padx=20)

    def delete_words_func(self):
        """
        Create popup window to delete entry from vocabulary.csv. The user can select a word (from any flipcard side)
        from a drop-down menu and, upon button click, the corresponding word pair is deleted from the csv file
        """
        # destroy previous window
        self.top_deck.destroy()

        # place window in the middle of the screen
        x = int(self.master.width / 2)
        y = int(self.master.height / 2)
        # define popup window as top level
        self.top_delete = ctk.CTkToplevel(width=x, height=y)
        self.top_delete.geometry(f"+{x - int(self.master.width / 5)}+{y - int(self.master.height / 5)}")
        # make top level the main window
        self.top_delete.transient(self.master)

        ###############################################################
        # label and drop down menu to select from face 1
        self.label_select_one = ctk.CTkLabel(self.top_delete, text="Select card by front side:", font=self.large_font)
        self.label_select_one.grid(row=0, column=0, pady=10, padx=50)
        # empty label for formatting
        ctk.CTkLabel(self.top_delete, text=" ", width=self.master.width / 10).grid(row=0, column=1)
        self.drplist_face_one = ctk.CTkComboBox(self.top_delete, values=list(self.app.df_words["Face1"]),
                                                state='readonly', dropdown_fg_color="#4158D0",
                                                corner_radius=32, width=235)
        self.drplist_face_one.grid(row=0, column=2, pady=10, padx=10)
        # empty label for formatting
        ctk.CTkLabel(self.top_delete, text=" ", width=self.master.width / 10).grid(row=0, column=3)

        ###############################################################
        # label and drop down menu to select from face 2
        self.label_select_two = ctk.CTkLabel(self.top_delete, text="Select card by back side:", font=self.large_font)
        self.label_select_two.grid(row=1, column=0, pady=10, padx=50)
        ctk.CTkLabel(self.top_delete, text=" ", width=self.master.width / 10).grid(row=1, column=1)
        self.drplist_face_two = ctk.CTkComboBox(self.top_delete, values=list(self.app.df_words["Face2"]),
                                                state='readonly', dropdown_fg_color="#4158D0",
                                                corner_radius=32, width=235)
        self.drplist_face_two.grid(row=1, column=2, pady=10, padx=10)
        # empty label for formatting
        ctk.CTkLabel(self.top_delete, text=" ", width=self.master.width / 10).grid(row=1, column=3)

        ###############################################################
        # if one word has been selected from one drop-down menu, then show its pair in the other drop-down menu
        self.drplist_face_one.configure(command=partial(self.change_default_combobox, "two"))
        self.drplist_face_two.configure(command=partial(self.change_default_combobox, "one"))

        ###############################################################
        # ok button: when clicked, the word pair is deleted from the csv file
        self.ok_button = ctk.CTkButton(self.top_delete, text="OK", font=self.large_font, fg_color="#4158D0",
                                       command=self.delete_from_csv, hover_color="#C850C0", corner_radius=32)
        self.ok_button.grid(row=2, column=1, pady=20, padx=20, sticky="e")

    def change_default_combobox(self, side, chosen):
        """
        Change default value from specified combo-box to match the other combo-box
        :param side: whether the user has modified the combo-box associated with the first side (front side) or the
        second side (back side) of the flipcard
        :param chosen: the option selected by the user in the combo-box
        """
        if side == "one":
            # find the pair entry
            new_value = self.app.df_words["Face1"].loc[self.app.df_words["Face2"] == chosen].values[0]
            # display the pair entry in the other combo-box
            self.drplist_face_one.configure(variable=ctk.StringVar(value=new_value))
        elif side == "two":
            new_value = self.app.df_words["Face2"].loc[self.app.df_words["Face1"] == chosen].values[0]
            self.drplist_face_two.configure(variable=ctk.StringVar(value=new_value))

    def save_words_to_csv(self):
        """
        Save word pairs to vocabulary.csv
        """
        # get the word pair
        first_word = self.text_face_one.get("1.0", "end-1c")
        second_word = self.text_face_two.get("1.0", "end-1c")

        # if any entry is empty, show warning and exit
        if first_word == "" or second_word == "":
            self.app.show_warning("Please fill in all entries before continuing")
            return

        # add word pair to dataframe
        self.app.df_words.loc[len(self.app.df_words.index)] = [first_word, second_word, 1]
        self.app.df_words.reset_index(inplace=True, drop=True)
        self.app.df_words.to_csv("vocabulary.csv", index=False)

        # destroy "Add words" window
        self.top_add.destroy()

    def delete_from_csv(self):
        """
        Delete row(s) from csv by cell values
        """
        # get word pair to be deleted
        to_remove_one = self.drplist_face_one.get()
        to_remove_two = self.drplist_face_two.get()

        # if nothing has been selected, show warning and exit
        if to_remove_one == "":
            self.app.show_warning("Please select something first")
            return

        # drop all rows with cell values as specified by the user
        self.app.df_words.drop(self.app.df_words[(self.app.df_words["Face1"] == to_remove_one) &
                                                 (self.app.df_words["Face2"] == to_remove_two)].index, inplace=True)
        # reset index and update csv file
        self.app.df_words.reset_index(inplace=True, drop=True)
        self.app.df_words.to_csv("vocabulary.csv", index=False)

        # destroy previous window
        self.top_delete.destroy()

    def study_func(self):
        """
        Logic for functionality (b): delete previous content from frame and show the vocab pairs one-by-one. The latter
        is a simplified version, as it does not account for past performance when setting the pair order.
        """
        # destroy frame
        self.frame.destroy()

        # for every pair, show both faces
        for (idx, row) in self.app.df_words.iterrows():
            card = Flashcard(self.master, row["Face1"], row["Face2"])
            self.master.mainloop()
            card = Flashcard(self.master, row["Face2"], row["Face1"])
            self.master.mainloop()
