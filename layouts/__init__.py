import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from layouts import model_filters, detail_display

main_layout = [
    dbc.Row(
        className="mt-auto",
        children=[
            dbc.Col(
                children=[
                    dbc.CardBody(
                        [
                            html.H5("Car Insurance Claim Simulation", className="card-title"),
                            dcc.Markdown(
                                "This is a simple interface to simulate the **expected value and distribution of claim "
                                "amounts** on car insurance policy with selected parameters. Other model parameters "
                                "are randomly sampled from the original dataset. Under the hood of the simulation is a "
                                "**TweedieRegressor** model with a Power parameter of 1.5.",
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
                md=6,
                className="shadow-sm bg-white",
                children=[
                    dcc.Loading(
                        id="loading-div",
                        type="circle",
                        children=dcc.Graph()
                    ),

                ]
            ),
            dbc.Col(
                md=2,
                children=detail_display.layout
            ),

            dbc.Col(
                md=3,
                children=model_filters.layout
            )
        ]
    )
]