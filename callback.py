import numpy as np
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.figure_factory as ff
import dash_core_components as dcc

from models.claim_amount.tweedie_regressor import TweedieClaimModel

tweedie_model = TweedieClaimModel()


def register_callbacks(app):

    """
    Register app callbacks
    """
    @app.callback(
        [
        # Output('simulation-graph', 'figure'),
         Output('mean-expected-value', 'children'),
         Output('loading-div', 'children')],
        [Input('submit-model-simulation', 'n_clicks')],
        [State('make-select', 'value'),
         State('year-select', 'value'),
         State('no-simulations-slider', 'value')]
    )
    def update_simulation_graph(n_clicks, make_select_val, year_select_val, no_sim_val):
        """
        Parameters
        n_clicks: int
            number of button clicks
        make_select_val: str
            car make
        year_select_val: int
            model year
        no_sim_val:
            number of simulations
        """

        if n_clicks == 0:
            raise PreventUpdate

        y_pred = tweedie_model.batch_predict(
            car_make=make_select_val,
            car_year=year_select_val,
            n_simulations=no_sim_val
        )

        # figure needs list of lists as input data
        hist_data = [y_pred]

        fig = ff.create_distplot(hist_data, bin_size=.05, group_labels=["Predicted values"],
                                 show_curve=True)

        # Add title
        fig.update_layout(
            title_text=f'Distribution of predicted expected values N={no_sim_val}',
            legend={"orientation": "h"}
        )
        # calculate expected value
        ev = np.round(y_pred.mean(), decimals=3)
        return ev, dcc.Graph(figure=fig)
