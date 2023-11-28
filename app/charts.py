import matplotlib.pyplot as plt

def generate_bar_chart(country,labels,values):

  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.title("Population by year")
  plt.savefig(f'./imgs/bar/{country}_bar_chart.png')
  plt.close()

def generate_pie_chart(continent, labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis('equal')
  plt.savefig(f'./imgs/pie/{continent}_pie_chart.png')
  plt.close()

if __name__ == '__main__':
  labels = ['A', 'B', 'C']
  values = [15, 20, 14]
  country = 'china'
  continent = 'South America'
  generate_bar_chart(country,labels,values)
  generate_pie_chart(continent,labels,values)
  



