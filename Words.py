import pandas as pd
import numpy as np

#Loadn parquet
numdata = pd.read_parquet("word_search_numdata.parquet")

# Extract columns into NumPy arrays
words_list = numdata["Nvalue"].to_numpy()
relevance_scores = numdata["relevance"].to_numpy()

alphabet = {}

for i in range(1, 27):
    letter = chr(64 + i)
    alphabet[letter] = i

print(alphabet)
word_list = []
input_values = []
relevance_scores = []
q = 0
while q<5:
    word = input("Enter a word: ") .strip().upper()
     # Reject empty words and nonalphabetic characters
    if not word or not word.isalpha() or not word.isascii():
        print("Please enter a word using A-Z only.")
        continue
    q+=1
    Nvalue = [alphabet[letter] for letter in word]
    words_list.append(word)
    input_values.append(Nvalue)
    relevance_scores.append(0)  # Append a default relevance score for the new word 
    print(word)
    print(Nvalue)
    print("Words in dataset:", len(words_list))
    print("Relevance scores:", len(relevance_scores))

