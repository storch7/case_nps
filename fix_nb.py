import nbformat as nbf

with open('extracao.ipynb', 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

new_source = """\
# Atribuir o tópico predominante para cada comentário e adicionar ao DataFrame
# Recarregando o módulo para garantir que as novas funções sejam detectadas pelo Jupyter
import importlib
import topic_extractor
importlib.reload(topic_extractor)
from topic_extractor import assign_topics

df['Dominant_Topic'] = assign_topics(df['Comment'].tolist(), num_topics=3, num_words=4)

display(df[['Comment', 'Sentiment', 'Dominant_Topic']].head(10))

# Para salvar o dataframe de volta no arquivo original:
# df.to_excel('NPS.xlsx', index=False)
"""

nb.cells[-1].source = new_source

with open('extracao.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
