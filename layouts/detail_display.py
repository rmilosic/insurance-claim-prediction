import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


layout = [
    dbc.Row(
        dbc.Col(
            xs=12,
            className="bg-white shadow-sm",
            children=[
                dbc.Row(
                    [
                        dbc.Col(
                            html.Span("Mean expected value"),
                            className="mt-2",
                            xs=12
                        ),
                        dbc.Col(
                            html.P(
                                "-",
                                id="mean-expected-value"
                            ),
                            className="font-weight-bold",
                            xs=12
                        )
                    ],
                    className="text-center")
            ]
        )
    )

]