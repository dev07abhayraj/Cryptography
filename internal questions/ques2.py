
# 2. Write a Python code to create a word dictionary using the alphabet 'a', 'b', 'c', 'd' with a length of 5?

import itertools

# Define the alphabet and word length
alphabet = 'abcd'
word_length = 5

# Use itertools.product to generate all combinations
combinations = itertools.product(alphabet, repeat=word_length)

# Create the word dictionary
word_dict = {''.join(combination): None for combination in combinations}

# Optionally, if you need the dictionary to hold some values, you can initialize it differently, e.g., with a count or some default value
# word_dict = {''.join(combination): 0 for combination in combinations}

# Print the number of words in the dictionary to verify
print(f"Number of words in the dictionary: {len(word_dict)}")

# Print the first 10 words as a sample
for i, word in enumerate(word_dict):
    if i < 10:
        print(word)
    else:
        break
  