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
