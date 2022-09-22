import pandas as pd

df = pd.read_csv('dataAnalysisWithPandas\dataSet\Gapminder.csv', on_bad_lines='skip', sep=';')

df.rename(columns = {'country':'pais', 'continent': 'continente', 'year': 'ano', 'lifeExp': 'expectativa de vida', 'pop': 'populacao total', 'gdpPercap': 'pib' }, inplace = True)

df = df.rename(columns=lambda x: x.upper())

print(df.head(10))