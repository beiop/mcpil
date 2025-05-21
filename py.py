import re
assetsDir = "assets/"

def custom_split(line):
    # Count leading spaces
    leading_spaces = len(line) - len(line.lstrip(' '))
    depth = leading_spaces // 4
    # Remove leading spaces
    content = line.lstrip(' ')
    # Split the rest by spaces (default split)
    words = content.split()
    # Return a list: one "word" for each depth, then the split words
    return (['    '] * depth) + words

# Example usage:
with open(f"{assetsDir}possibly-available-feature-flags", "r") as file:
    for line in file:
        words = custom_split(line.rstrip('\n'))
        print(words)