import pandas as pd
import plotly.figure_factory as pf

df = pd.read_csv('SOCR-HeightWeight.csv')
fig = pf.create_distplot([df["Weight(Pounds)"].tolist()],["Hello,thisismyfirst height?Wait,wdym?"],show_hist=False)
fig.show()