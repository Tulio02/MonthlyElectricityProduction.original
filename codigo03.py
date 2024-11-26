import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Monthly Electricity Production in GWh.csv') #Lê o arquivo CSV e carrega os dados em um DataFrame do pandas.

#Filtra o DataFrame para excluir países ou regiões agregadas que não são relevantes para a análise.
df = df[df['COUNTRY'] != 'OECD Total']  
df = df[df['COUNTRY'] != 'IEA Total']
df = df[df['COUNTRY'] != 'OECD Americas']
df = df[df['COUNTRY'] != 'OECD Europe']
df = df[df['COUNTRY'] != 'OECD Asia Oceania']

print(df)#Imprime a sumarização dos dados
anos = range(2010, 2023) #Cria um intervalo de anos de 2010 a 2022.
producao = [] #Inicializa uma lista vazia para armazenar os dados de produção por ano.


#Loop para coletar os dados de produção de energia elétrica para cada ano.
for ano in anos:
    producao_ano = df.loc[
        (df['YEAR'] == ano) & #Filtra os dados para o ano atual no loop.
        (df['COUNTRY'] == 'United States') & #Filtra para o país "United States".
        (df['yearToDate']) & #Seleciona apenas registros com valores em 'yearToDate'.
        (df['PRODUCT'] == 'Net electricity production') #Filtra para o produto 'Net electricity production'.
        
    ]
    producao.append(producao_ano['yearToDate']) #Adiciona o valor correspondente de 'yearToDate' à lista de produção.
#Cria o gráfico com os anos no eixo X e os valores de produção no eixo Y.
plt.plot(anos, producao, 'o-', color='blue') #Define o estilo do gráfico como linhas com marcadores ('o-') em azul.


plt.legend(['GERAÇÃO DE ENERGIA']) #Adiciona uma legenda para o gráfico.
plt.xlabel('ANOS') #Define o rótulo do eixo X como "ANOS".
plt.ylabel('GERAÇÃO DE ENERGIA GWh EM CADA ANO (MILHÃO)') #Define o rótulo do eixo Y.
plt.xticks(rotation=45) #Rotaciona os rótulos do eixo X em 45 graus para melhor legibilidade.
plt.grid() #Adiciona uma grade ao gráfico para facilitar a visualização.
plt.title("Produção líquida de eletricidade - EUA (2010-2022)") #Define o título do gráfico.
plt.show() #Exibe o gráfico na tela.

