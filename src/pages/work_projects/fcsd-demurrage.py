import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/work_projects/fcsd-demurrage",
    name="Container Demurrage"
)

layout = dbc.Container([
    # Title & short intro
    html.H2("Container Demurrage Analysis"),
    html.P(
        "Analyzing container pool dynamics to identify drivers of demurrage cost and quantify their impact across FCSD warehouses.",
        className="text-muted"
    ),

    html.Hr(),

    # Problem statement
    html.H4("Problem statement"),
    html.P(
        "FCSD warehouses maintain container pools with a limited number of free days per carrier. "
        "After free days expire, demurrage accrues daily. The team suspected hazardous documentation "
        "processing times prolonged on-site dwell, increasing demurrage costs."
    ),

    # Current products
    html.H4("Current products"),
    html.Ul([
        html.Li("Project44 visibility data."),
        html.Li("Multiple Excel workbooks used to manage container pool levels and events.")
    ]),

    # Analysis description
    html.H4("Analysis description"),
    html.Ul([
        html.Li("Restructured the data into a daily event timeline per container with current status to visualize pool levels by carrier and warehouse."),
        html.Li("Added container pool targets and daily container loads to assess whether pool sizing vs. process delays drove costs."),
        html.Li("Findings indicated pool size/imbalance was a primary driver of demurrage, not only document processing."),
        html.Li("Validated that hazardous documentation processing times frequently exceeded carrier targets."),
        html.Li("Identified a third driver: containers loaded after the weekly earliest rail cut could not depart until the following week, extending dwell."),
    ]),

    html.P(
        "These three factors in combination explained recurring demurrage. "
        "A Power BI report was developed to quantify total demurrage and attribute impact by driver "
        "(pool sizing/imbalance, documentation delays, missed rail cut)."
    ),

    html.Hr(),

    # Visuals (placeholder)
    html.H4("Visuals"),
    html.P("-"),
    html.Img(src="/assets/transit_time_chart.png", style={"maxWidth": "100%", "borderRadius": "12px"}),

    html.Hr(),

    # Impact
    html.H4("Impact"),
    html.Ul([
        html.Li("Clear attribution of demurrage to structural pool sizing vs. process delays."),
        html.Li("Actionable targets for pool levels by carrier/warehouse and SLA tracking for documentation."),
        html.Li("Operational change to guard against loading after rail-cut deadlines."),
        html.Li("Power BI dashboard for ongoing monitoring and cost avoidance.")
    ]),
], fluid=True)