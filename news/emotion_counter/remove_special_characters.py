import re


# input: string of characters
# output: string of characters without special characters
def remove_special_characters(text):
    new_text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return new_text
