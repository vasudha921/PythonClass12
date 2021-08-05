import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("distribute.csv")
fig = ff.create_distplot([df["Height(Inches)"]], ["Height plotting"], show_hist= False)
fig.show()
