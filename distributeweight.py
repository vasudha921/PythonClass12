import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("distribute.csv")
fig = ff.create_distplot([df["Weight(Pounds)"]], ["Weight plotting"], show_hist= False)
fig.show()