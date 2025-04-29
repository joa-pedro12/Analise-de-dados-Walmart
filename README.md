# Analise-de-dados-Walmart
Treino de analise de dados 

# Análise de Dados de Ações do Walmart

Este projeto realiza uma análise exploratória dos dados de ações do Walmart, utilizando Python com as bibliotecas Pandas, NumPy, Seaborn e Matplotlib. O objetivo é compreender o comportamento das ações ao longo do tempo.

## Bibliotecas Utilizadas

* **Pandas:** Para manipulação e análise de dados tabulares.
* **NumPy:** Para operações numéricas eficientes.
* **Seaborn:** Para visualizações estatísticas atraentes.
* **Matplotlib:** Para criação de gráficos e visualizações.

## Dados

O conjunto de dados utilizado é `wmt_data.csv`, que contém informações sobre as ações do Walmart. As colunas incluem:

* `date`: Data da observação.
* `open`: Preço de abertura da ação.
* `high`: Preço máximo da ação no dia.
* `low`: Preço mínimo da ação no dia.
* `close`: Preço de fechamento da ação no dia.
* `adj_close`: Preço de fechamento ajustado.
* `volume`: Volume de ações negociadas.

O dataset pode ser encontrado no seguinte caminho: `/kaggle/input/walmart-stock-data-2025/wmt_data.csv`

## Análise Realizada

1.  **Importação de Bibliotecas:** As bibliotecas necessárias (Pandas, NumPy, Seaborn, Matplotlib) foram importadas.
2.  **Leitura dos Dados:** O conjunto de dados foi carregado em um DataFrame do Pandas.
3.  **Exploração Inicial:**
    * Exibição das primeiras e últimas linhas do DataFrame.
    * Verificação das informações gerais do DataFrame (tipos de dados, quantidade de linhas e colunas, etc.).
4.  **Tratamento dos Dados:**
    * Verificação da quantidade de linhas e colunas.
    * Verificação dos tipos de dados de cada coluna.
    * Verificação de valores nulos.
    * Verificação de valores duplicados.
    * Verificação da quantidade de valores únicos em cada coluna.
    * Conversão da coluna `date` para o tipo datetime.
5.  **Análise Descritiva:**
    * Cálculo de estatísticas descritivas para as colunas numéricas (média, desvio padrão, mínimo, máximo, quartis, etc.).
6.  **Análise de Correlação:**
    * Cálculo da matriz de correlação entre as colunas `open`, `high`, `low`, `close` e `volume`.
    * Visualização da matriz de correlação usando um heatmap do Seaborn.

## Visualizações

* **Heatmap de Correlação:** Um heatmap foi gerado para visualizar a correlação entre as diferentes variáveis.

## Como Executar o Código

O código está em um notebook Jupyter (`treino-de-analise-walmart.ipynb`). Para executá-lo, você precisa ter o Jupyter Notebook ou JupyterLab instalado, juntamente com as bibliotecas listadas acima.

1.  Clone o repositório ou baixe o notebook.
2.  Certifique-se de que o dataset `wmt_data.csv` está no caminho especificado no notebook ou ajuste o caminho se necessário.
3.  Abra o notebook no Jupyter.
4.  Execute as células do notebook sequencialmente.

## Resultados

Os resultados da análise incluem:

* Informações sobre a estrutura e os tipos de dados do dataset.
* Estatísticas descritivas das variáveis.
* Visualização da correlação entre as variáveis numéricas.

Esses resultados fornecem uma visão geral dos dados e podem ser usados como base para análises mais aprofundadas ou modelagem preditiva.

## Autor

JOÃO PEDRO DE SOUSA CABRAL 
