from googletrans import Translator
from google_trans_new import google_translator


def LanguageConversionGT(content):
    translatorGT = Translator()
    return (translatorGT.translate(content)).text


def LanguageConversionGTN(content):
    translatorGTN = google_translator()
    return translatorGTN.translate(content, lang_tgt='en')


def ArticleConversion(nepali_article):
    english_article = LanguageConversionGTN(nepali_article)
    return english_article
