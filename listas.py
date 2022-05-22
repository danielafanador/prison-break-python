from helper import *

index = 0
url = str('https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes')
data = data_from_url(url)
years = []
frequency = {}
attempts_per_year = {}
attempts_per_year_list = []
attempts_per_year_values = []

for row in data[0:47]:
    data[index] = fetch_year(row[0])
    years.append(data[0])

#Imprimir todos los años en su orden original
print ('==TODOS LOS AÑOS EN SU ORDEN ORIGINAL==')
print (' ')
print (years[0:47])
print (' ')

#Imprimir cuántos valores únicos existen
print ('==VALORES ÚNICOS==')
print (' ')
print (len(years))
print (' ')

for year in years:
    if year in frequency:
        frequency[year] += 1
    else: 
        frequency[year] = 1

#Imprimir cuántas veces aparece cada año
print ('==DICCIONARIO CON CADA AÑO Y NÚMERO DE REPETICIONES==')
print (' ')
print (frequency)
print (' ')
print ('==AÑOS ÚNICOS==')
print (' ')
print (len(frequency))
print (' ')

#Extrear todos los años únicos en una lista (antes diccionario)
print ('==Lista con todos los años únicos==')
print (' ')
attempts_per_year_list = list (frequency)
print (' ')
print (attempts_per_year_list)
print (' ')

#Extraer todos los valores en una lista (de un diccionario)
print ('==Lista con los valores dentro de la lista==')
print (' ')
attempts_per_year_values = list (frequency.values())
print (' ')
print (attempts_per_year_values)
