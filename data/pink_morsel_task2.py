from dash import Dash, dcc, html, dash
import plotly.express as px
import pandas as pd
import csv


from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import csv
app = dash.Dash(__name__)
df = pd.read_csv("final.csv")

fig = px.line(df, x='date', y='sales', color='region')

app.layout = html.Div(children=[
    html.H1(children='Pink Morsels Sales Analysis - Soul Food'),
    html.Div(children='''Sales analysis to and from price increase on 15th Jan.'''),
    dcc.Graph(id='example-graph', figure=fig)
])

fig.show()
if __name__== '__main__':
    app.run_server(debug=True)

