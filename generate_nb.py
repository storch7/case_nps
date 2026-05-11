import nbformat as nbf

nb = nbf.v4.new_notebook()

nb['cells'] = [
    nbf.v4.new_markdown_cell('# Análise de Sentimento\nEste notebook aplica o módulo `sentiment_analyzer` na base de comentários do arquivo `NPS.xlsx`.'),
    nbf.v4.new_code_cell('import pandas as pd\nfrom sentiment_analyzer import get_sentiment'),
    nbf.v4.new_code_cell("# Carregar a base de dados\ndf = pd.read_excel('NPS.xlsx', keep_default_na=False)\ndf.head(3)"),
    nbf.v4.new_code_cell("# Aplicar a análise de sentimento na coluna 'Comment'\n# Como get_sentiment retorna uma tupla (polaridade, classificação), vamos desempacotar o resultado em duas colunas.\ndf[['Polarity', 'Sentiment']] = df['Comment'].apply(lambda x: pd.Series(get_sentiment(str(x))))"),
    nbf.v4.new_code_cell("# Visualizar as primeiras linhas atualizadas e o resumo dos sentimentos\ndisplay(df.head())\nprint('\\nDistribuição dos Sentimentos:')\nprint(df['Sentiment'].value_counts())")
]

with open('extracao.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
