import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from layouts import model_filters

main_layout = [
    dbc.Row(
        className="mt-auto",
        children=[
            dbc.Col(
                children=[
                    dbc.CardBody(
                        [
                            html.H5("Car Insurance Claim Simulation", className="card-title"),
                            html.P(
                                "This is a simple interface to simulate expected value and disribution of claim "
                                "amount depending on a few parameters. Under the hood of the simulation is a "
                                "TweedieRegressor model with Power parameter 1.5 ",
                                className="card-text",
                            ),
                            dbc.Button(
                                "More info in github repo", color="success", className="mt-auto",
                                href="https://github.com/rmilosic/insurance-claim-prediction/blob/"
                                     "master/notebooks/exploratory_data_analysis.ipynb",
                                external_link=True
                            ),
                        ]
                    )
                ]
            )
        ]
    ),
    dbc.Row(
        className="justify-content-between",
        children=[
            dbc.Col(
                md=8,
                className="shadow-sm bg-white",
                children=[
                    dcc.Graph(
                        id="trend-graph-absolute"
                    )
                ]
            ),

            dbc.Col(
                md=3,
                children=model_filters.layout
            )
        ]
    )
]