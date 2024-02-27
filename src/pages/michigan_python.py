import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_player

dash.register_page(__name__, order=4)

green_text = {'color':'green'}

def layout():
    return dbc.Row([
        dbc.Card(
            style={"width": "48%", "padding": "0px"},
            children=[
                dash_player.DashPlayer(
                    id="player",
                    url="https://www.youtube.com/watch?v=2IKErnao0Dg",
                    controls=True,
                    width="100%",
                    height="250px",
                )]
        ),
    ], justify='center')