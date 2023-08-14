import json
import os
from django.conf import settings
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

app = DjangoDash("SimpleExample")

app.layout = html.Div(
    className="plotly-app",
    children=[
        html.H3("Analysis of the ML model's results using ROC and PR curves"),
        html.P("Select a model:"),
        dcc.Dropdown(
            id="dropdown",
            options=["Logistic Regression", "Decision Tree", "Random Forest"],
            value="Logistic Regression",
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


@app.callback(Output("graph", "figure"), Input("dropdown", "value"))
def display_roc(model_name):
    # roc_data file paths
    logreg_path = "log_reg_roc.json"
    dectree_path = "dec_tree_roc.json"
    rdmfrst_path = "rdm_frst_roc.json"

    if model_name == "Logistic Regression":
        data_path = logreg_path
        score = 0.83

    elif model_name == "Decision Tree":
        data_path = dectree_path
        score = 0.89
    elif model_name == "Random Forest":
        data_path = rdmfrst_path
        score = 0.95
    else:
        pass
    data_path = os.path.join(
        f"{settings.BASE_DIR}/wqpred/dash_apps/finished_apps", data_path
    )
    # load data
    with open(data_path) as json_data:
        roc_data = json.load(json_data)

    x = roc_data["fpr"]
    # min_x = min(x)
    # max_x = max(x)
    y = roc_data["tpr"]
    # min_y = min(y)
    # max_y = max(y)

    x_line = [i / 10 for i in range(0, 11, 1)]
    y_line = x_line
    graph = go.Scatter(x=x, y=y, fill="tozeroy", name=f"{model_name}")
    line = go.Scatter(x=x_line, y=y_line, name="Random Classifier")

    layout = go.Layout(
        title=f"ROC Curve (AUC={score})"
        # paper_bgcolor="#27293d",
        # plot_bgcolor="rgba(0,0,0,0)",
    )

    plot_dict = {"data": [graph, line], "layout": layout}
    plot_info = f"score {score}"

    return plot_dict
