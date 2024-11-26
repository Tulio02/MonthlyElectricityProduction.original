import pandas as pd
import matplotlib.pyplot as plt

#Lê um arquivo CSV contendo dados de produção mensal de eletricidade em GWh
df = pd.read_csv('Monthly Electricity Production in GWh.csv')

#Remove dados de países e regiões agregadas que não são relevantes para a análise
df = df[df['COUNTRY'] != 'OECD Total']
df = df[df['COUNTRY'] != 'IEA Total']
df = df[df['COUNTRY'] != 'OECD Americas']
df = df[df['COUNTRY'] != 'OECD Europe']
df = df[df['COUNTRY'] != 'OECD Asia Oceania']

#Filtra os dados para obter apenas a produção líquida de eletricidade no período de 2010 a 2022
producao = df.loc[(df['YEAR'] >= 2010) & (df['YEAR'] <= 2022) & (df['PRODUCT'] == 'Net electricity production')]

#Ordena os dados por produção acumulada no ano ('yearToDate') em ordem decrescente
ordem = producao.sort_values(by='yearToDate', ascending=False)

#Remove duplicatas, mantendo apenas a maior produção para cada país
IF = ordem.drop_duplicates(subset='COUNTRY', keep='first')
print(IF) #Exibe o DataFrame resultante com os maiores produtores de cada país

#Define os índices dos 10 maiores produtores de energia
top10 = IF.index[0:10]

#Exibe o TOP 10 dos maiores produtores de energia no console
print('TOP 10 DOS MAIORES PRODUTORES DE ENERGIA')
for i in range(10): #Itera sobre os 10 primeiros índices
    #Dá formatação para o terminal evitando que fique tudo em uma linha
    TOP = print(f'\n{i+1}°) {IF.iloc[i,0]} Ghw: {IF.iloc[i,9]} {IF.iloc[i,6]}')

#Salva os dados do TOP 10 em um arquivo CSV chamado 'top10.csv'
IF.to_csv('top10.csv', index=False)

#Lê o arquivo CSV gerado contendo os dados do TOP 10
df2 = pd.read_csv('top10.csv')

#Filtra novamente para selecionar os 10 maiores produtores
top10 = df2.loc[(df2.index[0:10])]

plt.plot(top10['COUNTRY'], top10['yearToDate'], 'o-', color='blue') #Cria a linha e os marcadores
plt.legend(['TOP10']) #Adiciona legenda
plt.xlabel('PAÍSES') #Define o rótulo do eixo X
plt.ylabel('GERAÇÃO DE ENERGIA GWh (Milhão)') #Define o rótulo do eixo Y
plt.grid() #Adiciona uma grade ao gráfico
plt.xticks(rotation=60) #Rotaciona os rótulos do eixo X para melhor visualização
plt.title("TOP 10 DOS MAIORES PRODUÇAO LÍQUIDA DE ELETRICIDADE") #Define o título do gráfico
plt.show() #Exibe o gráfico