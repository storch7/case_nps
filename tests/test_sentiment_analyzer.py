import pytest
from src.sentiment_analyzer import get_sentiment

def test_get_sentiment_positive():
    text = "The product is amazing and I love it!"
    polarity, classification = get_sentiment(text)
    assert polarity > 0.0
    assert classification == 'Positive'

def test_get_sentiment_negative():
    text = "This is the worst experience I have ever had, terrible service."
    polarity, classification = get_sentiment(text)
    assert polarity < 0.0
    assert classification == 'Negative'

def test_get_sentiment_neutral():
    text = "I received the package today."
    polarity, classification = get_sentiment(text)
    assert classification == 'Neutral'

def test_get_sentiment_empty():
    text = ""
    polarity, classification = get_sentiment(text)
    assert polarity == 0.0
    assert classification == 'Neutral'
    
def test_get_sentiment_none():
    text = None
    polarity, classification = get_sentiment(text)
    assert polarity == 0.0
    assert classification == 'Neutral'
