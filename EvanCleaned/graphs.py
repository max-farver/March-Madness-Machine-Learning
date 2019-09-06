import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

import pandas as pd

champs = pd.read_hdf("Champions.h5", key="df")
ncaa_tourney = pd.read_hdf("AllNcaaTourneyGames.h5", key="df")
champs_games = pd.read_hdf("AllChampGames.h5", key="df")
champ_mean = pd.read_hdf("ChampMean.h5", key="df")
first_round = pd.read_hdf("FirstRound.h5", key="df")




champ2003 = champs_games[champs_games['Season'] == 2003]
champ2004 = champs_games[champs_games['Season'] == 2004]
champ2005 = champs_games[champs_games['Season'] == 2005]
champ2006 = champs_games[champs_games['Season'] == 2006]
champ2007 = champs_games[champs_games['Season'] == 2007]
champ2008 = champs_games[champs_games['Season'] == 2008]
champ2009 = champs_games[champs_games['Season'] == 2009]
champ2010 = champs_games[champs_games['Season'] == 2010]
champ2011 = champs_games[champs_games['Season'] == 2011]
champ2012 = champs_games[champs_games['Season'] == 2012]
champ2013 = champs_games[champs_games['Season'] == 2013]
champ2014 = champs_games[champs_games['Season'] == 2014]
champ2015 = champs_games[champs_games['Season'] == 2015]
champ2016 = champs_games[champs_games['Season'] == 2016]
champ2017 = champs_games[champs_games['Season'] == 2017]

champ_score = dcc.Graph(
        id='champ_score',
        figure={
            'data':[
                go.Scatter(
                    x=champ2003['DayNum'],
                    y=champ2003['Score'],
                    mode='markers',
                    name=str(champ2003['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(19, 81, 249)' #blue
                    },
                ),
                go.Scatter(
                    x=champ2004['DayNum'],
                    y=champ2004['Score'],
                    mode='markers',
                    name=str(champ2004['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(25,255,102)' #guppie green
                    },
                ),
                go.Scatter(
                    x=champ2005['DayNum'],
                    y=champ2005['Score'],
                    mode='markers',
                    name=str(champ2005['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(230,230,0)' #peridot
                    },
                ),
                go.Scatter(
                    x=champ2006['DayNum'],
                    y=champ2006['Score'],
                    mode='markers',
                    name=str(champ2006['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(255,0,255)' #fuchsia
                    },
                ),
                go.Scatter(
                    x=champ2007['DayNum'],
                    y=champ2007['Score'],
                    mode='markers',
                    name=str(champ2007['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(102,255,255)' #electric blue
                    },
                ),
                go.Scatter(
                    x=champ2008['DayNum'],
                    y=champ2008['Score'],
                    mode='markers',
                    name=str(champ2008['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(255,153,170)' #salmon pink
                    },
                ),
                go.Scatter(
                    x=champ2009['DayNum'],
                    y=champ2009['Score'],
                    mode='markers',
                    name=str(champ2009['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(234,230,255)' #lavender
                    },
                ),
                go.Scatter(
                    x=champ2010['DayNum'],
                    y=champ2010['Score'],
                    mode='markers',
                    name=str(champ2010['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(0,153,153)' #persian green
                    },
                ),
                go.Scatter(
                    x=champ2011['DayNum'],
                    y=champ2011['Score'],
                    mode='markers',
                    name=str(champ2011['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(255,128,0)' #orange
                    },
                ),
                go.Scatter(
                    x=champ2012['DayNum'],
                    y=champ2012['Score'],
                    mode='markers',
                    name=str(champ2012['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(0,102,17)' #pakistan green
                    },
                ),
                go.Scatter(
                    x=champ2013['DayNum'],
                    y=champ2013['Score'],
                    mode='markers',
                    name=str(champ2013['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(230,238,255)' #glitter
                    },
                ),
                go.Scatter(
                    x=champ2014['DayNum'],
                    y=champ2014['Score'],
                    mode='markers',
                    name=str(champ2014['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(128,0,21)' #burgundy
                    },
                ),
                go.Scatter(
                    x=champ2015['DayNum'],
                    y=champ2015['Score'],
                    mode='markers',
                    name=str(champ2015['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(255,230,251)' #lavender blush
                    },
                ),
                go.Scatter(
                    x=champ2016['DayNum'],
                    y=champ2016['Score'],
                    mode='markers',
                    name=str(champ2016['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(255,242,230)' #old lace
                    },
                ),
                go.Scatter(
                    x=champ2017['DayNum'],
                    y=champ2017['Score'],
                    mode='markers',
                    name=str(champ2017['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(234,255,230)' #honeydew
                    },
                )
            ],
            'layout': go.Layout(
                xaxis={'type': 'linear', 'title': 'Champ Score vs Round'},
                yaxis={'type': 'linear', 'title': 'Points'},
                showlegend= False
            )
        }
    )

champ_agianst = dcc.Graph(
        id='champ_against',
        figure={
            'data':[
                go.Scatter(
                    x=champ2003['DayNum'],
                    y=champ2003['OppScore'],
                    mode='markers',
                    name=str(champ2003['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(19, 81, 249)' #blue
                    },
                ),
                go.Scatter(
                    x=champ2004['DayNum'],
                    y=champ2004['OppScore'],
                    mode='markers',
                    name=str(champ2004['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(25,255,102)' #guppie green
                    },
                ),
                go.Scatter(
                    x=champ2005['DayNum'],
                    y=champ2005['OppScore'],
                    mode='markers',
                    name=str(champ2005['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(230,230,0)' #peridot
                    },
                ),
                go.Scatter(
                    x=champ2006['DayNum'],
                    y=champ2006['OppScore'],
                    mode='markers',
                    name=str(champ2006['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(255,0,255)' #fuchsia
                    },
                ),
                go.Scatter(
                    x=champ2007['DayNum'],
                    y=champ2007['OppScore'],
                    mode='markers',
                    name=str(champ2007['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(102,255,255)' #electric blue
                    },
                ),
                go.Scatter(
                    x=champ2008['DayNum'],
                    y=champ2008['OppScore'],
                    mode='markers',
                    name=str(champ2008['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(255,153,170)' #salmon pink
                    },
                ),
                go.Scatter(
                    x=champ2009['DayNum'],
                    y=champ2009['OppScore'],
                    mode='markers',
                    name=str(champ2009['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(234,230,255)' #lavender
                    },
                ),
                go.Scatter(
                    x=champ2010['DayNum'],
                    y=champ2010['OppScore'],
                    mode='markers',
                    name=str(champ2010['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(0,153,153)' #persian green
                    },
                ),
                go.Scatter(
                    x=champ2011['DayNum'],
                    y=champ2011['OppScore'],
                    mode='markers',
                    name=str(champ2011['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(255,128,0)' #orange
                    },
                ),
                go.Scatter(
                    x=champ2012['DayNum'],
                    y=champ2012['OppScore'],
                    mode='markers',
                    name=str(champ2012['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(0,102,17)' #pakistan green
                    },
                ),
                go.Scatter(
                    x=champ2013['DayNum'],
                    y=champ2013['OppScore'],
                    mode='markers',
                    name=str(champ2013['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(230,238,255)' #glitter
                    },
                ),
                go.Scatter(
                    x=champ2014['DayNum'],
                    y=champ2014['OppScore'],
                    mode='markers',
                    name=str(champ2014['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(128,0,21)' #burgundy
                    },
                ),
                go.Scatter(
                    x=champ2015['DayNum'],
                    y=champ2015['OppScore'],
                    mode='markers',
                    name=str(champ2015['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': 'rgb(255,230,251)' #lavender blush
                    },
                ),
                go.Scatter(
                    x=champ2016['DayNum'],
                    y=champ2016['OppScore'],
                    mode='markers',
                    name=str(champ2016['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(255,242,230)' #old lace
                    },
                ),
                go.Scatter(
                    x=champ2017['DayNum'],
                    y=champ2017['OppScore'],
                    mode='markers',
                    name=str(champ2017['Season']),
                    opacity=0.7,
                    marker={
                        'size':6,
                        'line': {'width': 0.5, 'color': 'white'},
                        'color':  'rgb(234,255,230)' #honeydew
                    },
                )
            ],
            'layout': go.Layout(
                xaxis={'type': 'linear', 'title': 'Champ Points Against vs Round'},
                yaxis={'type': 'linear', 'title': 'Points Against'},
                showlegend= False
            )
        }
    )

champ_score_average = dcc.Graph(
    id="champ_score_average",
    figure={
        'data':[
            go.Scatter(
                x = champ_mean['DayNum'],
                y = champ_mean['Score'],
                mode = 'markers',
                opacity=0.7,
                marker={
                    'size':6,
                    'line': {'width': 0.5, 'color': 'white'},
                    'color':  'rgb(0,0,0)' #black
                },
            )
        ],
        'layout': go.Layout(
            xaxis={'type': 'linear', 'title': 'Champ Average Points vs Round'},
            yaxis={'type': 'linear', 'title': 'Average Points'},
            showlegend= False
        )
    }
)

champ_against_average = dcc.Graph(
    id="champ_agianst_average",
    figure={
        'data':[
            go.Scatter(
                x = champ_mean['DayNum'],
                y = champ_mean['OppScore'],
                mode = 'markers',
                opacity=0.7,
                marker={
                    'size':6,
                    'line': {'width': 0.5, 'color': 'white'},
                    'color':  'rgb(0,0,0)' #black
                },
            )
        ],
        'layout': go.Layout(
            xaxis={'type': 'linear', 'title': 'Champ Average Points Against vs Round'},
            yaxis={'type': 'linear', 'title': 'Average Points Against'},
            showlegend= False
        )
    }
)

champ_seed = dcc.Graph(
    id="champ_seed",
    figure={
        'data':[
            go.Bar(
                x=[1,2,3,7],
                y=[9,2,3,1],
                text=champs['WSeed'],
                marker=dict(
                    color='rgb(158,202,225)',
                    line=dict(
                        color='rgb(8,48,107)',
                        width=1.5),
                ),
                opacity=0.6
            )
        ],
        'layout': go.Layout(
            xaxis={'type': 'linear', 'title': 'Champ Seed'},
            yaxis={'type': 'linear', 'title': 'Number of Occurences'},
        )
    }
)
# x=[1,2,3,4,5]
x=['big_east','acc','sec', 'big_twelve', 'aac']
y=[5,5,3,1,1]
champ_conf = dcc.Graph(
    id="champ_conf",
    figure={
        'data':[
            go.Bar(
                x=x,
                y=y,
                text=y,
                textposition='auto',
                marker=dict(
                    color='rgb(158,202,225)',
                    line=dict(
                        color='rgb(8,48,107)',
                        width=1.5),
                ),
                opacity=0.6
            )
        ],
        'layout': go.Layout(
            xaxis={'title': 'Champ Conference'},
            yaxis={'type': 'linear', 'title': 'Number of Championships'},
        )
    }
)

tourney_games = dcc.Graph(
    id="tourney_games",
    figure={
        'data':[
            go.Bar(
                x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
                y=[251,198,176,155,124,111,123,106,91,94,102,92,74,68,65,60],
                text=ncaa_tourney['Seed'],
                marker=dict(
                    color='rgb(158,202,225)',
                    line=dict(
                        color='rgb(8,48,107)',
                        width=1.5),
                ),
                opacity=0.6
            )
        ],
        'layout': go.Layout(
            xaxis={'type': 'linear', 'title': 'Games Played vs Seed'},
            yaxis={'type': 'linear', 'title': 'Score'},
        )
    }
)