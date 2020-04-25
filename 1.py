
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def random_colours(number_of_colors):
    colors = []
    for i in range(number_of_colors):
        colors.append("#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
    return colors

sns.set_context('paper')
import random

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (25, 15)

df = pd.read_csv('dataset.csv', index_col='name')

df.info()
print(df.groupby('name')['price', 'views'].median())



df.groupby('name')['views'].median().plot(kind='bar', stacked=True,  color=random_colours(12))
plt.savefig( 'A/name-views-bar.png' )
df.groupby('name')['price'].median().plot(kind='bar', stacked=True,  color=random_colours(12))
plt.savefig( 'A/name-price-bar.png' )

df.plot(stacked=True,  color=random_colours(12), x='price', y='views')
plt.savefig( 'A/price-views.png' )
