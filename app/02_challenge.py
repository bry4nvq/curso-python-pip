import read_csv as rd
import charts

def countries_population_ratio(population, continent):

  countries_ratio = {country['Country/Territory']:country['World_Population_%'] for country in population if country['Continent'].lower() == continent.lower()}
  labels = list(countries_ratio.keys())
  values = list(countries_ratio.values())

  return labels, values

def plot_pie_chat(population,continent):

  labels, values = countries_population_ratio(population, continent)
  charts.generate_pie_chart(continent, labels, values)

def run():
  path = './population.csv'
  population = rd.read_csv_uno(path)
  print("Type the continent to plot")
  continent = input("> ")
  plot_pie_chat(population, continent)

if __name__ == '__main__':

  run()
