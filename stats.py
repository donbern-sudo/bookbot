#Module for Stat Utility 

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
