import read_csv as rd
import charts

def select_country(countries, country):
  """
  Select the country we want to plot it as dict
  """
  selected_country = filter(lambda item: item['Country/Territory'].lower() == country.lower(), countries)
  selected_country = list(selected_country)[0]
  
  return selected_country

def populations_country(country):
  """
  filter the population by year columns of one dict
  """
  populations = {year[:4]:population for (year,population) in country.items() if 'Population' in year and year[:4].isnumeric()}
  return populations

def plot_country(populations, country):
  selected_country = select_country(populations, country)
  populations_by_year = populations_country(selected_country)
  labels = list(populations_by_year.keys())[::-1]
  values = list(populations_by_year.values())[::-1]
  charts.generate_bar_chart(country,labels,values)

def run():

  print("Type the country to plot")
  country = input("> ")
  path = './population.csv'
  population = rd.read_csv_uno(path)
  plot_country(population, country)

if __name__ == '__main__':

  run()



  