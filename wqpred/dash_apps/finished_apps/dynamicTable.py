import json
import os
from django.conf import settings
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

app = DjangoDash("DynamicTable")

app.layout = html.Div(
    className="plotly-app",
    children=[
        html.H3("Input vs Summary Statistics"),
        html.P("Select a model:"),
        dcc.Dropdown(
            id="dropdown",
            options=["Maximum", "Median", "Minimum"],
            value="Maximum",
            clearable=False,
            style={"margin-bottom": "1rem", "width": "50%", "color": "#270c3b"},
        ),
        dcc.Graph(id="graph", style={}),  # animate=True,
    ],
    style={
        "background-color": "#270c3b",
        "padding": "1rem 1rem",
        "border-radius": "2rem",
        "color": "white",
    },
)
