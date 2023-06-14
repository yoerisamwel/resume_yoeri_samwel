import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
from .side_bar import sidebar
from dash.dependencies import Input, Output
import pandas as pd
from dash_bootstrap_templates import load_figure_template
import requests

dash.register_page(__name__, title="Today's weather API")

load_figure_template(["SUPERHERO"])

#-----------------------------------------------------------------------------------------------------------------------
#weather API documentation
#https://weatherstack.com/documentation

#categories to pull from weather api for use in the app
categories=["Last weather data pull","Temperature in Celsius","Wind speed in meter per second",
            "Expected rain amount in centiliters","Relative humidity","Cloud cover",
            "The feels like temperature","uv index"]

def update_weather():
    weather_requests = requests.get(
        "http://api.weatherstack.com/current?access_key=ed70eba547a6b7e20b465d953d5e491d&query=Detroit"
    )
    json_data = weather_requests.json()
    df = pd.DataFrame(json_data)
    print(df)
    df2 = df.rename({"observation_time": "Last weather data pull", "wind_speed": "Wind speed in meter per second",
                     "temperature": "Temperature in Celsius","precip": "Expected rain amount in centiliters",
                     "humidity": "Relative humidity", "cloudcover": "Cloud cover",
                     "feelslike": "The feels like temperature","uv_index": "uv index"})
    print(df2)
    return([
            html.Table(
                className='table-weather',
                children=[
                    html.Tr(
                        children=[
                            html.Td(
                                children=[
                                    name+": "+str(data)
                                ]
                            )
                        ]
                    )
            for name,data in zip(categories,df2['current'][categories])
        ])
    ])

#-------------------------------------------------------------------------------

def layout():
    return html.Div([
        dbc.Row([
                dbc.Col(
                    [
                        sidebar()
                    ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

                dbc.Col([
                    dbc.Card([
                        dcc.Interval(
                            id='my_interval',
                            disabled=False,
                            n_intervals=0,
                            interval=43200 * 1000,  # increment the counter n_intervals every 5 minutes
                            max_intervals=100,  # number of times the interval will be fired.
                        ),
                        html.Div([
                            html.Div(id="weather", children=update_weather()
                                     )
                            ])
                        ])
                    ], width=4)
                ])


    ])


#-------------------------------------------------------------------------------
# Callback to update news
@callback(Output("weather", "children"), [Input("my_interval", "n_intervals")])
def update_weather_div(n):
    return update_weather()