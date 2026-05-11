import pandas as pd
from sentiment_analyzer import get_sentiment
from topic_extractor import assign_topics

print("Lendo NPS.xlsx...")
df = pd.read_excel('NPS.xlsx', keep_default_na=False)

print("Processando Análise de Sentimento...")
# Reaplica o sentimento para garantir que a base salva tenha todas as colunas
df[['Polarity', 'Sentiment']] = df['Comment'].apply(lambda x: pd.Series(get_sentiment(str(x))))

print("Processando Modelagem de Tópicos (LDA)...")
comments_list = df['Comment'].tolist()
assigned_topics = assign_topics(comments_list, num_topics=3, num_words=4)

# Adiciona a nova coluna no DataFrame
df['Dominant_Topic'] = assigned_topics

print("Salvando no arquivo NPS.xlsx original...")
df.to_excel('NPS.xlsx', index=False)

print("Processo concluído com sucesso!")
