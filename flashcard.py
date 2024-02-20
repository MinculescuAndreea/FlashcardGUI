import customtkinter as ctk


class Flashcard:
    def __init__(self, master, front_text, back_text):
        """
        Class to handle flashcard styling and logic
        :param master: the window
        :param front_text: the text on the front side (shown to the user)
        :param back_text: the text on the back side
        """
        self.master = master
        self.front_text = front_text
        self.back_text = back_text

        # empty labels for spacing
        ctk.CTkLabel(self.master, text="", height=self.master.height / 5).grid(row=0, column=0)
        ctk.CTkLabel(self.master, text="", width=self.master.width / 3).grid(row=1, column=0)

        # label for flashcard text
        self.card_widget = ctk.CTkLabel(self.master, text="", text_color="black", height=self.master.height / 3,
                                        width=self.master.width / 3, wraplength=self.master.width / 3, fg_color='gray',
                                        font=("Arial", 30), corner_radius=20)
        # display front text
        self.add_text(self.front_text)
        self.card_widget.grid(row=1, column=1)

        ############################################
        # empty labels for spacing
        ctk.CTkLabel(self.master, text="", width=self.master.width / 3).grid(row=1, column=2)
        ctk.CTkLabel(self.master, text="", height=self.master.height / 4).grid(row=2, column=0)

        # button to show the answer on the back
        self.submit_button = ctk.CTkButton(self.master, text='Show answer', corner_radius=32, fg_color="#4158D0",
                                           hover_color="#C850C0", width=120, height=32, font=("Arial", 18),
                                           command=lambda: self.add_text(f"\n{'-'*20}\n{self.back_text}"))
        self.submit_button.grid(row=3, column=1, padx=10, pady=20, sticky="w")

        # button to skip to the next flashcard
        self.next_button = ctk.CTkButton(self.master, text='Next card', corner_radius=32, fg_color="#4158D0",
                                         hover_color="#C850C0", width=120, height=32, font=("Arial", 18),
                                         command=self.next_button_func)
        self.next_button.grid(row=3, column=1, padx=10, pady=20, sticky="e")

    def add_text(self, text):
        """
        Add text to the flashcard label
        :param text: text to be added
        """
        # get already existing text
        old_text = self.card_widget.cget("text")
        # if the answer has not already been revealed...
        if "-" not in old_text:
            # show the text on the back side (together with the text on the front side)
            self.card_widget.configure(text=old_text+text)

    def next_button_func(self):
        """
        If flashcard skipped, then simply quit
        """
        self.master.quit()
