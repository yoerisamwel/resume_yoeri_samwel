import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=2)

def layout():
    return html.Div([
    html.H3("People that I've had the pleasure to work with", style={'textAlign':'center'}, className='my-3'),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('#### Joe Thompson'),
            dcc.Markdown('Director of Supply Chain')
        ], width=2),
        dbc.Col([
            dcc.Markdown('Yoeri is the rare jack-of-all-trades that excels at everything he touches,'
                         ' partially from natural talent and intelligence, partially from his steadfast '
                         'determination to seeing projects through to their conclusion. He is an intuitive' 
                         'problem-solver that will continuously innovate to reach sound, data-driven solutions,' 
                         "and I've personally seen him touch all corners of our business leaving no stone unturned"
                         ' to provide exceptional resolutions. I consider myself extremely fortunate to have '
                         'had Yoeri on our team.',
                         className='ms-3'),
        ], width=5)
    ], justify='center'),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('#### Ousmane Dembélé'),
            dcc.Markdown('FC Barcelona Attacking Midfielder')
        ], width=2),
        dbc.Col([
            dcc.Markdown('Yoeri is so good with the ball. Every time he has the ball, I can see the stadium rise to its feet.'
                         ' And he always shares goal opportunities with his teammates. The opposite of selfish. I know it is not '
                         'appropriate for a player to say this, but I wish Yoeri was our coach instead of Xavier.',
                         className='ms-3'),
        ], width=5)
    ], justify='center'),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('#### Eric Garcia'),
            dcc.Markdown('FC Barcelona Defender')
        ], width=2),
        dbc.Col([
            dcc.Markdown('I feel so lucky to have a teammate like Yoeri on my team. People talk about Messi all the time '
                         'but the talent Yoeri has for making goals is unmatched. Plus, Yoeri has never evaded taxes, so you '
                         'would be lucky to have him on your team.',
                         className='ms-3'),
        ], width=5)
    ], justify='center')
])