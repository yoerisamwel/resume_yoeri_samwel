import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .side_bar import sidebar
from datetime import datetime as dt
from dash_bootstrap_templates import load_figure_template
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

dash.register_page(__name__, title='Projects', order=1)

load_figure_template(["SUPERHERO"])

#-----------------------------------------------------------------------------------------------------------------------
#importing data/csv's
df_sales = pd.read_csv('https://raw.githubusercontent.com/yoerisamwel/raw_data/master/sales2.csv')
df_geo = pd.read_csv('https://raw.githubusercontent.com/yoerisamwel/raw_data/master/geo_data.csv')
df_sales['purchase_time_index'] = df_sales['purchase_time']
df_sales['purchase_time_index'] = pd.to_datetime(df_sales['purchase_time_index'])
df_sales['purchase_time'] = pd.to_datetime(df_sales['purchase_time'])
df_sales2 = df_sales.copy()
df_sales_geo = df_sales2.merge(df_geo, on='zipcode', how='left')
df_sales2.set_index('purchase_time_index', inplace=True)
df_sales_geo.set_index('purchase_time_index', inplace=True)
df_sales_geo2=df_sales_geo.dropna(subset=['state'])
#df_sales_geo.to_csv('check.csv')

#-----------------------------------------------------------------------------------------------------------------------
#layout


def layout():
    return html.Div([
    dbc.Row([
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("Date range", style={'fontSize': 20, 'textAlign': 'center'}),
                    dbc.CardBody([
                        dcc.DatePickerRange(
                            id='sales_date_range',
                            calendar_orientation='horizontal',
                            day_size=39,
                            end_date_placeholder_text="Return",
                            with_portal=False,
                            first_day_of_week=0,
                            reopen_calendar_on_clear=True,
                            is_RTL=False,
                            clearable=True,
                            number_of_months_shown=1,
                            start_date=dt(2022, 8, 1).date(),
                            end_date=dt(2022, 10, 30).date(),
                            display_format='MMM Do, YY',
                            month_format='MMMM, YYYY',
                            minimum_nights=1,
                            persistence=True,
                            persisted_props=['start_date'],
                            persistence_type='session',
                            updatemode='singledate'
                    )
                ], style={"height": 150})
                    ])
                ])
            ]),
    dbc.Row([
        dbc.Col([
            dbc.CardBody(
                id='sales_bar_1')
                ], width=6)
        ])
    ])
#-------------------------------------------------------------------
#callbacks


@callback(
    Output(component_id='sales_bar_1', component_property='children'),
    Input(component_id='sales_date_range', component_property='start_date'),
    Input(component_id='sales_date_range', component_property='end_date')
    )
def build_bar_graph_1(start_date,end_date):
    df = df_sales2.sort_index().loc[start_date:end_date]
    df = df.drop(['purchase_time'], axis=1)
    dff = df.groupby(['product']).sum().reset_index()
    dff2 = dff.copy()
    fig = px.bar(dff2, x="product", y="revenue", color="product",title = "Sales per product")
    return dcc.Graph(id='Bar1_v1', figure=fig)

'''
@callback(
    Output(component_id='sales_chloromap_1', component_property='children'),
    Input(component_id='sales_analysis_data', component_property='data')
     )
def build_bar_graph_1(data):
    df = pd.DataFrame(data)
    dff = df.groupby(['zipcode'])['adjusted_quantity'].sum().reset_index()
    fig = px.choropleth(dff, geojson=counties, locations='zipcode', color='adjusted_quantity',
                        color_continuous_scale="Viridis",
                        range_color=(0, 12),
                        scope="usa",
                        labels={'adjusted_quantity': 'units sold'}
                        )
    fig.update_layout(margin={"r": 0, "t": 100, "l": 0, "b": 0},title = "Counties generating sales")
    return [dcc.Graph(id='chloro_1_v1', figure=fig)]
'''