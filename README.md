# Análise de Sentimentos e Modelagem de Tópicos - NPS

Este projeto realiza a extração e o processamento de comentários de uma pesquisa de NPS (Net Promoter Score), aplicando técnicas de Processamento de Linguagem Natural (NLP) para analisar o sentimento dos clientes e extrair automaticamente os principais temas abordados.

## Bibliotecas Utilizadas

As principais bibliotecas que tornaram essa automação possível foram:

- **[Pandas](https://pandas.pydata.org/):** Estruturação, manipulação de dados e I/O de arquivos Excel.
- **[TextBlob](https://textblob.readthedocs.io/):** Biblioteca de processamento de linguagem natural focada em extração de características do texto (Polaridade).
- **[Scikit-learn](https://scikit-learn.org/):** Biblioteca de Machine Learning utilizada para a extração não-supervisionada de tópicos através do algoritmo LDA (Latent Dirichlet Allocation).
- **[nbformat](https://nbformat.readthedocs.io/):** Geração e manipulação programática de arquivos Jupyter Notebook.
- **[Pytest](https://docs.pytest.org/):** Framework utilizado para criação de testes automatizados e validação de regras de negócio.

## Onde e Como Foram Aplicadas

- **Análise de Sentimentos (`src/sentiment_analyzer.py`):**
  O **TextBlob** foi utilizado para avaliar semanticamente cada comentário da base. A biblioteca calcula a *polaridade* do texto e, a partir desse valor, o código aplica uma regra de negócio para classificar a resposta em `Positive` (polaridade > 0), `Negative` (polaridade < 0) ou `Neutral`.

- **Modelagem de Tópicos (`src/topic_extractor.py`):**
  O módulo de NLP e Machine Learning do **Scikit-learn** foi aplicado em duas etapas: primeiro o texto é vetorizado (`CountVectorizer`), criando uma matriz de ocorrência de palavras. Depois, o modelo LDA identifica agrupamentos latentes de palavras, definindo temas e calculando a probabilidade matemática de um comentário pertencer a cada tema, permitindo extrair o *Tópico Dominante*.

- **Pipeline de Manipulação (`src/main.py`):**
  A biblioteca **Pandas** orquestra todo o fluxo, lendo os dados brutos (`data/NPS.xlsx`), iterando as análises através da função `.apply()`, processando milhares de registros de forma otimizada, e gerando um novo DataFrame estruturado que é exportado para o arquivo final (`data/NPS_tratado.xlsx`).

- **Geração de Notebooks (`scripts/`):**
  Utilizando **nbformat**, os scripts (como `generate_nb.py` e `update_nb.py`) constroem de forma automatizada o caderno Jupyter de exploração (`notebooks/extracao.ipynb`), preenchendo células em Markdown e injetando códigos de importação dos módulos da pasta `src`.

- **Testes Unitários (`tests/`):**
  O **Pytest** foi aplicado para construir cenários que garantem a confiabilidade da nossa esteira: verificando como o código lida com comentários vazios, objetos `None` e se as classificações matemáticas convergem para o resultado esperado.

## Resultados Obtidos

Ao final da execução da pipeline (rodando o `src/main.py`), a empresa alcança os seguintes resultados:

1. **Dados Prontos para Tomada de Decisão:** 
   O output gerado (`NPS_tratado.xlsx`) ganha contexto de inteligência artificial sem a necessidade de leitura humana, trazendo novas colunas:
   - `Polarity` e `Sentiment`: Permitem gerar indicadores numéricos de satisfação da base.
   - `Dominant_Topic`: Entrega aos gestores um mapeamento claro e automático sobre *quais assuntos* estão impactando positiva ou negativamente a nota do NPS.

2. **Repositório Profissional e Escalável:**
   Ao seguir as boas práticas de desenvolvimento de software (Clean Code e separação de responsabilidades), o projeto agora possui uma estrutura lógica com `data/`, `src/`, `tests/` e `scripts/`, tornando futuras manutenções e o trabalho em equipe muito mais fácil.
