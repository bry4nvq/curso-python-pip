import matplotlib.pyplot as plt

def generate_pie_chart():

    labels = ['X','C','Z']
    values = [130, 120, 122]

    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig('pie.png')
    plt.close()