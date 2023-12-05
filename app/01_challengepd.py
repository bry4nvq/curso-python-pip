import charts
import pandas as pd

def select_country(countries, country):
  """
  Select the country we want to plot it as a dataframe
  """
  pais = countries[countries['Country/Territory'] == country.title()]

  return pais

def populations_country(country):
  """
  filter the population by year columns of the dataframe
  """
  years = country[country.columns[5:13]]
  forma = years.melt(var_name='year', value_name='population')
  #print(selected.filter(like='Population'))
  forma['year'] = forma['year'].replace(' Population', '', regex=True)
  
  return forma

def plot_country(populations, country):
  
  selected_country = select_country(populations, country)
  populations_by_year = populations_country(selected_country)
  labels = populations_by_year['year'].values
  values = populations_by_year['population'].values
  charts.generate_bar_chart(country,labels[::-1],values[::-1])

def run():

  print("Type the country to plot")
  country = input("> ")
  path = './population.csv'
  population = pd.read_csv(path)
  plot_country(population, country)


if __name__ == '__main__':

    run()