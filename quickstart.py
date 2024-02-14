from window import Window
from flashcard import Flashcard
import pandas as pd

root = Window("Flashcard GUI")

vocab_pairs = pd.read_csv("vocabulary.csv")
for (idx,row) in vocab_pairs.iterrows():
    card = Flashcard(root, row["Face1"], row["Face2"])
    root.mainloop()
