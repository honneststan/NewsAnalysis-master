from textblob import TextBlob


def textblob_sentiment_analyzer(sentiment_text):
    blob_value = TextBlob(sentiment_text)
    if blob_value.sentiment.polarity > 0:
        polarity = "Positive statement"
    elif blob_value.sentiment.polarity < 0:
        polarity = "Negative statement"
    else:
        polarity = "Neutral vibe"
    return polarity
