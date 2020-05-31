from dash.dependencies import Input, Output
import plotly.graph_objects as go
import dash_table


def register_callbacks(app):
    """
    Register app callbacks
    """
    pass
    # @app.callback(
    #     Output('trend-graph-absolute', 'figure'),
    #     [
    #         Input('aggregate-value-radio', 'value'),
    #         Input('atc-level-dropdown', 'value')
    #     ]
    # )
    # def update_main_graph(aggregate_value_name: str, atc_level: int):
    #
    #     df2 = df.loc[df[aggregate_value_name] > 0]
    #
    #     df_pivot = df2.pivot_table(
    #         index=["leto", atc_level],
    #         values=aggregate_value_name,
    #         aggfunc=sum
    #     ).unstack(1)
    #
    #     categoryarray = df_pivot.loc[df_pivot.index.max()].sort_values(ascending=False).index
    #
    #     fig = go.Figure()
    #
    #     for col in categoryarray:
    #
    #         fig.add_trace(
    #             go.Bar(
    #                 x=df_pivot.index.to_list(), y=df_pivot[col].to_list(), name=print_name(col[1])
    #             )
    #         )
    #
    #     fig.update_layout(
    #         title="Pregled porabe po ATC skupinah",
    #         barmode='stack',
    #         xaxis={'categoryorder': 'sum descending', "tickmode": "linear"},
    #         legend_orientation="v",
    #         legend={"font": {"size": 9}})
    #
    #     return fig
    #
    #     }