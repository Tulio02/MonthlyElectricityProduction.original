import pandas as pd
import matplotlib.pyplot as plt

#Importação do arquivo CSV
df = pd.read_csv('Monthly Electricity Production in GWh.csv')

#Filtragem de dados para remover certos produtos específicos
df = df[df['PRODUCT'] != 'Electricity supplied'] #Eletricidade fornecida
df = df[df['PRODUCT'] != 'Net electricity production'] #Produção líquida de eletricidade
df = df[df['PRODUCT'] != 'Final consumption'] #Consumo final
df = df[df['PRODUCT'] != 'Non-renewables'] #Não renováveis
df = df[df['PRODUCT'] != 'Total combustible fuels'] #Total de combustíveis
df = df[df['PRODUCT'] != 'Low carbon'] #Baixo carbono
df = df[df['PRODUCT'] != 'Other renewable energies'] #Outras energias renováveis
df = df[df['PRODUCT'] != 'Total fuels'] #Combustíveis fósseis
df = df[df['PRODUCT'] != 'Renewable combustible energies'] #Energias renováveis combustíveis
df = df[df['PRODUCT'] != 'Other non-renewable combustible energies'] #Outras energias não renováveis combustíveis
df = df[df['PRODUCT'] != 'Unspecified'] #Não especificado
df = df[df['PRODUCT'] != 'Total imports'] #Total de importações
df = df[df['PRODUCT'] != 'Total exports'] #Total de exportações
df = df[df['PRODUCT'] != 'Used for pumped storage'] #Usada para armazenamento bombeado
df = df[df['PRODUCT'] != 'Distribution losses'] #Perdas de distribuição
df = df[df['PRODUCT'] != 'Electricity trade'] #Comércio de eletricidade
df = df[df['PRODUCT'] != 'Renewables'] #Renováveis
df = df[df['PRODUCT'] != 'Others'] #Outros
df = df[df['PRODUCT'] != 'Other aggregated renewables'] #Outras renováveis agregadas
df = df[df['PRODUCT'] != 'Fossil fuels'] #Combustíveis fósseis
df = df[df['PRODUCT'] != 'Other renewables aggregated'] #Outras fontes renováveis agregadas
df = df[df['PRODUCT'] != 'Combustible renewables'] #Fontes renováveis combustíveis
df = df[df['PRODUCT'] != 'Other combustible non-renewables'] #Outros combustíveis não renováveis
df = df[df['PRODUCT'] != 'Not specified'] #Não especificado
df = df[df['PRODUCT'] != 'Other renewables'] #Outras renováveis

#Filtragem dos dados de produção no período de 2010 a 2022
producao = df.loc[(df['YEAR'] >= 2010) & (df['YEAR'] <= 2022) & (df['PRODUCT'])]

#Ordenação dos dados pelo valor 'yearToDate' em ordem decrescente
ordem = producao.sort_values(by='yearToDate', ascending=False) #Ordenação
print(ordem) #Imprime os dados ordenados

#Remoção de duplicatas da coluna 'PRODUCT'
IF = ordem.drop_duplicates(subset='PRODUCT', keep='first') #Mantém apenas a primeira ocorrência de cada produto
#Imprime o DataFrame filtrado sem certas colunas
print(IF.drop(columns=['previousYearToDate', 'share', 'DISPLAY_ORDER', 'yearToDate']))

#Seleciona os índices do TOP 5 produtos
top10 = IF.index[0:5] #Pega os índices dos primeiros 5 produtos

#Impressão do TOP 5 fontes de energia mais utilizadas globalmente
print('TOP 5 FONTES ENERGÉTICAS MAIS UTILIZADAS GLOBALMENTE') #Mensagem inicial
for i in range(5): #Loop para imprimir os 5 primeiros produtos
    #Imprime a posição, o produto e a quantidade
    TOP = print(f'\n{i+1}°) {IF.iloc[i, 0]} GWh: {IF.iloc[i, 9]} {IF.iloc[i, 6]}')

#Salva o TOP 5 em um arquivo CSV
IF.to_csv('top5.csv', index=False)  # Exporta os dados para um arquivo CSV chamado 'top5.csv'

#Leitura do arquivo CSV do TOP 5
df2 = pd.read_csv('top5.csv') #Lê o arquivo CSV criado anteriormente

#Seleção dos 5 primeiros elementos do DataFrame lido
top5 = df2.loc[(df2.index[0:5])] #Seleciona os 5 primeiros elementos do DataFrame
print(top5) #Imprime os dados do TOP 5

#Criação de gráfico do TOP 5 de fontes energéticas
plt.plot(top5['PRODUCT'], top5['yearToDate'], 'o-', color='blue') #Plota o gráfico usando os dados do TOP 5
plt.legend(['TOP5']) #Define a legenda do gráfico
plt.xlabel('PAÍSES') #Define o rótulo do eixo x
plt.ylabel('GERAÇÃO DE ENERGIA GWh (Milhão)') #Define o rótulo do eixo y
plt.grid() #Adiciona a grade ao gráfico
plt.xticks(rotation=45) #Rotaciona os rótulos do eixo x em 45 graus
plt.title("TOP 5 FONTES ENERGÉTICAS MAIS UTILIZADAS GLOBALMENTE") #Define o título do gráfico
plt.show() #Mostra o gráfico na tela



