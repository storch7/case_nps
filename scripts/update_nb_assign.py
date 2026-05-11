import nbformat as nbf

with open('../notebooks/extracao.ipynb', 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

code_assign = """\
# Atribuir o tópico predominante para cada comentário e adicionar ao DataFrame
from topic_extractor import assign_topics

df['Dominant_Topic'] = assign_topics(df['Comment'].tolist(), num_topics=3, num_words=4)

display(df[['Comment', 'Sentiment', 'Dominant_Topic']].head(10))

# Para salvar o dataframe de volta no arquivo original:
# df.to_excel('../data/NPS_tratado.xlsx', index=False)
"""

nb.cells.append(nbf.v4.new_code_cell(code_assign))

with open('../notebooks/extracao.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
