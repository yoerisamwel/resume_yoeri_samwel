import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_player

dash.register_page(__name__, path='/', order=0)

# resume sample template from https://zety.com/
layout = html.Div([
    dcc.Markdown('# Yoeri Samwel', style={'textAlign':'center'}),
    dcc.Markdown('Michigan, USA', style={'textAlign': 'center'}),

    dcc.Markdown('### Professional Summary', style={'textAlign': 'center'}),
    html.Hr(),
    dcc.Markdown('I am a dynamic, outgoing person with strong communication skills. \n'
                 'Experience with python and especially the Dash plotly visualization library \n'
                 'I actively seek opportunities where my analytical skills and creativity can ' 
                 'contribute and help drive change/innovation.\n'
                 'My ability to adapt and learn in a fast paced changing environment makes'
                 'me an asset for organizations.\n'
                 'I firmly believe in continuous learning. I actively seek out opportunities to learn '
                 'new skills that improve me as a professional and as a person.\n'
                 'I thrive working independently as well as being part of a team (or as group leader)' 
                 'and my passion is to motivate people towards achieving shared goals.\n',
                 style={'textAlign': 'center', 'white-space': 'pre'}),
    dcc.Markdown('### Skills', style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            * Guest services 
            * Inventory control procedures
            * Supply Chain expertise
            ''')
        ], width={"size": 3, "offset": 1}),
        dbc.Col([
            dcc.Markdown('''
            * Python 
            * SQL
            * Excel/Google sheets
            * HTML 
            * CSS
            * 
            ''')
        ], width=3)
    ], justify='center'),

    dcc.Markdown('### Work History', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('10/2022 to 6/2023', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Supply Chain Analytics manager \n'
                         'Urbanstems - Remote, MI',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Performed complex analyses on large datasets for the supply-chain team. '
                        'Utilized Looker, Mode and Dash plotly to visualize the analysis.'),
                html.Li('Developed tool to identify non optimal outbound shipments in the network. '
                        'The setup allows for high level trend identification. As well as deep dives into '
                        'different events causing the non optimal outbound shipments to spike'),
                html.Li('Developed tool to identify non optimal outbound shipments in the network. '
                        'The setup allows for high level trend identification. As well as deep dives into '
                        'different events causing the non optimal outbound shipments to spike')
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('08/2020 to 10/2022',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('NonFloral Procurement Manager \n'
                         'Urbanstems - Remote, MI',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Managed the plant supply chain team (2 FTE team members) as well as 5 dropship locations.'
                    'As well as the inbound logistics of plants and hardgoods into the internal Urbanstems network.'),
                html.Li(
                    'Developed extensive analysis with python and a UI in Dash plotly. '
                    'To identify quality and packaging issues driving poor customer expierences.'
                    "Drove improvements in packaging SOP's and team training in packaging and quality control "
                    "based on this analysis"
                    'The setup of the Dashboard allows for high level tren spotting and depp dives into '
                    'specific issues'),
                html.Li(
                    'Developed an extensive outbound shipping cost analysis with python and a UI (Dashbaord) in '
                    'Dash plotly.'
                    'Allowing to monitor where outbound shipping cost were elevated and the correlation with on hand '
                    'inventory levels. Ebeling corrective actions to be taken to minimize outbound freight cost.'),
                html.Li(
                    'Based improvement plan for the distribution network on this analysis '
                    'and presented this to senior leadership.'),
                html.Li(
                    'Improved quality issue rates from 7% to 3%.')
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('01/2020 to 08/2020',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Head of fulfillment \n'
                         'Urbanstems - On Site, DC',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    "Managed the order fulfillment for three fulfillment centers and the distribution warehouse."
                    'Responsible for up to 50 employees during major holidays.'),
                html.Li(
                    'Reviewed and implemented improvements in how plant and flowers were processed and stored.'
                    ' This through training and sharing information with the team members'),
                html.Li(
                    'Developed a mode report that allowed tracking of employee productivity as well as quality '
                    'issues caused by packing. '
                    'Getting this information visible to the team allowed for feedback to individual team members '
                    'and helped improve fulfillment productivity/reduce labor cost. '
                    'As well as reduce quality complain rates due to packing errors.'),
                html.Li(
                    'Developed extensive analysis in google sheets to track where labor was spend.'
                    'As well as budget what we expected to spend labor on based on the sales forecast'),
                html.Li(
                    'Led the warehouse team on site through the start of the covid epidemic.')
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('08/2019 to 12/2019',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Sales manager \n'
                         'Lets Grow - Remote, DC',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Responsible for sales in North Amerika and implementation of Letsgrow with new customers.')
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('02/2017 to 08/2019',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Project manager \n'
                         'Horti-Group - King George, VA',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Managed greenhouse strawberry cultivation test for strawberry and young plant production. '
                    'Was responsible for all food regulation compliance and IPM/climate/growing strategy'),
                html.Li(
                    'Managed annual fern production of 70.000 ferns. '
                    'Responsible for the harvest and growing of the crop'),
                html.Li(
                    'Managed the Priva climate control system of the greenhouse including maintenance. '
                    'Trained/guided tenants on how to optimally use the system')
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('01/2015 to 02/2017',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Entrepreneur \n'
                         'Beyo-Plants - Stevensburg, VA',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Owned a plant import business selling hydroponic ornamental plants. '
                    'Sold product to major grocery chains through Color Orchids.')
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('01/2014 to 01/2015',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Project analyst \n'
                         'Sion Orchids - De Lier, The Netherlands',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Developed sales and researched the Phalanopsis market in the USA.')
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('01/2012 to 12/2013',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Project manager \n'
                         'Van Den Berg Roses - Delftgouw, The Netherlands',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Responsible for several key projects to expand the ornamental product assortment in the Chinese '
                    'location. Provided project management support and cultivation support for the crop production '
                    'tests')
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('01/2011 to 01/2012',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Assistant general manager \n'
                         'Van Den Berg Roses - Kunming, China',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Responsible for sales and the supplychain. Managed 12 fte and drove several improvements in the '
                    'coldchain recommmended in my final thesis.')
            ])
        ], width=5)
    ], justify='center'),

    dcc.Markdown('### Education', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2010',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Bachelor: Business Administration\n'
                         'Hogeschool Inholland - Delft, The Netherlands',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5)
    ], justify='center'),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('Achievements \n',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Initiated research out of curriculim reseach on Dutch companies entering the Chinese market.'
                    'Found three companies willing to fund the research and facilitate field visits to the 12 companies '
                    'throughout China.'
                    'Summarized all experiences and presented these findings in a symposium attended by 180 people.'),
                html.Li('Won competition to compete in the USA IFAMA agriculture business case competition and was '
                        'selected to represent university. Placed third out of a total of 20 international teams.')
            ])
        ], width=7),
    ], justify='center'),
    html.Hr(),
    dbc.Row([
        dbc.Card(
            style={"width": "48%", "padding": "0px"},
            children=[
                dash_player.DashPlayer(
                    id="player",
                    url="https://www.youtube.com/watch?v=EDftTdmK9nc",
                    controls=True,
                    width="100%",
                    height="250px",
                )]
        ),
    ], justify='center'),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('2006',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('MBO: Greenhouse management\n'
                         'Holland College - De Lier, The Netherlands',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5)
    ], justify='center')
])