import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/work_projects/dynamic_utlization", name="Dynamic Container Utilization")

layout = dbc.Container([
    html.H2("Container Utilization Optimization", className="mb-2"),
    html.P(
        "End-to-end analysis from customer order placement to container stuffing, identifying inefficiencies and developing scenarios to guide senior leadership decisions on optimizing utilization and reducing costs.",
        className="text-muted"
    ),
    html.Hr(),

    # Problem statement
    html.H4("Problem statement", className="mt-3"),
    html.P(
        "From the moment a customer places an order to the final container stuffing, multiple supply chain steps determine the final utilization rate. "
        "The customer’s liquid volume utilization per container was consistently below target. Existing tools only measured 'liquid utilization' shipment data, "
        "which did not capture the true dynamic (dimensional) utilization. The challenge was to quantify the issue, identify root causes, and design solutions that could be replicated program-wide."
    ),

    # Stakeholders
    html.H4("Stakeholders", className="mt-4"),
    html.Ul([
        html.Li("Ford FCSD Export Program"),
        html.Li("DSV Advanced Analytics Team"),
        html.Li("DSV eDC (Supply Chain Program) Team"),
        html.Li("Warehouse Operations Teams"),
    ]),

    # Original products
    html.H4("Original products", className="mt-4"),
    html.Ul([
        html.Li("Excel report measuring liquid utilization per container based on shipment data."),
        html.Li("Manual analysis using shipment records.")
    ]),

    # Solutions developed
    html.H4("Solutions developed", className="mt-4"),

    html.H5("Step 1 – Baseline visibility and stakeholder engagement"),
    html.Ul([
        html.Li("More extensive Power BI report showing the utilization over time was developed based on container utilization data captured."),
        html.Li("Visited warehouses to observe stuffing processes, collect operational feedback, and validate data gaps."),
        html.Li("Identified that commercial invoices recorded overpack dimensions but not the true packing efficiency within those overpacks."),
        html.Li("Confirmed overpacks with suboptimal shapes and combinations reduced container stuffing efficiency."),
        html.Li("Noted that re-optimizing freight post-commercial invoice creation was avoided due to administrative burdens.")
    ], className="mb-3"),

    html.H5("Step 2 – Data integration and initial quantification"),
    html.Ul([
        html.Li("Extracted commercial invoice data from PDF and combined with warehouse and shipping datasets."),
        html.Li("Developed Python scripts to clean, combine, and analyze datasets, covering every step from order receipt to container stuffing."),
        html.Li("Estimated optimization potential (~40%) by loading overpack data into a load optimizer for simulated stuffing scenarios."),
        html.Li("Identified lack of volume forecasting per location, leaving operations without a planning tool.")
    ], className="mb-3"),

    html.H5("Step 3 – Scenario development for leadership decision-making"),
    html.Ul([
        html.Li("Created three scenarios to simulate alternative stuffing strategies and quantify savings potential:"),
        html.Li([
            html.Strong("Scenario 1:"), " Ignored warehouse cycle times; stuffed containers optimally based on overpack dimensions to find theoretical minimum container count."
        ]),
        html.Li([
            html.Strong("Scenario 2:"), " Grouped shipments by week; assumed basic dimensional planning available, allowing more effective overpack combinations — showing ~30% savings potential."
        ]),
        html.Li([
            html.Strong("Scenario 3:"), " Assigned cycle time targets per overpack; incorporated FCL/LCL cost models; used Python logic to identify most cost-effective shipping method per combination."
        ]),
        html.Li("All scenarios provided quantified trade-offs for leadership to weigh cost savings vs. operational constraints.")
    ], className="mb-3"),

    html.H5("Step 4 – Scaled analysis with SQLLite, Python Dash, and API-driven optimization"),
    html.Ul([
        html.Li(
            "Received larger datasets (all overpacks and part shipments, plus assumed box shapes) and integrated them into an SQLLite database."),
        html.Li(
            "Stored intermediate analysis results to allow fast UI interaction in Dash without reprocessing raw data."),
        html.Li(
            "Combined full FCL/LCL/AIR shipment data to detect trends and label 'optimizable' volumes — including unexpected AIR shipments to internal warehouses."),
        html.Li(
            "Grouped parts into shape, weight, and recurring volume segments to identify underperforming categories."),
        html.Li(
            "Identified parts as suboptimal when inventory at destination indicated shipments were replenishment moves — where more cost-effective methods should have been chosen."),
        html.Li(
            "Applied Google OR-Tools and an API-driven analysis setup to determine optimal overpack selection according to the 80-20 principle, prioritizing shapes that fit most commonly shipped parts and were easiest to combine."),
        html.Li(
            "Ran simulations on overpack combinations to achieve maximum dynamic utilization while aligning with operational feasibility.")
    ]),

    html.H5("Step 5 – Transition to enterprise-level solutions"),
    html.Ul([
        html.Li([
            html.Strong("Solution 1 (SCM Program): "),
            "Deploy DSV Supply Chain Management tool to automate dataset integration, track order-level events end-to-end, ",
            "enable EDI with the customer, and surface KPIs in Power BI. ",
            "The program will also incorporate dynamic container utilization calculations so utilization is measured natively within the monitoring platform."
        ]),
        html.Li([
            html.Strong("Solution 2 (Advanced Analytics): "),
            "Build and maintain the scenario engine outside the SCM program. ",
            "This service generates optimization scenarios (cycle time targets, FCL/LCL mix, stuffing plans) using Python/Dash and OR-Tools, ",
            "feeding results back to stakeholders for decision-making."
        ])
    ]),

    html.Hr(),

    # Visuals placeholder
    html.H4("Visuals Used In Analysis", className="mt-3"),
    html.Div([
        html.Figure([
            html.Img(
                src="/assets/Box_Volume_Buildup_52832_2024-07-01_to_2024-09-30.jpg",
                alt="Box volume buildup vs 40ft container loads with cycle-time and target thresholds",
                style={
                    "maxWidth": "100%",
                    "borderRadius": "12px",
                    "border": "1px solid #e6e6e6"
                }
            ),
            html.Figcaption(
                "Green = 40ft load events. Blue/red bars = liquid volume buildup by overpack. "
                "Containers often depart under the liquid-volume target due to dynamic utilization and cycle-time triggers. "
                "Lack of forward visibility on orders limits optimal overpack combinations."
            )
        ]),

        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H6("Avg Liquid Fill", className="card-title text-muted"),
                    html.H4("58%", className="card-text text-primary")
                ])
            ], className="text-center"), width=3),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H6("TEU Below Target", className="card-title text-muted"),
                    html.H4("60%", className="card-text text-danger")
                ])
            ], className="text-center"), width=3),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H6("Avoidable TEU", className="card-title text-muted"),
                    html.H4("4 TEU", className="card-text text-warning")
                ])
            ], className="text-center"), width=3),
        ], className="mt-3 g-2")
    ]),

    html.Hr(),

    # Impact
    html.H4("Impact", className="mt-3"),
    html.Ul([
        html.Li("Mapped inefficiencies from customer order entry to container stuffing, pinpointing underutilization causes."),
        html.Li("Quantified cost-saving opportunities up to 40% through scenario-based optimization."),
        html.Li("Provided leadership with actionable trade-offs between cost, cycle times, and operational feasibility."),
        html.Li("Established scalable, repeatable process for utilization analysis and optimization."),
        html.Li("Enabled analysis transition to project to implement enterprise tools for automated monitoring and scenario simulation.")
    ]),

    html.Hr(),

    # Tech stack
    html.H4("Tech stack", className="mt-3"),
    dbc.Stack([
        dbc.Badge("Power BI", color="primary", className="me-2"),
        dbc.Badge("Python", color="secondary", className="me-2"),
        dbc.Badge("Pandas", color="info", className="me-2"),
        dbc.Badge("Dash", color="dark", className="me-2"),
        dbc.Badge("SQLLite", color="success", className="me-2"),
        dbc.Badge("APIs", color="danger", className="me-2"),
    ], direction="horizontal", gap=2, className="mb-4"),

], fluid=True)