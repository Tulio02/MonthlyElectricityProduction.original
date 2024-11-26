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