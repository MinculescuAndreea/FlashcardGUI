from window import Window
from flashcardUI import FlashcardApp

# generate window object
root = Window("Flashcard GUI")
# generate GUI object
app = FlashcardApp(root, vocab_path="vocabulary.csv")
root.mainloop()
