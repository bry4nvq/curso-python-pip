import csv

#la manera que sabia antes

def read_csv_uno(path):
  list = []
  with open(path, 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    header = next(reader)
    for row in reader:
      dict = {}
      dict['Rank'] = row[0]
      dict['CCA3'] = row[1]
      dict['Country/Territory'] = row[2]
      dict['Capital'] = row[3]
      dict['Continent'] = row[4]
      dict['2022_Population'] = int(row[5])
      dict['2020_Population'] = int(row[6])
      dict['2015_Population'] = int(row[7])
      dict['2010_Population'] = int(row[8])
      dict['2000_Population'] = int(row[9])
      dict['1990_Population'] = int(row[10])
      dict['1980_Population'] = int(row[11])
      dict['1970_Population'] = int(row[12])
      dict['Area_km_cuadrados'] = float(row[13])
      dict['Density/km_cuadrado'] = float(row[14])
      dict['Growth_Rate'] = float(row[15])
      dict['World_Population_%'] = float(row[16])
      list.append(dict)
  return list

#la manera de platzi, esta manera es mucho más simple, usando la
#función zip se logra crear un diccionario de manera mucho más sencilla

def read_csv(path):
  with open(path, 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    headers = next(reader)
    list = []
    for row in reader:
      iterable = zip(headers, row)
      #dict = {header:item for header, item in iterable}
      list.append(dict(iterable))

  return list
    
if __name__ == '__main__':
  path = './population.csv'
  population = read_csv(path)
  #print(population)
  


      
      
  