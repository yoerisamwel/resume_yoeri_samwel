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
            dcc.Markdown('Urbanstems Director of Supply Chain')
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
            dcc.Markdown('#### Steven Weinstein'),
            dcc.Markdown('Urbanstems Lead analyst engineer')
        ], width=2),
        dbc.Col([
            dcc.Markdown('Yoeri is a combination of a strong business acumen, a sense of curiosity, and an ability to '
                         'learn quickly.'
                         ' At Urbanstems, Yoeri was able to identify areas where his technical skills could add large '
                         'amounts of value and then collaborated with business users to quickly build in-depth, '
                         'reusable analysis. '
                         'Not satisfied with that, he continued to pull on strings, looking for previously unknown '
                         'drivers of crucial KPIs which led to new questions, new analysis, and, ultimately, better '
                         'decisions. I would be lucky to work with him again.',
                         className='ms-3'),
        ], width=5)
    ], justify='center'),
    html.Hr()
])