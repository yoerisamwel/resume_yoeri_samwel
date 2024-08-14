import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
from .side_bar import sidebar
from dash_bootstrap_templates import load_figure_template

dash.register_page(__name__, title='Projects', order=1)

load_figure_template(["SUPERHERO"])

def layout():

    return html.Div([
    dbc.Row([html.Br()]),
    dbc.Row([  # Row starts here
        dbc.Col([  # Column inside the row
            dbc.Card(
                [
                    dbc.CardHeader("Titanic analysis"),
                    dbc.CardBody(
                        [
                            html.P("A brief analysis of the Titanic dataset.", className="card-text"),
                            dbc.Button("Go to GitHub", href="https://github.com/yoerisamwel/titanic-analysis",
                                       color="primary", external_link=True, target="_blank")
                        ]
                    )
                ],
                #style={"width": "18rem"},  # Adjust size as needed
                className="rounded-3"  # Rounded edges
            )
        ], width=6),
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardHeader("Titanic analysis"),
                    dbc.CardBody(
                        [
                            html.P("A brief analysis of the Titanic dataset.", className="card-text"),
                            dbc.Button("Go to GitHub", href="https://github.com/yoerisamwel/titanic-analysis",
                                       color="primary", external_link=True, target="_blank")
                        ]
                    )
                ],
                #style={"width": "18rem"},  # Adjust size as needed
                className="rounded-3"  # Rounded edges
            )
    ], width=6)])
    ])


