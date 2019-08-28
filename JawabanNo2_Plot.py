### Soal 2 : Infografis ASEAN

import mysql.connector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

## Connecting to MySQL

dbku = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user= 'root',
    passwd='gr00vym0nkey',
    database='world'
)

kursor = dbku.cursor()

query1 = '''SELECT co.Name as Negara_ASEAN, co.Population as Populasi_Negara
FROM country co
JOIN city ci
ON ci.ID=co.Capital
WHERE ID = 939
or ID = 538
or ID = 1800
or ID = 1522
or ID = 2432
or ID = 2464
or ID = 2710
or ID = 766
or ID = 3208
or ID = 3320
or ID = 3770
ORDER BY Negara_ASEAN'''

#Create DataFrame for Plots
df = pd.read_sql(query1, con=dbku)
neg = list(df['Negara_ASEAN'])
pop = list(df['Populasi_Negara'])

### No 1. Populasi ASEAN ####
### Negara vs Populasi ###

x = neg
y = pop

# plt.bar(x, y, 
# color=['red','green','yellow','aqua','blue','lightblue','lightgreen','pink','magenta','purple','orange'])

# for a,b in zip(x, y):
#     plt.text(a, b, str(b), ha='center',size=5.7)
# plt.grid(True)
# plt.title('Populasi Negara ASEAN')
# plt.xlabel('Negara')
# plt.ylabel('Populasi (x100jt jiwa)')
# plt.xticks(rotation=45, size=7)
# plt.yticks(size=8)

# plt.show()


### No. 2 : Persentase Penduduk ASEAN
### Using Pie Chart

# color = [
#     'darkblue', 'khaki', 'green', 'crimson', 'goldenrod',
#     'cyan', 'orchid', 'navy', 'purple', 'yellow', 'lightgreen'
#     ]

# plt.pie(
#     y, labels=x, colors=color, counterclock=False,
#     startangle=180, shadow=True,
#     autopct='%1.1f%%',
#     textprops={'color':'black', 'size': 7}
#     )

# plt.title('Populasi Negara ASEAN')
# plt.show()


### No. 3 : Gross National Product in ASEAN
### Negara vs GNP

## Stating Query
query2 = '''SELECT co.Name as Negara_ASEAN, GNP
FROM country co
JOIN city ci
ON ci.ID=co.Capital
WHERE ID = 939
or ID = 538
or ID = 1800
or ID = 1522
or ID = 2432
or ID = 2464
or ID = 2710
or ID = 766
or ID = 3208
or ID = 3320
or ID = 3770
ORDER BY Negara_ASEAN'''

#Create DataFrame Containing Datas to be Plotted
df2 = pd.read_sql(query2, con=dbku)

neg2 = list(df2['Negara_ASEAN'])
gnp = list(df2.GNP)

#Plotting in Bars
color2 = [
    'orchid', 'khaki', 'purple', 'yellow', 'lightgreen', 'darkblue', 'coral', 'green', 'crimson', 'goldenrod',
    'indigo', 
    ]

# x = neg2
# y = gnp

# plt.bar(x, y, 
# color=color2)

# for a,b in zip(x, y):
#     plt.text(a, b, str(b), ha='center',size=5.7)
# plt.grid(True)
# plt.title('Populasi Negara ASEAN')
# plt.xlabel('Negara')
# plt.ylabel('GNP')
# plt.xticks(rotation=45, size=7)
# plt.yticks(size=8)

# plt.show()

### Soal 4 : Persentase Luas Dataran ASEAN
### In Percentage, Piechart

query3 = '''SELECT co.Name as Negara_ASEAN, co.SurfaceArea as LuasDaratan
FROM country co
JOIN city ci
ON ci.ID=co.Capital
WHERE ID = 939
or ID = 538
or ID = 1800
or ID = 1522
or ID = 2432
or ID = 2464
or ID = 2710
or ID = 766
or ID = 3208
or ID = 3320
or ID = 3770
ORDER BY Negara_ASEAN'''

# Create DataFrame and Preparing datas to be plotted
df3 = pd.read_sql(query3, con=dbku)
neg3 = list(df3['Negara_ASEAN'])
luas = list(df3.LuasDaratan)

# Plotting in PieChart
y = luas
x = neg3

color=['chocolate','navy','goldenrod','teal','indigo','lightblue','maroon','lime','goldenrod','olive','tomato']
#teal
plt.pie(
    y, labels=x, colors=color, counterclock=False,
    startangle=180, shadow=True,
    autopct='%1.1f%%',
    textprops={'color':'black', 'size': 7}
    )

plt.title('Persentase Luas Daratan ASEAN')
plt.show()