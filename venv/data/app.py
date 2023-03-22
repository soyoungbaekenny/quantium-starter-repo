import pandas as pd
from dash import Dash, html, dcc

from plotly.express import line

csv_file = "./final.csv"

df = pd.read_csv(csv_file)
df = df.sort_values(by="date")
app = Dash(__name__)

fig = line(df, x="date", y="sales", title="Pink Morsel Sales")
visualization = dcc.Graph(
    id="visualization",
    figure=fig
)
app.layout = html.Div(children=[
    html.H1(children='Pink Morsels Sales Analysis - Soul Food'),
    html.Div(children='''Sales analysis to and from price increase on 15th Jan.'''),
    dcc.Graph(id='line-graph', figure=fig)
])

if __name__ == '__main__':
    app.run_server()