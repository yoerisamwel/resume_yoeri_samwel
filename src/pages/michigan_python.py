import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_player

dash.register_page(__name__, order=4)

text_style = {'textAlign': 'center', 'margin': '20px'}


def layout():
    return dbc.Container([
        # Introductory text
        html.Div([
            html.H2("Presentation Skills Enhancement", style=text_style),
            html.P(
                "I am creating these presentation videos to improve my presentation skills and "
                "get to know more Python enthusiasts.", style=text_style
            )
        ]),

        # Row for video players
        dbc.Row([
            # First video
            dbc.Col([
                dbc.Card(
                    style={"width": "100%", "padding": "0px"},
                    children=[
                        dash_player.DashPlayer(
                            id="player1",
                            url="https://www.youtube.com/watch?v=9lD73vbDjG4",
                            controls=True,
                            width="100%",
                            height="250px",
                        )]
                )
            ], width=12, md=6),  # md=6 for medium screens, each video takes half width

            # Second video
            dbc.Col([
                dbc.Card(
                    style={"width": "100%", "padding": "0px"},
                    children=[
                        dash_player.DashPlayer(
                            id="player2",
                            url="https://www.youtube.com/watch?v=2IKErnao0Dg&t=30s",
                            controls=True,
                            width="100%",
                            height="250px",
                        )]
                )
            ], width=12, md=6),  # Same here for consistent layout
        ], justify='around'),  # This will space out the video columns on larger screens
    ], fluid=True)  # fluid=True for the Container to use the entire screen width