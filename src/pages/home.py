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
                 'My ability to adapt and learn in a fast paced changing environment makes '
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
            dcc.Markdown('2023 Sep to Current', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Logistics Engineer & Data Analyst at DSV North America', style={'textAlign': 'center'}),
            dcc.Markdown(
                'Cost Saving and Network Optimization:\n'
                '- Conducted analyses to identify cost-saving opportunities in Ford\'s logistics network.\n'
                '- Identified areas for network optimization to enhance efficiency and reduce expenses.\n'
                '- Used data analysis techniques to uncover trends, inefficiencies, and areas for improvement.\n'
                'Program Targets:\n'
                '- Collaborated with Ford stakeholders to set clear targets for cost-saving and optimization.\n'
                '- Incorporated feedback on shipping timelines and cost priorities into target-setting.\n'
                '- Ensured targets aligned with Ford\'s logistics goals and objectives.\n'
                'Dashboard Development:\n'
                '- Created interactive dashboards with Power BI and Python\'s Dash to visualize key metrics.\n'
                '- Designed dashboards for real-time insights into program health and progress.\n'
                '- Regularly reviewed dashboards with stakeholders to monitor performance and identify improvements.\n'
                'Forecasting Trends:\n'
                '- Developed forecasting models using Scikit-learn and Facebook Prophet to predict volume and timeline trends.\n'
                '- Leveraged historical data for accurate forecasts to support decision-making.\n'
                '- Integrated trends into program targets and strategies to address future challenges.\n'
                'Achievements:\n'
                '- Conducted a study using Python, Py3DBP, Pandas, Plotly, and Jupyter Notebooks to analyze packing volume '
                'and container stuffing, showing 20% optimization potential for the Ford FCSD program.\n'
                '- Developed a Power BI dashboard for in-depth transit time analysis, comparing actual transit times \n'
                'against contracted times with ocean carriers.\n'
                '- Added a Data Analyst role, enabling the creation of Power BI dashboards for customer presentations.\n'
                '- Automated several manual processes using Power Automate.\n'
                '**Skills:** Data Analysis · Data Modeling · Key Metrics · DAX · Problem Solving · Python · Microsoft Power Query · Power BI · Analytics · Data Models · Supply Chain Optimization · Query Writing · Data Quality · Data Manipulation',
                style={'white-space': 'pre'},
                className='ms-3'
            )
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2023 June to 2023 Aug', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown(
                'In a period of professional reflection following a layoff, I made a decisive move towards a field that \n'
                'has always fascinated me: data analytics. With a firm resolve to pivot my career into data science, \n'
                'I enrolled in the GW Data Analytics Boot Camp. This program is not just an educational endeavor; \n'
                'it\'s a bridge to the thriving and transformative field of data science, offering a comprehensive \n'
                'curriculum that turns raw data into actionable insights. During this time, I also had the privilege \n'
                'of spending three amazing months with my daughter, who was 1.5 years old at the time, enjoying the Michigan summer.\n',
                style={'white-space': 'pre'},
                className='ms-3'
            )
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2022 Aug to 2023 May', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Supply Chain Analytics Manager \n'
                         'Urbanstems - Remote, MI',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Automated multiple supply chain analyses and reports using Python and SQL with '
                        'Mode Analytics UI. Enabled team members to run analyses daily instead of weekly through '
                        'significantly reducing time and labor required to create reports. Facilitated faster '
                        'identification of issues and enabled the team to address issues as they developed.'),
                html.Li('Developed an extensive Python dashboard to analyze non-optimal shipments. Created time series '
                        'analysis to facilitate daily analysis into inventory availability and developed logic to '
                        'identify non-optimal shipment orders due to inventory availability. Created a function that '
                        'allows users to run analysis for a longer time period to identify and address ongoing '
                        'inventory issues.'),
                html.Li('Developed a Python dashboard to enable the identification of high-level trends and '
                        'facilitate deep dive analyses into plant and flower quality issues occurring in outbound '
                        'shipping. Team members gained insight into quality issue trends and took appropriate '
                        'corrective action due to utilizing the dashboard.')
            ])
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2021 Oct to 2022 Aug', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('NonFloral Procurement Manager \n'
                         'Urbanstems - Remote, MI',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Developed models to identify where additional fulfillment locations are needed. Onboarded '
                        'West Coast third-party fulfillment partner carrying a complete product assortment based '
                        'on this model, resulting in a reduction of outbound shipping costs and improved product quality.'),
                html.Li(
                    'Implemented product shelf-life tracking for the internal HUB network. The tracking system extended '
                    'overall shelf life and delivered a higher quality product to the end consumer.'),
                html.Li('Developed analyses of SKUs for each state to identify factors impacting product profit margin '
                        'and developed an action plan to improve performance for each issue.'),
                html.Li('Based improvement plan for the distribution network on this analysis '
                        'and presented this to senior leadership.'),
                html.Li('Delivered improvements in quality control, reduced the complaint rate for Valentine\'s Day '
                        '2022 to 3% from 10% in 2021.'),
                html.Li('Managed two associates by guiding the creation of personal development goals, assigning '
                        'responsibilities, monitoring team goals, and problem-solving with associates when necessary '
                        'to maintain progress.')
            ])
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2020 Jan to 2021 Oct', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Head of Fulfillment \n'
                         'Urbanstems - On Site, DC',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    "Responsible for the internal fulfillment network consisting of three same-day fulfillment locations "
                    "and one warehouse. The team consisted of three managers and twenty hourly employees."),
                html.Li('Redesigned and optimized the order fulfillment process to handle significantly '
                        'increased volume in sales.'),
                html.Li('Responsible for IT support of guided fulfillment system, including purchase, installment, '
                        'and maintenance of hardware needed for increased fulfillment capacity.'),
                html.Li('Developed analytical tools in Looker and Google Sheets to track labor costs, allowing for '
                        'detailed analysis of the utilization of labor hours, resulting in a reduction of labor cost by 15%.'),
                html.Li('Led dried bouquet product development. Implemented, designed, and managed overall '
                        'production process.')
            ])
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2019 Aug to 2019 Dec', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Sales Manager \n'
                         'Lets Grow - Remote, DC',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Responsible for sales in North America and implementation of Letsgrow with new customers.')
            ])
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2017 Feb to 2019 Aug', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Project Manager \n'
                         'Horti-Group - King George, VA',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Provided technical expertise for Priva software to tenants, enabling them to save energy and '
                        'optimize production of crops in the 55-acre greenhouse facility. Solved technical problems with '
                        'Priva software and the underlying IO network.'),
                html.Li('Responsible for producing and cultivating 70,000 Boston Ferns for spring sales. Managed '
                        'climate control, chemical crop protection, watering strategy, and fertilizer schedule. '
                        'Organized production of orders with a team of 10 employees.'),
                html.Li('Responsible for the organization and scheduling of regular maintenance of the greenhouse and '
                        'equipment. Created a program with Access to organize the maintenance tasks and track employee '
                        'hours and inventory of spare parts.'),
                html.Li('Conducted 1.5 Acre production test of strawberry young plants. Managed climate control, '
                        'integrated chemical crop protection, biological crop protection, watering strategy, and '
                        'fertilizer schedule.')
            ])
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2015 Jan to 2017 Feb', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Entrepreneur \n'
                         'Beyo-Plants - Stevensburg, VA',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Developed plant concepts of Spathiphyllum grown in water and the Albuca Spiralis. '
                        'Managed product import from Europe, production, climate control, chemical crop protection, '
                        'watering strategy, and fertilizer schedule. Managed the production and shipping of orders '
                        'with a team of 6 employees.')
            ])
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2014 Jan to 2015 Jan', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Project Analyst \n'
                         'Sion Orchids - De Lier, The Netherlands',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Conducted market research into Phalaenopsis market in the USA.'),
                html.Li('Developed an assortment of varieties that could be profitably sold in the United States.')
            ])
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2012 Jan to 2013 Dec', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Project Manager \n'
                         'Van Den Berg Roses - Delfgouw, The Netherlands',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Managed project to establish production of a broader product assortment for the location '
                        'in China. The product assortment offered, produced, and sold by Van den Berg Roses grew '
                        'from 2 to 8 products.')
            ])
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2011 Jan to 2012 Jan', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Assistant General Manager \n'
                         'Van Den Berg Roses - Kunming, China',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Implemented the conclusions from student thesis into the sales strategy of Van den Berg Roses. '
                    'Sales moved from 98% sales through the Dounan flower auction and 2% sales through the internal '
                    'sales department to 100% sales through internal sales department.'),
                html.Li('Developed new packing method for the product, enabling Van den Berg Roses to ship product '
                        'utilizing the existing cold chain while maintaining product quality.'),
                html.Li('Helped develop three brands to help floral wholesalers distinguish themselves from '
                        'competition in the local market, increasing sales by 50%.')
            ])
        ], width=7)
    ], justify='center'),

    dcc.Markdown('### Education', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2010', style={'textAlign': 'center'})
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
            dcc.Markdown('Achievements', style={'white-space': 'pre'}, className='ms-3'),
            html.Ul([
                html.Li('Initiated research out of curriculum research on Dutch companies entering the Chinese market. '
                        'Found three companies willing to fund the research and facilitate field visits to the 12 companies '
                        'throughout China. Summarized all experiences and presented these findings in a symposium attended by 180 people.'),
                html.Li('Won competition to compete in the USA IFAMA agriculture business case competition and was '
                        'selected to represent the university. Placed third out of a total of 20 international teams.')
            ])
        ], width=7)
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