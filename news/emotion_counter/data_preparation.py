from .remove_special_characters import remove_special_characters
from .tokenization import tokenization
from .remove_stopwords import remove_stopwords


# input: string of characters
# output: list of tokens without special characters and stopwords
def prepared_data(text):
    text_without_special_characters = remove_special_characters(text)
    tokenized_text_without_special_characters = tokenization(text_without_special_characters)
    tokenized_text_without_special_characters_and_stopwords = remove_stopwords(tokenized_text_without_special_characters)
    return tokenized_text_without_special_characters_and_stopwords