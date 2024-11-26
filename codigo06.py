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