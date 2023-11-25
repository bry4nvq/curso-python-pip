import tools

dict = [{'country':'Colombia','population':50}
  , {'country':'Bolivia','population':30}
  , {'country':'Argentina','population':48}
  ,{'country':'Perú','population':43}]

def run():
  #from mod import get_population
  keys, values = tools.get_population()
  print(keys, values)
  print('\n')
  country = input("Type Country: ")
  new_dict = tools.population_by_country(dict,country)
  print(new_dict)
  print('\n')

if __name__ == '__main__':
  run()

"""
This "if__name__ == '__main__'" is called entry point it helps to execute
the part of code we want from another python file, keeping the option to
execute it as well in the terminal
"""