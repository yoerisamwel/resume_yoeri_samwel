import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_player

dash.register_page(__name__, path='/', order=0)

layout = html.Div([
    dcc.Markdown('# Yoeri Samwel', style={'textAlign':'center'}),
    dcc.Markdown('Michigan, USA', style={'textAlign': 'center'}),

    dcc.Markdown('### Professional Summary', style={'textAlign': 'center'}),
    html.Hr(),
    dcc.Markdown('I am a dynamic, outgoing person with strong communication skills. \n'
                 'I have experience with python and especially the Dash plotly visualization library \n'
                 'I actively seek opportunities where my analytical skills and creativity can ' 
                 'contribute and help drive change/innovation.\n'
                 'My ability to adapt and learn in a fast paced changing environment makes'
                 'me an asset for organizations.\n'
                 'I firmly believe in continuous learning. I actively seek out opportunities to learn '
                 'new skills that improve me as a professional and as a person.\n'
                 'I thrive working in a group and am excided to lead a team to reach shared goals.\n',
                 style={'textAlign': 'center', 'white-space': 'pre'}),
    dcc.Markdown('### Skills', style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            * Analytical
            * Creative
            * Self-motivated
            * Self-starter
            * Team player
            ''')
        ], width={"size": 3, "offset": 1}),
        dbc.Col([
            dcc.Markdown('''
            * Python 
            * SQL
            * Excel/Google sheets
            * HTML 
            * CSS
            * Looker
            * Mode Analytics
            ''')
        ], width=3)
    ], justify='center'),

    dcc.Markdown('### Work History', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2022 Aug  to 2023 May', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Supply Chain Analytics manager \n'
                         'Urbanstems - Remote, MI',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Automated multiple supply chain analyses and reports using python and SQL with '
                        'Mode Analytics UI. Enabled team members to run analyses daily instead of weekly through '
                        'significantly reducing time and labor required to create reports. Facilitated faster '
                        'identification of issues and enabled the team to address issues as they developed.'),
                html.Li('Developed extensive python dashboard to analyze non-optimal shipments. Created time series '
                        'analysis to facilitate daily analysis into inventory availability and developed logic to '
                        'identify non-optimal shipment orders due to inventory availability. Created function that '
                        'allows user to run analysis for a longer time period to identify and address ongoing '
                        'inventory issues.'),
                html.Li('Developed python dashboard to enable the identification of high-level trends and '
                        'facilitate deep dives analyses into plant and flower quality issues occurring in outbound '
                        'shipping. Team members gained insight into quality issue trends and took appropriate '
                        'corrective action due to utilizing dashboard.')
            ])
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2021 Oct  to 2022 Aug',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('NonFloral Procurement Manager \n'
                         'Urbanstems - Remote, MI',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Developed models to identify where additional fulfillment locations are needed. Onboarded '
                    'West Coast third party fulfillment partner carrying complete product assortment partners based '
                    'on this model, resulting in a reduction of outbound shipping costs and improved product quality.'),
                html.Li(
                    'Implemented product shelf-life tracking for internal HUB network. Tracking system extended '
                    'overall shelf life and delivered a higher quality product to end consumer.'),
                html.Li(
                    'Developed analyses of SKUs for each state to identify factors impacting product profit margin '
                    'and developed action plan to improve performance for each issue.'),
                html.Li(
                    'Based improvement plan for the distribution network on this analysis '
                    'and presented this to senior leadership.'),
                html.Li(
                    'Delivered improvements in quality control, reduced the complaint rate for Valentines Day '
                    '2022 to 3% from 10% in 2021.'),
                html.Li(
                    '-	Managed two associates by guiding creation of personal development goals, assigning '
                    'responsibilities, monitoring team goals and problem solving with associates when necessary '
                    'to maintain progress.')
            ])
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2020 Jan to 2021 Oct',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Head of fulfillment \n'
                         'Urbanstems - On Site, DC',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    "Responsible for internal fulfillment network consisting of three same day fulfillment locations "
                    "and one warehouse. Team consisted of three managers and twenty hourly employees."),
                html.Li(
                    'Redesigned and optimized the order fulfillment process to optimize for significantly '
                    'increased volume in sales.'),
                html.Li(
                    'Responsible for IT support of guided fulfillment system, including purchase, installment '
                    'and maintenance of hardware needed for increased fulfillment capacity.'),
                html.Li(
                    'Developed analytical tools in Looker and Google Sheets to track labor costs, allowing for '
                    'detailed analysis of utilization of labor hours, resulting in a reduction of labor cost by 15%.'),
                html.Li(
                    'Led dried bouquet product development. Implemented, designed and managed overall '
                    'production process.')
            ])
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2019 Aug to 2019 Dec',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Sales manager \n'
                         'Lets Grow - Remote, DC',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Responsible for sales in North America and implementation of Letsgrow with new customers.')
            ])
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2017 Feb to 2019 Aug',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Project manager \n'
                         'Horti-Group - King George, VA',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Provided technical expertise for Priva software to tenants, enabling them to save energy and '
                    'optimize production of crops in the 55-acre greenhouse facility. Solved technical problems with  '
                    'Priva software and the underlying IO network.'),
                html.Li(
                    'Responsible producing and cultivating 70,000 Boston Ferns for spring sales. Managed '
                    'climate control, chemical crop protection, watering strategy and fertilizer schedule. '
                    'Organized production of orders with team of 10 employees. '),
                html.Li(
                    'Responsible for organization and scheduling of regular maintenance of the greenhouse and '
                    'equipment. Created program with Access to organize the maintenance tasks and track employee '
                    'hours and inventory of spare parts.'),
                html.Li(
                    'Conducted 1,5 Acre production test of strawberry young plants. Managed climate control, '
                    'integrated chemical crop protection, biological crop protection, watering strategy and '
                    'fertilizer schedule.')
            ])
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2015 Jan to 2017 Feb',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Entrepreneur \n'
                         'Beyo-Plants - Stevensburg, VA',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Developed plant concepts of Spathypylium grown in water and the Albuca Spiralis. '
                    'Managed product import from Europe, production, climate control, chemical crop protection, '
                    'watering strategy and fertilizer schedule. Managed the production and shipping of orders '
                    'with team of 6 employees. ')
            ])
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2014 Jan to 2015 Jan',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Project analyst \n'
                         'Sion Orchids - De Lier, The Netherlands',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Conducted market research into Phalaenopsis market in the USA.'),
                html.Li(
                    'Developed assortment of varieties that could be profitably sold in the United States.')
            ])
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2012 Jan to 2013 Dec',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Project manager \n'
                         'Van Den Berg Roses - Delftgouw, The Netherlands',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Managed project to establish production of broader products assortment for the location '
                    'in China. Product assortment offered, produced and sold by Van den Berg Roses grew '
                    'from 2 to 8 products.')
            ])
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2011 Jan to 2012 Jan',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Assistant general manager \n'
                         'Van Den Berg Roses - Kunming, China',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Implemented the conclusions from student thesis into the sales strategy of Van den Berg Roses. '
                    'Sales moved from 98% sales through the Dounan flower auction and 2% sales through the internal '
                    'sales department to 100% sales through internal sales department.'),
                html.Li(
                    'Developed new packing method for the product enabling Van den Berg Roses to ship product '
                    'utilizing existing cold chain while maintaining product quality.'),
                html.Li(
                    'Helped develop three brands to help floral wholesalers distinguish themselves from '
                    'competition in the local market, increasing the sales by 50%. ')
            ])
        ], width=7)
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
        ], width=7)
    ], justify='center'),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('Achievements \n',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Initiated research out of curriculum research on Dutch companies entering the Chinese market.'
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