from textblob import TextBlob

def get_sentiment(text: str) -> tuple[float, str]:
    """
    Analisa o sentimento de um texto utilizando TextBlob.
    
    Args:
        text (str): O texto a ser analisado.
        
    Returns:
        tuple[float, str]: Uma tupla contendo:
            - polarity (float): Um valor entre -1.0 (muito negativo) e 1.0 (muito positivo).
            - classification (str): 'Positive', 'Neutral' ou 'Negative'.
    """
    if not text or not isinstance(text, str):
        return 0.0, 'Neutral'
        
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0.05:
        classification = 'Positive'
    elif polarity < -0.05:
        classification = 'Negative'
    else:
        classification = 'Neutral'
        
    return polarity, classification