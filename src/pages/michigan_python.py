import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_player

dash.register_page(__name__, order=4)

# Style for the introductory text
text_style = {'textAlign': 'center', 'margin': '20px'}


def layout():
    return dbc.Container([
        # Introductory text
        html.Div([
            html.H2("Presentation Skills Enhancement", style=text_style),
            html.P(
                "I am creating these presentation videos to improve my presentation skills and "
                "expand my network of Python enthusiasts.", style=text_style
            )
        ]),

        # Row for video players
        dbc.Row([
            # First video card
            dbc.Col([
                dbc.Card(
                    style={"width": "100%", "margin-bottom": "20px"},
                    children=[
                        dbc.CardHeader("This Presentation"),
                        dbc.CardBody([
                            dash_player.DashPlayer(
                                id="player1",
                                url="https://www.youtube.com/watch?v=9lD73vbDjG4",
                                controls=True,
                                width="100%",
                                height="250px",
                            ),
                            html.P("Here's an explanation of what this video is about, "
                                   "and how it contributes to my presentation skills improvement.",
                                   className="card-text")
                        ])
                    ]
                )
            ], width=12, md=6),

            # Second video card
            dbc.Col([
                dbc.Card(
                    style={"width": "100%", "margin-bottom": "20px"},
                    children=[
                        dbc.CardHeader("This Presentation"),
                        dbc.CardBody([
                            dash_player.DashPlayer(
                                id="player2",
                                url="https://www.youtube.com/watch?v=2IKErnao0Dg&t=30s",
                                controls=True,
                                width="100%",
                                height="250px",
                            ),
                            html.P("This video further demonstrates my efforts in honing "
                                   "my presentation skills, featuring Python-related content.",
                                   className="card-text")
                        ])
                    ]
                )
            ], width=12, md=6),
        ], justify='around'),
    ], fluid=True)