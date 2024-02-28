import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import requests
import re
from .side_bar import sidebar
from dash_bootstrap_templates import load_figure_template

dash.register_page(__name__, title='Projects', order=1)

load_figure_template(["SUPERHERO"])


def layout():
    USERNAME = "yoerisamwel"
    REPOSITORY = "GWU-Project-3"  # Just the repository name
    BRANCH = "main"  # Branch name
    README_URL = f"https://raw.githubusercontent.com/{USERNAME}/{REPOSITORY}/{BRANCH}/README.md"

    try:
        readme_content = requests.get(README_URL).text
        # Replace 'screenshots' with 'assets' in the image paths
        modified_content = re.sub(r'\(screenshots/', r'(assets/', readme_content)

        # Convert Markdown content to HTML, including the className for custom CSS styling
        return html.Div([
            dcc.Markdown(modified_content, className="markdown-body")
        ])
    except Exception as e:
        return html.Div([
            html.P("Failed to load README content"),
            html.P(str(e))
        ])