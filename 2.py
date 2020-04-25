import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

def random_colours(number_of_colors):
    colors = []
    for i in range(number_of_colors):
        colors.append("#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
    return colors

sns.set_context('paper')
plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (25, 15)  # Размер картинок

def graph(NAME):

    df = pd.read_csv(NAME+'.csv', sep=',')

    df = df.iloc[::-1]
    print(df)
    df['Date'].plot(x="Date", y="Price", stacked=True,  color=random_colours(12))
    path = 'B' + '/' + NAME + '.png'
    plt.savefig(path)
    plt.close('all')

graph('AAPL')
graph('AMZN')
graph('FB')
graph('GOOGL')
graph('NFLX')