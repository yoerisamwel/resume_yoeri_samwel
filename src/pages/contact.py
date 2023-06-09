import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=3)

green_text = {'color':'green'}

def layout():
    return dbc.Row([
        dbc.Col([
    dcc.Markdown('# Yoeri Samwel', className='mt-5'),
    html.Hr(),
    dcc.Markdown('### Personal info', className='mb-2'),
    dcc.Markdown('Address:', className='mb-2'),
    dcc.Markdown('510 n Connecticut ave Royal Oak MI'),
    dcc.Markdown('Phone Number:', className='mb-2'),
    dcc.Markdown('540-729-4921'),
    dcc.Markdown('Email:', className='mb-2'),
    dcc.Markdown('yoerisamwel@gmail.com'),
    dcc.Markdown('Linkedin:', className='mb-2'),
    dcc.Markdown('https://www.linkedin.com/in/yoeri-samwel-07301826/', link_target='_blank'),
    dcc.Markdown('Github:', className='mb-2'),
    dcc.Markdown('github.com/yoerisamwel', link_target='_blank'),
        ], width={'size':6, 'offset':2})
], justify='center')