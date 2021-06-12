# input: string of characters
# output: list of tokens
def tokenization(text):
    text_without_whitespaces_on_any_side = text.strip()
    list_of_tokens = text_without_whitespaces_on_any_side.split(" ")
    return list_of_tokens
