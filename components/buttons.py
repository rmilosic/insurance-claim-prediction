import dash_bootstrap_components as dbc


submit_button = dbc.Button(
    "Simulate",
    id="submit-model-simulation",
    color="success",
    className="mt-auto",
    block=True,
    n_clicks=0
)
