import pandas as pd
import charts

def countries_population_ratio(population, continent):

  countries_ratio = population[population['Continent'] == continent.title()]
  countries_ratio = countries_ratio[['Country/Territory','World Population Percentage']]
  labels = countries_ratio['Country/Territory'].values
  values = countries_ratio['World Population Percentage'].values

  return labels, values

def plot_pie_chat(population,continent):

  labels, values = countries_population_ratio(population, continent)
  charts.generate_pie_chart(continent, labels, values)

def run():
  path = './population.csv'
  population = pd.read_csv(path)
  print("Type the continent to plot")
  continent = input("> ")
  plot_pie_chat(population, continent)

if __name__ == '__main__':

  run()