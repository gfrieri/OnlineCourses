#Archivo con el que trabajé porque sololearn no tiene ventan de output ni da el csv para que lo descargues
import pandas as pd

df = pd.read_csv("covid19cases_test.csv")

df.set_index('date', inplace=True)
df['ratio'] = df['deaths']/df['cases']
print(df[df['ratio'] == df['ratio'].max()])

'''
Respuesta en sololearn

import pandas as pd

df = pd.read_csv("/usercode/files/ca-covid.csv")

df.drop('state', axis=1, inplace=True)
df.set_index('date', inplace=True)

df['ratio'] = df['deaths']/df['cases']
print(df[df['ratio'] == df['ratio'].max()])
'''