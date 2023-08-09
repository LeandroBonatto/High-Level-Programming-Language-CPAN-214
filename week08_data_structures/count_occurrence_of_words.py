def process_text(text_, word_counts_):
    text_ = replace_punctuation(text_)  # Replace punctuation with space
    words = text_.split()  # Get words from each line
    for word in words:
        if word in word_counts_:
            word_counts_[word] += 1  # Increase count for word
        else:
            word_counts_[word] = 1  # Add an item in the dictionary

# Replace punctuation in the line with space
def replace_punctuation(text_):
    for ch in text_:
        if ch in '~@#$%^&*()_-+=~<>?/,.;:!{}[]|\'\"':
            text_ = text_.replace(ch, ' ')

    return text_

# Prompt the user to enter a file
text = input('Enter a text: ')

word_counts = {}  # Create an empty dictionary to count words
process_text(text.lower(), word_counts)

pairs = list(word_counts.items())  # Get pairs from the dictionary

items = [[count, word] for (word, count) in pairs]
items.sort(reverse=True)  # Sort pairs in items

for count, word in items[:10]:  # Slice the first 10 items
    print(word, count, sep='\t')

# Count each word in the line
