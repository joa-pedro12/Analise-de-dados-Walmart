import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 

# carregando os dados 
df = pd.read_csv('wmt_data.csv')


print(df.head().to_string())
print("\n ultimos: ",df.tail().to_string())

print("\n informação: \n")
df.info()
#tratameto dos dados 
print("\n Quantidade de linhas e colunas: \n",df.shape)
print("\n Tipos de dados: \n ", df.dtypes)
print("\n Verificando valores nulos: \n ",df.isnull().sum())
print("\n Verificnado os valores duplicados : \n ", df.duplicated().sum())
print("\n Dados unicos: \n ", df.nunique())

df['date'] = pd.to_datetime(df['date'], utc = True)

# Estatistica resumidas 
print("\n descrição dos dados: \n")
print(df.describe())


# visualização de dados

plt.figure(figsize=(14, 6))
plt.plot(df['date'], df['close'], label='Closing Price', color='blue')
plt.title('Walmart Stock Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.legend()
plt.grid(True)
plt.show()  


plt.figure(figsize=(14, 6))
plt.plot(df['date'], df['volume'], label='volume', color='green')
plt.title('Number of shares traded that year')
plt.xlabel('Date')
plt.ylabel('Quantity')
plt.legend()
plt.grid(True)
plt.show()  

corr = df[['open', 'high', 'low', 'close', 'volume']].corr()
plt.figure(figsize =(8, 6) )
sns.heatmap(corr, annot = True, cmap='YlGnBu',fmt='.2f',linewidths=0.5)
plt.title('Correlation of Features')
plt.show()
