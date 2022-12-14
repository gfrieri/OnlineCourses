import numpy as np

data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])

mean = np.mean(data)
sd = np.std(data)
x = (mean-sd)
y = (mean+sd)

osdc = 0
for n in data:
    if (n >= x) & (n <= y):
        osdc = osdc + 1

perc = (osdc/data.size)*100
print('Porcentaje de valores a una desviación estandar de la media:', perc)