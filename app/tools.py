def get_population():
  keys = ['colombia', 'bolivia']
  values = [300, 400]
  return keys, values

def population_by_country(data,country):
  """
  A partir de una lista de diccionarios la cual es el parámetro data
  retorna otra lista diccionarios filtrando los diccionarios cuyo país
  es igual al parámetro country.
  """

  return list(filter(lambda nation: nation['country'].lower() == country.lower(), data))
  
