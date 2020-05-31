import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import dash_bootstrap_components as dbc

from callback import register_callbacks
from components import navigation
import layouts


# # load data
# df = pd.read_csv("data/processed/final_dataset_10_19.csv", encoding="utf-8")
#
# years = df.leto.unique()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LITERA], suppress_callback_exceptions=True)
server = app.server     # the Flask app

app.layout = html.Div(
    style={"backgroundColor": "#fafafa"},
    children=[
        dcc.Location(id='url', refresh=False),
        # navigation.layout,
        html.Div(id='page-content')
    ]
)


register_callbacks(app)


# URL ROUTING
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return dbc.Container(
            children=layouts.main_layout
        )
    else:
        return dcc.Location(pathname="/", id="xyxsa")


if __name__ == '__main__':
    app.run_server(debug=True)
