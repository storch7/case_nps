import pytest
from topic_extractor import extract_topics, assign_topics

def test_extract_topics_valid_texts():
    texts = [
        "The performance of the product is amazing.",
        "Performance degraded over time.",
        "System performance needs improvement.",
        "Customer support was very helpful and responsive.",
        "The support team is great.",
        "I need help from support."
    ]
    topics = extract_topics(texts, num_topics=2, num_words=3)
    
    assert len(topics) == 2
    topics_str = " ".join(topics).lower()
    
    assert "performance" in topics_str or "support" in topics_str

def test_assign_topics_valid_texts():
    texts = [
        "The performance of the product is amazing.",
        "Customer support was very helpful and responsive.",
        ""
    ]
    assigned = assign_topics(texts, num_topics=2, num_words=3)
    
    assert len(assigned) == 3
    assert assigned[2] == "Sem Tópico (Texto Vazio)"
    assert "Tópico" in assigned[0]
