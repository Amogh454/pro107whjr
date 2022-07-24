import pandas as pd
import plotly
import plotly_express as Pe
import csv
import plotly.graph_objects as pg

df = pd.read_csv('data.csv')
print(df.groupby('level')['attempt'].mean())
graph = pg.Figure(pg.Scatter(x=df.groupby('level')['attempt'].mean(), y= ['Level 1', 'Level 2', 'Level 3', 'Level 4'], ))
graph.show()