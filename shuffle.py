import string
import random

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ., 1234567890-!{}"
tmp_alphabet = list(alphabet)
random.shuffle(tmp_alphabet, lambda: 0.97444187175646646) # Shuffle the list into random order (but the same order every time)
shuffled_alphabet = ''.join(tmp_alphabet)
print(shuffled_alphabet)
shuffleit = string.maketrans(alphabet,shuffled_alphabet)
print(shuffleit)