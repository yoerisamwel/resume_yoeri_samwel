import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/work_projects/ford-transit-time", name="Ford Transit Time Optimization")

layout = dbc.Container([
    html.H2("Transit Time Optimization", className="mb-2"),
    html.P(
        "Improving transit-time reliability to reduce costly express (AIR) shipments in Ford’s Europe production and FCSD export programs.",
        className="text-muted"
    ),
    html.Hr(),

    # Problem statement
    html.H4("Problem statement", className="mt-3"),
    html.P(
        "Part flows from supplier to plant/customer pass through multiple supply-chain steps. "
        "Each step involves inventory and inter-step transit time. Inventory in-step or in-transit is costly and minimized. "
        "Disruptions increase the risk of express (AIR) shipments, which are significantly more expensive. "
        "The goal of this analysis is to reduce the need for express shipments by improving visibility into transit times and upcoming route changes."
    ),

    # Current products
    html.H4("Original products", className="mt-4"),
    html.Ul([
        html.Li(
            "Routing Guide (manually maintained by logistics engineers). "
            "This manual setup is labor-intensive and difficult to replicate across programs."
        )
    ]),

    # Analysis description
    html.H4("Solutions developed", className="mt-4"),

    html.H5("Power BI Routing Guide (baseline)"),
    html.Ul([
        html.Li("Power BI report to streamline Routing Guide creation and maintenance."),
        html.Li("Transit-time performance analysis vs. Routing Guide, customer contract SLAs, and ocean carrier contracts."),
        html.Li("Enables the customer to measure carrier transit-time performance under contract."),
    ], className="mb-3"),

    html.H5("Proactive Routing Guide (Carrier API-driven)"),
    html.Ul([
        html.Li("Ingests ocean carrier APIs to retrieve published route schedules and transit times with a 180-day look-ahead."),
        html.Li("Detects changes vs. expected schedules to flag weeks with atypical transit times."),
        html.Li("Generates early warnings so operations can mitigate disruptions with cost-effective alternatives before production is impacted."),
        html.Li("Status: in testing."),
    ]),

    html.Hr(),

    # Visuals placeholder
    html.H4("Visuals", className="mt-3"),
    html.P("-", className="mb-2"),
    html.Img(src="/assets/transit_time_chart.png", style={"maxWidth": "100%", "borderRadius": "12px"}),

    html.Hr(),

    # Impact
    html.H4("Impact", className="mt-3"),
    html.Ul([
        html.Li("Earlier detection of carrier schedule shifts and atypical transit times."),
        html.Li("Reduced reliance on expensive express (AIR) shipments."),
        html.Li("Higher schedule adherence and inventory stability across steps."),
        html.Li("Scalable, repeatable process across programs (less manual upkeep)."),
    ]),

    html.Hr(),

    # Tech stack
    html.H4("Tech stack", className="mt-3"),
    dbc.Stack([
        dbc.Badge("Power BI", color="primary", className="me-2"),
        dbc.Badge("Python", color="secondary", className="me-2"),
        dbc.Badge("Pandas", color="info", className="me-2"),
        dbc.Badge("Dash", color="dark", className="me-2"),
        dbc.Badge("APIs (Ocean Carrier)", color="warning", text_color="dark", className="me-2"),
        dbc.Badge("SQL", color="success", className="me-2"),
        dbc.Badge("SharePoint / Dataflows/ Power Automate", color="light", text_color="dark"),
    ], direction="horizontal", gap=2, className="mb-4"),

], fluid=True)