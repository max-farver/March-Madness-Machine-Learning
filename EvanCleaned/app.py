import numpy
import pandas as pd
import plotly_express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

tourneyGames = pd.read_hdf("FirstRound.h5", key="df")
col_options = [dict(label=x, value=x) for x in tourneyGames.columns]
dimensions = ["x", "y", "color"]

app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)

app.layout = html.Div(
    [
        html.H1("Demo: Plotly Express in Dash with Tips Dataset"),
        html.Div(
            [
                html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
                for d in dimensions
            ],
            style={"width": "25%", "float": "left"},
        ),
        dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"}),
    ]
)


@app.callback(Output("graph", "figure"), [Input(d, "value") for d in dimensions])
def make_figure(x, y, color):
    return px.scatter(
        tourneyGames,
        x=x,
        y=y,
        color=color,
        height=700,
    )

if __name__ == "__main__":
    app.run_server(debug=True)