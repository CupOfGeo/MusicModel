import pandas as pd
import numpy as np
import plotly.express as px
df = pd.read_csv('data.csv')
#print(df.columns)


filtered_df = df[df.year >= 2015].copy()
filtered_df['artists'] = filtered_df['artists'].apply(lambda x: x[1:-1].replace("'", ""))
art = filtered_df['artists'].sample()
print(len(art))
print(art.values[0])#.index[0])

#i should remove the brackets and the quotes
#match same song
#for name in df['name']:
