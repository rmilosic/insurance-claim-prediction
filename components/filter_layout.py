import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


def create_filter_layout(title: str, filter_component):
    """
    Creates a filter layout based on title and filter component


    """
    return html.Div(
        children=[
            dbc.Row(
                children=[
                    dbc.Col(
                        children=[
                            html.H4(
                                f"{title}"
                            )
                        ]
                    )
                ]
            ),

            dbc.Row(
                className="my-4",
                children=[
                    dbc.Col(
                        children=[
                            filter_component
                        ]
                    )
                ]
            )
        ]
    )