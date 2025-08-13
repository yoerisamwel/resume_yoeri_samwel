import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
from .side_bar import sidebar
from dash_bootstrap_templates import load_figure_template
from pathlib import Path

# Main registering section
dash.register_page(__name__, title='Projects', order=1)
load_figure_template(["SUPERHERO"])

# ----- Load long descriptions from /work_projects as Markdown -----
# Here I added the logic to show a snapshot and then when the visitor click on the project it takes them to that page
APP_ROOT = Path(__file__).resolve().parents[1]  # app root (parent of /pages)
CANDIDATES = [
    APP_ROOT / "work_projects",          # e.g., /work_projects
    APP_ROOT / "pages" / "work_projects" # e.g., /pages/work_projects
]
MD_DIR = next((p for p in CANDIDATES if p.exists()), CANDIDATES[0])
print(f"[projects] Using Markdown dir: {MD_DIR}")

def read_md(slug: str) -> str:
    fp = (MD_DIR / f"{slug}.md")
    if not fp.exists():
        print(f"[projects] Markdown not found: {fp}")
        return "*Details coming soon.*"
    return fp.read_text(encoding="utf-8")

projects = [
    {
        "id": 1,
        "slug": "ford-transit-time",
        "title": "Transit Time Optimization",
        "summary": "Proactive transit-time monitoring allowing for early detection of carrier vessel schedule issues."
                   "Enebeling the team to proactive adjust the inventory in transit planning and reduce Air Freight spend.",
        "details": read_md("ford-transit-time"),
    },
    {
        "id": 2,
        "slug": "dynamic_utlization",
        "title": "Dynamic Container Utilization",
        "summary": "Optimized container utilization from order to stuffing through end-to-end supply chain analysis, identifying 40% savings potential."
                "Developed scenario-based tools enabling senior leadership to make data-driven cost and efficiency decisions.",
        "details": read_md("dynamic_utlization"),
    },
]

def make_card(p):
    return dbc.Card([
        dbc.CardHeader(p["title"]),
        dbc.CardBody([
            html.P(p["summary"], className="card-text"),
            dbc.Collapse(
                dbc.Card(
                    dbc.CardBody(
                        dcc.Markdown(p["details"], link_target="_blank")  # <-- render Markdown
                    )
                ),
                id={"type": "collapse", "index": p["id"]},
                is_open=False
            ),
            dbc.Button("View Details", href=f"/work_projects/{p['slug']}", color="primary", className="mt-2")
        ])
    ], className="mb-3 rounded-3")

# Projects page layout

def layout():

    return html.Div([
        html.H3("Professional Projects", style={'textAlign': 'center'}, className='my-3'),
        html.Hr(),
        *[
            dbc.Row(
                dbc.Col(make_card(p), width=12),
                className="mb-2"
            )
            for p in projects
        ],
        html.H3("George Washington Data Analytics Bootcamp Projects", style={'textAlign': 'center'}, className='my-3'),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader("Regional Retail Insights (Group Project 4)"),
                        dbc.CardBody(
                            [
                                html.P(
                                    "Segmentation of shopping behavior across regions to surface growth opportunities. "
                                    "Identifies seasonal and local effects to tailor promotions and assortments.",
                                    className="card-text"),
                                dbc.Button("Go to GitHub", href="https://github.com/yoerisamwel/GWU-Project-4",
                                           color="primary", external_link=True, target="_blank")
                            ]
                        )
                    ],
                    className="rounded-3"
                )
            ], width=6),
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader("NYC Coffee Chain Comparator (Group Project 3)"),
                        dbc.CardBody(
                            [
                                html.P("Web app to compare price points and ratings across NYC coffee chains. "
                                       "Benchmarks brands against Starbucks, Dunkin’, and Tim Hortons.",
                                       className="card-text"),
                                dbc.Button("Go to GitHub", href="https://github.com/yoerisamwel/GWU-Project-3",
                                           color="primary", external_link=True, target="_blank")
                            ]
                        )
                    ],
                    className="rounded-3"
                )
            ], width=6)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader("Home Sales with PySpark"),
                        dbc.CardBody(
                            [
                                html.P("Distributed analysis of home sales using PySpark with data in S3. "
                                       "Builds session, transforms data, and computes market-level metrics.",
                                       className="card-text"),
                                dbc.Button("Go to GitHub", href="https://github.com/yoerisamwel/Home_Sales",
                                           color="primary", external_link=True, target="_blank")
                            ]
                        )
                    ],
                    className="rounded-3"
                )
            ], width=6),
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader("Grant Success Classifier (Deep Learning)"),
                        dbc.CardBody(
                            [
                                html.P("Binary classifier to predict nonprofit funding outcomes with Keras/TensorFlow. "
                                       "Cleans features, tunes architecture, and evaluates model performance.",
                                       className="card-text"),
                                dbc.Button("Go to GitHub",
                                           href="https://github.com/yoerisamwel/deep-learning-challenge",
                                           color="primary", external_link=True, target="_blank")
                            ]
                        )
                    ],
                    className="rounded-3"
                )
            ], width=6)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader("US COVID 2022 Analysis (Group Project 1)"),
                        dbc.CardBody(
                            [
                                html.P("Explores correlates of infections, hospitalizations, deaths, and vaccinations. "
                                       "Combines public data to uncover state-level drivers and trends.",
                                       className="card-text"),
                                dbc.Button("Go to GitHub", href="https://github.com/yoerisamwel/1st_GWU_group_project",
                                           color="primary", external_link=True, target="_blank")
                            ]
                        )
                    ],
                    className="rounded-3"
                )
            ], width=6),
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader("Crowdfunding ETL Pipeline (Group Project 2)"),
                        dbc.CardBody(
                            [
                                html.P("Team-built ETL in Jupyter to extract, transform, and load crowdfunding data. "
                                       "Normalizes tables and prepares analysis-ready outputs.",
                                       className="card-text"),
                                dbc.Button("Go to GitHub",
                                           href="https://github.com/yoerisamwel/Crowdfunding_ETL",
                                           color="primary", external_link=True, target="_blank")
                            ]
                        )
                    ],
                    className="rounded-3"
                )
            ], width=6)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader("Crypto Clustering with K-Means & PCA"),
                        dbc.CardBody(
                            [
                                html.P("Unsupervised learning on cryptocurrency features to discover structure. "
                                       "Scales data, reduces dimensions with PCA, and clusters via K-Means.",
                                       className="card-text"),
                                dbc.Button("Go to GitHub", href="https://github.com/yoerisamwel/CryptoClustering",
                                           color="primary", external_link=True, target="_blank")
                            ]
                        )
                    ],
                    className="rounded-3"
                )
            ], width=6),
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader("Earthquake Mapping with Leaflet"),
                        dbc.CardBody(
                            [
                                html.P("Interactive geospatial visualization of seismic activity using Leaflet.js. "
                                       "Plots magnitudes, depths, and overlays for intuitive exploration.",
                                       className="card-text"),
                                dbc.Button("Go to GitHub",
                                           href="https://github.com/yoerisamwel/leaflet-challenge",
                                           color="primary", external_link=True, target="_blank")
                            ]
                        )
                    ],
                    className="rounded-3"
                )
            ], width=6)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader("Eat Safe, Love: MongoDB NoSQL"),
                        dbc.CardBody(
                            [
                                html.P("Hands-on MongoDB project covering ingestion, cleaning, and CRUD operations. "
                                       "Queries and transforms UK food establishment data in Jupyter.",
                                       className="card-text"),
                                dbc.Button("Go to GitHub",
                                           href="https://github.com/yoerisamwel/nosql-challenge/tree/main",
                                           color="primary", external_link=True, target="_blank")
                            ]
                        )
                    ],
                    className="rounded-3"
                )
            ], width=6),
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader("Credit Risk: Logistic Regression"),
                        dbc.CardBody(
                            [
                                html.P("Supervised ML to predict loan status using financial features. "
                                       "Trains and evaluates logistic regression for risk classification to analyze credit risk",
                                       className="card-text"),
                                dbc.Button("Go to GitHub",
                                           href="https://github.com/yoerisamwel/credit-risk-classification",
                                           color="primary", external_link=True, target="_blank")
                            ]
                        )
                    ],
                    className="rounded-3"
                )
            ], width=6)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader("Mars News & Weather Scraper"),
                        dbc.CardBody(
                            [
                                html.P(
                                    "Scrapes Mars news titles/previews and weather tables with BeautifulSoup/Splinter. "
                                    "Cleans, analyzes, and visualizes insights with Pandas.",
                                    className="card-text"),
                                dbc.Button("Go to GitHub",
                                           href="https://github.com/yoerisamwel/Beautiful-Soup-GWU-challenge/tree/main",
                                           color="primary", external_link=True, target="_blank")
                            ]
                        )
                    ],
                    className="rounded-3"
                )
            ], width=6),
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader("Climate API with SQLAlchemy & Flask"),
                        dbc.CardBody(
                            [
                                html.P("ORM-driven analysis of climate data with a Flask JSON API. "
                                       "Serves precipitation, stations, TOBS, and date-range stats from SQLite.",
                                       className="card-text"),
                                dbc.Button("Go to GitHub",
                                           href="https://github.com/yoerisamwel/sqlalchemy-challenge/tree/main",
                                           color="primary", external_link=True, target="_blank")
                            ]
                        )
                    ],
                    className="rounded-3"
                )
            ], width=6)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader("Weather → Vacation (API Project)"),
                        dbc.CardBody(
                            [
                                html.P(
                                    "Pulls weather via OpenWeatherMap and hotels via Geoapify to score destinations. "
                                    "Analyzes latitude correlations and maps candidate cities with hvPlot.",
                                    className="card-text"),
                                dbc.Button("Go to GitHub", href="https://github.com/yoerisamwel/python-api-challenge",
                                           color="primary", external_link=True, target="_blank")
                            ]
                        )
                    ],
                    className="rounded-3"
                )
            ], width=6),
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader("Employee Database: Relational SQL Design"),
                        dbc.CardBody(
                            [
                                html.P("PostgreSQL schema from a fictional HR dataset with ERD-driven modeling. "
                                       "Implements keys/relationships and runs analytical SQL queries.",
                                       className="card-text"),
                                dbc.Button("Go to GitHub",
                                           href="https://github.com/yoerisamwel/sql-challenge",
                                           color="primary", external_link=True, target="_blank")
                            ]
                        )
                    ],
                    className="rounded-3"
                )
            ], width=6)
        ]),
    html.H3("Personal Projects on Github", style={'textAlign': 'center'}, className='my-3'),
    html.Hr(),
    dbc.Row([  # Row starts here
        dbc.Col([  # Column inside the row
            dbc.Card(
                [
                    dbc.CardHeader("Dash Resume Website"),
                    dbc.CardBody(
                        [
                            html.P("My professional portfolio website highlighting data-driven supply chain optimization projects, blending logistics expertise with advanced analytics.", className="card-text"),
                            dbc.Button("Go to GitHub", href="https://github.com/yoerisamwel/resume_yoeri_samwel/tree/master",
                                       color="primary", external_link=True, target="_blank")
                        ]
                    )
                ],
                #style={"width": "18rem"},  # Adjust size as needed
                className="rounded-3"  # Rounded edges
            )
        ], width=6)
    ])
    ])

@callback(
    Output({"type": "collapse", "index": dash.MATCH}, "is_open"),
    Input({"type": "open-btn", "index": dash.MATCH}, "n_clicks"),
    State({"type": "collapse", "index": dash.MATCH}, "is_open")
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
