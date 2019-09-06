import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from graphs import champ_score, champ_agianst, champ_score_average, champ_against_average, champ_seed, tourney_games,\
    champ_conf

external_stylesheets = ['https://unpkg.com/material-components-web@latest/dist/material-components-web.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='March Madness Analysis'),

    # html.Div(children='''
    #     Dash: A web application framework for Python.
    # '''),

    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Champ Score Vs Round', children=[
            champ_score
        ]),
        dcc.Tab(label="Champ Point Against Vs Round", children=[
            champ_agianst
        ]),
        dcc.Tab(label='Champ Average Score Vs Round', children=[
            champ_score_average
        ]),
        dcc.Tab(label="Champ Average Points Against Vs Round", children=[
            champ_against_average
        ]),
        dcc.Tab(label="Count of Seed Vs Win", children=[
            champ_seed
        ]),
        dcc.Tab(label="Conference Championships", children=[
            champ_conf
        ]),
        dcc.Tab(label="Count Of Games for Seed", children=[
            tourney_games
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)