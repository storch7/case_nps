from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np

def extract_topics(texts: list[str], num_topics: int = 1, num_words: int = 5) -> list[str]:
    """
    Extrai os tópicos principais de uma lista de textos utilizando o modelo LDA do Scikit-Learn.
    """
    valid_texts = [str(text) for text in texts if text and str(text).strip()]
    
    if not valid_texts:
        return ["Nenhum tópico encontrado (textos vazios)."]

    vectorizer = CountVectorizer(stop_words='english', lowercase=True)
    
    try:
        dtm = vectorizer.fit_transform(valid_texts)
    except ValueError:
        return ["Nenhum tópico encontrado (apenas stop words)."]

    lda_model = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda_model.fit(dtm)
    
    feature_names = vectorizer.get_feature_names_out()
    topics_output = []
    
    for topic_idx, topic in enumerate(lda_model.components_):
        top_features_ind = topic.argsort()[:-num_words - 1:-1]
        top_features = [feature_names[i] for i in top_features_ind]
        topic_str = f"Tópico {topic_idx + 1}: " + ", ".join(top_features)
        topics_output.append(topic_str)
        
    return topics_output

def assign_topics(texts: list[str], num_topics: int = 3, num_words: int = 4) -> list[str]:
    """
    Atribui o tópico predominante a cada texto individual da lista.
    """
    vectorizer = CountVectorizer(stop_words='english', lowercase=True)
    
    cleaned_texts = [str(text) if text and str(text).strip() else "empty_text_placeholder" for text in texts]
    
    try:
        dtm = vectorizer.fit_transform(cleaned_texts)
    except ValueError:
        return ["Nenhum tópico (apenas stop words)"] * len(texts)

    actual_num_topics = min(num_topics, dtm.shape[1] if dtm.shape[1] > 0 else 1)
    
    lda_model = LatentDirichletAllocation(n_components=actual_num_topics, random_state=42)
    topic_distributions = lda_model.fit_transform(dtm)
    
    feature_names = vectorizer.get_feature_names_out()
    topic_strings = []
    
    for topic_idx, topic in enumerate(lda_model.components_):
        num_features = min(num_words, len(feature_names))
        top_features_ind = topic.argsort()[:-num_features - 1:-1]
        top_features = [feature_names[i] for i in top_features_ind]
        topic_strings.append(f"Tópico {topic_idx + 1}: " + ", ".join(top_features))

    assigned_topics = []
    for i, dist in enumerate(topic_distributions):
        if cleaned_texts[i] == "empty_text_placeholder":
             assigned_topics.append("Sem Tópico (Texto Vazio)")
        else:
             dominant_topic_idx = np.argmax(dist)
             assigned_topics.append(topic_strings[dominant_topic_idx])
             
    return assigned_topics
