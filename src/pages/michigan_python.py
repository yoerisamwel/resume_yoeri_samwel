import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_player

dash.register_page(__name__, order=4)

# Define text style for headings and paragraphs
text_style = {
    'color': '#fff',
    'fontFamily': 'Arial, sans-serif'
}

# Custom CSS for equal card height
card_body_style = {
    "display": "flex",
    "flexDirection": "column",
    "justifyContent": "space-between",
    "height": "400px"
}

def layout():
    return dbc.Container([
        # Introductory text
        html.Div([
            html.H2("Michigan Python Presentations", style=text_style),
            html.P(
                "I am creating these presentation videos to improve my presentation skills and "
                "get to know more fellow Python enthusiasts.", style=text_style
            )
        ]),

        # Row for video players
        dbc.Row([
            # First video card
            dbc.Col([
                dbc.Card(
                    style={"width": "100%", "margin-bottom": "20px"},
                    children=[
                        dbc.CardHeader("Dash Plotly presentation"),
                        dbc.CardBody([
                            dash_player.DashPlayer(
                                id="player1",
                                url="https://www.youtube.com/watch?v=9lD73vbDjG4",
                                controls=True,
                                width="100%",
                                height="250px",
                            ),
                            html.P("I conducted a virtual presentation for Michigan Python, "
                                   "offering a beginner-friendly introduction to Dash by Plotly, showcasing "
                                   "its versatility as a presentation tool.",
                                   className="card-text")
                        ], style=card_body_style)
                    ]
                )
            ], width=12, md=6),

            # Second video card
            dbc.Col([
                dbc.Card(
                    style={"width": "100%", "margin-bottom": "20px"},
                    children=[
                        dbc.CardHeader("Pandas introduction"),
                        dbc.CardBody([
                            dash_player.DashPlayer(
                                id="player2",
                                url="https://www.youtube.com/watch?v=2IKErnao0Dg&t=30s",
                                controls=True,
                                width="100%",
                                height="250px",
                            ),
                            html.P("I had the opportunity to share my knowledge with the Michigan "
                                   "Python community through a virtual presentation, focusing on "
                                   "the powerful pandas library, a cornerstone for data manipulation "
                                   "and analysis in Python.",
                                   className="card-text")
                        ], style=card_body_style)
                    ]
                )
            ], width=12, md=6),
        ], justify='around'),
        dbc.Row([
            # Third video card
            dbc.Col([
                dbc.Card(
                    style={"width": "100%", "margin-bottom": "20px"},
                    children=[
                        dbc.CardHeader("Geopandas introduction"),
                        dbc.CardBody([
                            dash_player.DashPlayer(
                                id="player3",
                                url="https://www.youtube.com/watch?v=CXWsC6t4M2s&t=1408s",
                                controls=True,
                                width="100%",
                                height="250px",
                            ),
                            html.P("I had the opportunity to share my knowledge with the Michigan Python community "
                                   "through a virtual presentation, focusing on the powerful GeoPandas library, "
                                   "a cornerstone for geospatial data manipulation and analysis in Python.",
                                   className="card-text")
                        ], style=card_body_style)
                    ]
                )
            ], width=12, md=6),
        ], justify='start'),
    ], fluid=True)