import pandas as pd
from bokeh.plotting import show
from plotter import *

s=pd.Series([1,2,3])
print(s)
print(type(list(s)[0]))


df=pd.read_csv('~/Desktop/recal_manual/000001_test.csv')
print(df)
show(line_graph_plot(df))