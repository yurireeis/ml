import matplotlib.pyplot as plt
import pandas as pd
import mplleaflet as mpl

plt.hold(True)
df = pd.read_csv('dataset/copacabana_lat_lng.csv')
plt.plot(df['lng'], df['lat'], 'o')
mpl.show()
