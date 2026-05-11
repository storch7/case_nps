import nbformat as nbf

# Ler o notebook existente
with open('../notebooks/extracao.ipynb', 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

# Criar nova célula com a extração de tópicos
code_topic = """\
# Extração do tema principal usando scikit-learn (LDA)
from topic_extractor import extract_topics

print("Extraindo os 3 principais temas abordados nos comentários:\\n")
comments_list = df['Comment'].tolist()
temas = extract_topics(comments_list, num_topics=3, num_words=4)

for tema in temas:
    print(tema)
"""

# Adicionar a célula ao notebook
nb.cells.append(nbf.v4.new_code_cell(code_topic))

# Salvar o notebook atualizado
with open('../notebooks/extracao.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
