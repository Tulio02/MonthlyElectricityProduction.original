import pandas as pd
import matplotlib.pyplot as plt

#TOP 10 GERAL DOS MAIORES PRODUTORES DE ENERGIA (RENOVÁVEIS)
df = pd.read_csv('Monthly Electricity Production in GWh.csv')#Importação do arquivo
df = df[df['COUNTRY'] != 'OECD Total']#Remove os conglomerados
df = df[df['COUNTRY'] != 'IEA Total']#Remove os conglomerados
df = df[df['COUNTRY'] != 'OECD Americas']#Remove os conglomerados 
df = df[df['COUNTRY'] != 'OECD Europe']#Remove os conglomerados
df = df[df['COUNTRY'] != 'OECD Asia Oceania']#Remove os conglomerados
producao = df.loc[(df['YEAR'] >= 2010) & (df['YEAR'] <= 2022) & (df['PRODUCT'] == 'Renewables')]#Produção geral entre 2010 e 2022
ordem = producao.sort_values(by='yearToDate', ascending=False)#Ordenando em ordem decrescente em relação a yearToDate
IF = ordem.drop_duplicates(subset='COUNTRY', keep='first')#Está removendo todas as linhas duplicadas considerando apenas a coluna COUNTRY
top10 = IF.index[0:10]#Está pegando as 10 primeiras linhas geradas por IF
print('TOP 10 MAIORES PRODUTORES DE ENERGIA')#Título da tabela

for i in range(10):#Irá fazer um laço de repetição em relação aos TOP 10 Paises
    #Imprimindo os 10 países que tiveram a maior produção de energia entre os anos de 2010 até 2022 e a quantidade gerada durante o ano
    TOP = print(f'\n{i+1}°) {IF.iloc[i,0]} GWh: {IF.iloc[i,9]}  {IF.iloc[i,6]}')
IF.to_csv('top10.csv', index=False)#Criando um novo arquivo sumarizado em relação à produção de energia em csv
df2 = pd.read_csv('top10.csv')#Nome do novo arquivo
top10 = df2.loc[(df2.index[0:10])]#Está pegando as 10 primeiras linhas geradas por df2
print(top10)#É exibido os 10 países mais produtores de energia

#TOP 10 MAIORES PRODUTORES DE ENERGIA (RENOVÁVEIS)
plt.subplot(1,2,1)#Cria o primeiro subplot (gráfico) para os dados de energia renovável
plt.plot(top10['COUNTRY'],top10['yearToDate'],'o-',color='blue')#Plota o gráfico de linha com os países e sua produção acumulada
plt.legend(['TOP10'])#Legenda
plt.xlabel('PAÍSES')#Título em relação a X
plt.ylabel('GERAÇÃO DE ENERGIA GWh (Milhão)')#Título em relação a Y
plt.grid()#Adicionar uma grade no gráfico
plt.xticks(rotation=60)#Ele está inclinando as variáveis em 60°
plt.title("TOP 10 MAIORES PRODUTORES DE ENERGIA\n(RENOVÁVEIS)")#Título do gráfico

#"TOP 10 GERAL DOS MAIORES PRODUTORES DE ENERGIA (NÃO RENOVÁVEIS)"
df3 = pd.read_csv('Monthly Electricity Production in GWh.csv')#Importação do arquivo

producao2 = df3.loc[(df3['YEAR'] >= 2010) & (df['YEAR'] <= 2022) & (df3['PRODUCT'] == 'Non-renewables')]#Produção geral entre 2010 e 2022
ordem2 = producao2.sort_values(by='yearToDate', ascending=False)#Ordenando em ordem decrescente em relação a yearToDate
IF2 = ordem2.drop_duplicates(subset='COUNTRY', keep='first')#Está removendo todas as linhas duplicadas considerando apenas a coluna COUNTRY
top10_1 = IF2.index[0:10]#Está pegando as 10 primeiras linhas geradas por IF

print('TOP 10 MAIORES PRODUTORES DE ENERGIA')#Título da tabela
for i in range(10):#Imprimindo os 10 países que tiveram a maior produção de energia entre os anos de 2010 até 2022 e a quantidade gerada durante o ano
    TOP = print(f'\n{i+1}°) {IF2.iloc[i,0]} GWh: {IF2.iloc[i,9]}  {IF2.iloc[i,6]}')

IF2.to_csv('top10.csv', index=False)#Criando um novo arquivo sumarizado em relação à produção de energia em csv
df2_1 = pd.read_csv('top10.csv')#Nome do novo arquivo
top10_1 = df2_1.loc[(df2_1.index[0:10])]#Está pegando as 10 primeiras linhas geradas por df2
print(top10_1)#É exibido os 10 países mais produtores de energia

#TOP 10 GERAL DOS MAIORES PRODUTORES DE ENERGIA (NÂO RENOVÁVEIS)
plt.subplot(1, 2, 2)
plt.plot(top10_1['COUNTRY'], top10_1['yearToDate'], 'o-', color='red')
#Criando um gráfico histograma sendo os países as variáveis independentes e a geração de energia uma variável dependente
plt.legend(['TOP10'])#Legenda
plt.xlabel('PAÍSES')#Título em relação a X
plt.ylabel('GERAÇÃO DE ENERGIA GWh (Milhão)')#Título em relação a Y
plt.grid()#Adicionar uma grade no gráfico
plt.xticks(rotation=60)#Ele está inclinando as variáveis em 60°
plt.title("TOP 10 MAIORES PRODUTORES DE ENERGIA \n(NÃO-RENOVÁVEIS)")#Título do gráfico

plt.show()#Saída do gráfico






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






import pandas as pd
import matplotlib.pyplot as plt

#Carrega os dados de produção de eletricidade a partir de um arquivo CSV
df = pd.read_csv('Monthly Electricity Production in GWh.csv')

#Filtra o DataFrame para remover algumas regiões agregadas específicas
df = df[df['COUNTRY'] != 'OECD Total']
df = df[df['COUNTRY'] != 'IEA Total']
df = df[df['COUNTRY'] != 'OECD Americas']
df = df[df['COUNTRY'] != 'OECD Europe']
df = df[df['COUNTRY'] != 'OECD Asia Oceania']

#Filtra os dados para obter a produção anual de eletricidade dos EUA entre 2010 e 2022
producao_ano = df.loc[(df['YEAR'] >= 2010) & (df['YEAR'] <= 2022) & (df['COUNTRY'] 
== 'United States') & (df['yearToDate']) & (df['PRODUCT']=='Final consumption')]
print(producao_ano)  # Exibe os dados filtrados

#Agrupa os dados por ano e soma a produção anual
producao_anual = producao_ano.groupby('YEAR')['yearToDate'].sum()

#Calcula a média e o desvio padrão da produção anual
media = producao_anual.mean()
Dp = producao_anual.std()
print(f'Media em relação a produçao anual ao longo de 12 anos\n{media}')  # Exibe a média da produção anual
print(f'O desvio padrão é {Dp}')  # Exibe o desvio padrão

#Cria o primeiro gráfico com a produção anual
plt.subplot(2,2,1)
plt.plot(producao_anual.index, producao_anual.values, 'o', color='blue', label='Produção Anual')
plt.axhline(media, color='red', linestyle='--', linewidth=2, label=f'Média = {media:.2f} GWh')
plt.fill_between(producao_anual.index, media - Dp, media + Dp, color='orange', alpha=0.3, label=f'desvio padrão = {Dp:.2f} Gwh')

#Define título, rótulos e configurações do gráfico
plt.title('Consumo de Energia ao Longo do Tempo (2010-2022) - EUA', fontsize=10)
plt.xlabel('Ano', fontsize=10)
plt.ylabel('Consumo de Energia (GWh)', fontsize=10)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.legend(fontsize=6)
plt.xticks(producao_anual.index, rotation=45)
plt.tight_layout()

#Calcula o coeficiente de variação (Desvio Padrão / Média * 100)
coeficiente = (Dp/media) * 100
print(f'COEFICIENTE DE VARIAÇÃO É {coeficiente:.2f}%') #Exibe o coeficiente de variação

#Recarrega os dados do CSV e repete o processo para um período mais curto (2020-2022)
df2 = pd.read_csv('Monthly Electricity Production in GWh.csv')
producao_ano2 = df2.loc[(df2['YEAR'] >= 2020) & (df2['YEAR'] <= 2022) & (df2['COUNTRY'] 
== 'United States') & (df2['yearToDate']) & (df2['PRODUCT']=='Final consumption')]
print(producao_ano2) #Exibe os dados filtrados

#Agrupa os dados por ano e soma a produção anual (2020-2022)
producao_anual2 = producao_ano2.groupby('YEAR')['yearToDate'].sum()

#Calcula a média e o desvio padrão da produção anual (2020-2022)
media2 = producao_anual2.mean()
Dp2 = producao_anual2.std()
print(f'Media em relação a produçao anual ao longo de 12 anos\n{media2}')  # Exibe a média
print(f'O desvio padrão é {Dp2}')  # Exibe o desvio padrão

#Cria o segundo gráfico com a produção anual (2020-2022)
plt.subplot(2,2,2)
plt.plot(producao_anual2.index, producao_anual2.values, 'o', linestyle='-', color='blue', label='Produção Anual')
plt.axhline(media2, color='red', linestyle='--', linewidth=2, label=f'Média = {media2:.2f} GWh')
plt.fill_between(producao_anual2.index, media2 - Dp2, media2 + Dp2, color='orange', alpha=0.3, label=f'desvio padrão = {Dp2:.2f} Gwh')

#Calcula e exibe o coeficiente de variação (2020-2022)
coeficiente2 = (Dp2/media2) * 100
print(f'COEFICIENTE DE VARIAÇÃO É {coeficiente2:.2f}%')

#Define título, rótulos e configurações do gráfico
plt.title('Consumo de Energia ao Longo do Tempo (2010-2022) - EUA', fontsize=10)
plt.xlabel('Ano', fontsize=10)
plt.ylabel('Consumo de Energia (GWh)', fontsize=10)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.legend(fontsize=7)
plt.xticks(producao_anual2.index, rotation=45)
plt.tight_layout()

#Carrega novamente os dados do CSV e filtra a produção de eletricidade líquida (2010-2022)
df = pd.read_csv('Monthly Electricity Production in GWh.csv')
df = df[df['COUNTRY'] != 'OECD Total']
df = df[df['COUNTRY'] != 'IEA Total']
df = df[df['COUNTRY'] != 'OECD Americas']
df = df[df['COUNTRY'] != 'OECD Europe']
df = df[df['COUNTRY'] != 'OECD Asia Oceania']
producao_ano = df.loc[(df['YEAR'] >= 2010) & (df['YEAR'] <= 2022) & (df['COUNTRY'] == 'United States')
                       & (df['yearToDate']) & (df['PRODUCT']=='Net electricity production')]
print(producao_ano) #Exibe os dados filtrados

#Agrupa os dados por ano e soma a produção anual
producao_anual = producao_ano.groupby('YEAR')['yearToDate'].sum()

#Calcula a média e o desvio padrão
media = producao_anual.mean()
Dp = producao_anual.std()
print(f'Media em relação a produçao anual ao longo de 12 anos\n{media}')
print(f'O desvio padrão é {Dp}')

#Cria o terceiro gráfico com a produção anual de eletricidade líquida (2010-2022)
plt.subplot(2,2,3)
plt.plot(producao_anual.index, producao_anual.values, 'o', color='black', label='Produção Anual')
plt.axhline(media, color='red', linestyle='--', linewidth=2, label=f'Média = {media:.2f} GWh')
plt.fill_between(producao_anual.index, media - Dp, media + Dp, color='orange', alpha=0.3, label=f'desvio padrão = {Dp:.2f} Gwh')

#Define título, rótulos e configurações do gráfico
plt.title('Geração de Energia ao Longo do Tempo (2010-2022) - EUA', fontsize=10)
plt.xlabel('Ano', fontsize=10)
plt.ylabel('Geração de Energia (GWh)', fontsize=10)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.legend(fontsize=7)
plt.xticks(producao_anual.index, rotation=45)
plt.tight_layout()

#Calcula o coeficiente de variação
coeficiente = (Dp/media) * 100
print(f'COEFICIENTE DE VARIAÇÃO É {coeficiente:.2f}%')

#Carrega novamente os dados para análise do período 2020-2022
df2 = pd.read_csv('Monthly Electricity Production in GWh.csv')
producao_ano2 = df2.loc[(df2['YEAR'] >= 2020) & (df2['YEAR'] <= 2022) & (df2['COUNTRY']
== 'United States') & (df2['yearToDate']) & (df2['PRODUCT']=='Net electricity production')]
print(producao_ano2)

#Agrupa os dados por ano e soma a produção anual (2020-2022)
producao_anual2 = producao_ano2.groupby('YEAR')['yearToDate'].sum()

#Calcula a média e o desvio padrão (2020-2022)
media2 = producao_anual2.mean()
Dp2 = producao_anual2.std()
print(f'Media em relação a produçao anual ao longo de 12 anos\n{media2}')
print(f'O desvio padrão é {Dp2}')

#Cria o quarto gráfico com a produção anual de eletricidade líquida (2020-2022)
plt.subplot(2,2,4)
plt.plot(producao_anual2.index, producao_anual2.values, 'o', linestyle='-', color='black', label='Produção Anual')
plt.axhline(media2, color='red', linestyle='--', linewidth=2, label=f'Média = {media2:.2f} GWh')
plt.fill_between(producao_anual2.index, media2 - Dp2, media2 + Dp2, color='orange', alpha=0.3, label=f'desvio padrão = {Dp2:.2f} Gwh')

#Calcula e exibe o coeficiente de variação
coeficiente2 = (Dp2/media2) * 100
print(f'COEFICIENTE DE VARIAÇÃO É {coeficiente2:.2f}%')

#Define título, rótulos e configurações do gráfico
plt.title('Geração de Energia ao Longo do Tempo (2010-2022) - EUA', fontsize=10)
plt.xlabel('Ano', fontsize=10)
plt.ylabel('Geração de Energia (GWh)', fontsize=10)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.legend(fontsize=7)
plt.xticks(producao_anual2.index, rotation=45)
plt.tight_layout()

#Exibe todos os gráficos criados
plt.show()






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






import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Monthly Electricity Production in GWh.csv')#Importação do arquivo
#Produção do ano 2010
producao_2010 = df.loc[(df['YEAR'] == 2010) & (df['PRODUCT']== 'Final consumption') & (df['COUNTRY'] == 'United States')]
#Produção do ano 2011
producao_2011 = df.loc[(df['YEAR'] == 2011) & (df['PRODUCT']== 'Final consumption') & (df['COUNTRY'] == 'United States')]
#Produção do ano 2012
producao_2012 = df.loc[(df['YEAR'] == 2012) & (df['PRODUCT']== 'Final consumption') & (df['COUNTRY'] == 'United States')]
ordem = producao_2010.sort_values(by='VALUE', ascending=False)#Ordenando em ordem decrescente em relação VALUE
ordem2 = producao_2011.sort_values(by='VALUE', ascending=False)#Ordenando em ordem decrescente em relação VALUE
ordem3 = producao_2012.sort_values(by='VALUE', ascending=False)#Ordenando em ordem decrescente em relação VALUE

print(ordem)#Imprime em ordem decrescente em relação VALUE no ano de 2010
print(ordem2)#Imprime em ordem decrescente em relação VALUE no ano de 2011
print(ordem3)#Imprime em ordem decrescente em relação VALUE no ano de 2012

plt.plot(producao_2010['MONTH_NAME'],producao_2010['VALUE'],'o-',color='green')#Adiciona detalhes ao gráfico
plt.plot(producao_2011['MONTH_NAME'],producao_2011['VALUE'],'o-',color='blue')#Adiciona detalhes ao gráfico
plt.plot(producao_2012['MONTH_NAME'],producao_2012['VALUE'],'o-',color='red')#Adiciona detalhes ao gráfico

plt.legend(['2010','2011','2012'])#Legenda
plt.xlabel('MESES')#Título em relação a X
plt.ylabel('GERAÇÃO DE ENERGIA GWh (Milhão)')#Título em relação a Y
plt.grid()#Adicionar uma grade no gráfico
plt.xticks(rotation=45)#Ele está inclinado as variaveis em 45°
plt.title("CONSUMO TOTAL MENSAL DOS ESTADOS UNIDOS (2010-2012)")#Título do gráfico
plt.show()#Saída do gráfico