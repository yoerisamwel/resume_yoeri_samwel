import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
from .side_bar import sidebar
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from datetime import datetime as dt
from dash_bootstrap_templates import load_figure_template


dash.register_page(__name__, title='Inventory dashboard')

load_figure_template(["SUPERHERO"])

#-----------------------------------------------------------------------------------------------------------------------
#importing data/csv's
df_stock = pd.read_csv('https://raw.githubusercontent.com/yoerisamwel/raw_data/master/stock_data_out.csv')
df_categories = pd.read_csv('https://raw.githubusercontent.com/yoerisamwel/raw_data/master/categories.csv')

df_stock = df_stock.drop(['Unnamed: 0'], axis=1)
df_stock['date_index'] = df_stock['date_day']
df_stock['date_index'] = pd.to_datetime(df_stock['date_index'])
df_stock['date_day'] = pd.to_datetime(df_stock['date_day'])
df_categories['product_category'] = df_categories.color_group
df_categories.product_category.fillna(df_categories.candy_group, inplace=True)
df_categories.product_category.fillna(df_categories.vase_group, inplace=True)
df_categories_2 = df_categories.drop(['color_group','candy_group','vase_group'], axis=1)
df_stock2 = df_stock.merge(df_categories_2, on='product', how='left')
df_stock2.set_index('date_index', inplace=True)
#-----------------------------------------------------------------------------------------------------------------------


def layout():
    return html.Div([
        dbc.Row(
            [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("Date range", style={'fontSize': 20, 'textAlign': 'center'}),
                    dbc.CardBody(
                        dcc.DatePickerRange(
                            id='date_picker_range',
                            calendar_orientation='horizontal',
                            day_size=39,
                            end_date_placeholder_text="Return",
                            with_portal=False,
                            first_day_of_week=0,
                            reopen_calendar_on_clear=True,
                            is_RTL=False,
                            clearable=True,
                            number_of_months_shown=1,
                            start_date=dt(2022, 7, 1).date(),
                            end_date=dt(2022, 7, 30).date(),
                            display_format='MMM Do, YY',
                            month_format='MMMM, YYYY',
                            minimum_nights=1,
                            persistence=True,
                            persisted_props=['start_date'],
                            persistence_type='session',
                            updatemode='singledate'
                        )
                    )
                ], style={"height": 185})
            ], md=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("Product group:", style={'fontSize': 20, 'textAlign': 'center'}),
                    dbc.CardBody(
                        dcc.Dropdown(
                            id='product_group_dpdn',
                            options=[{'label': s, 'value': s} for s in sorted(df_stock2.product_group.unique())],
                            value='bouquet',
                            clearable=False
                        )
                    )
                ], style={"height": 185})
            ], md=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("Product Category:", style={'fontSize': 20, 'textAlign': 'center'}),
                    dbc.CardBody(dcc.Dropdown(id='product_category_dpdn', options=[], multi=True))
                ], style={"height": 185})
            ], md=4)
        ], className="mb-4"),
        dbc.Row([
            dbc.Col(
                dcc.Graph(id='daterange_per_fc_sales_chloro_graph', figure={},
                          config={'staticPlot': False, 'scrollZoom': True, 'doubleClick': 'reset',
                                  'showTips': False, 'displayModeBar': True, 'watermark': True}
                          )
                , width=6)
        ], className="mb-4")
],className="dbc")

#-------------------------------------------------------------------

@callback(
    Output(component_id='product_category_dpdn', component_property='options'),
    [Input(component_id='product_group_dpdn', component_property='value'),
     Input(component_id='date_picker_range', component_property='start_date'),
     Input(component_id='date_picker_range', component_property='end_date')]
)
def set_cities_options(chosen_product_group,start_date,end_date):
    df = df_stock2.sort_index().loc[start_date:end_date]
    dff = df[df.product_group == chosen_product_group]
    return [{'label': c, 'value': c} for c in sorted(dff.product_category.unique())]

@callback(
    Output('product_category_dpdn', 'value'),
    Input('product_category_dpdn', 'options')
)
def set_cities_value(available_options):
    return [x['value'] for x in available_options]


@callback(
    [Output(component_id='daterange_per_fc_sales_chloro_graph', component_property='figure')],
    [Input(component_id='product_category_dpdn', component_property='value'),
     Input(component_id='product_group_dpdn', component_property='value'),
     Input(component_id='date_picker_range', component_property='start_date'),
     Input(component_id='date_picker_range', component_property='end_date')]
)
def update_grpah(selected_product_category,chosen_product_group, start_date, end_date):
    df = df_stock2.sort_index().loc[start_date:end_date]
    if len(chosen_product_group) == 0:
        return dash.no_update
    else:
        chosen_product_group_li = chosen_product_group.split(",")
        dff = df[(df.product_category.isin(selected_product_category)) & (df.product_group.isin(chosen_product_group_li))]
        dff = dff.drop(['date_day'], axis=1)
        dff2 = dff.groupby(['product_category', 'distribution_point_city'])['units_sold'].sum().reset_index()
        dff3 = dff2.pivot_table(index=["product_category"], columns=["distribution_point_city"], values="units_sold")
        fig = px.imshow(dff3, color_continuous_scale=px.colors.sequential.Plasma,
                        title="Units sold per distribution center",height=650)
        fig.update_layout(title_font={'size': 27}, title_x=0.5,height=500)
        fig.update_traces(hoverongaps=False,
                          hovertemplate="product: %{y}"
                                        "<br>distribution_point_city: %{x}"
                                        "<br>units_sold: %{z}<extra></extra>"
                          )

        return [fig]


