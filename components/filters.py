import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

from components import filter_layout


car_make_select_component = dcc.Dropdown(
    id='car-make-select',
    value="AJ"
)
car_make_select = filter_layout.create_filter_layout("Select car make", car_make_select_component)


car_model_year_select_component = dcc.Dropdown(
    id="car-model-select",
    value=2019
)
car_model_year_select = filter_layout.create_filter_layout("Car model year", car_model_year_select_component)

simulations_no_slider_component = dcc.Slider(
    className="mt-2",
    id="car-model-select",
    min=1000,
    max=50000,
    value=5000,
    tooltip={
        "always_visible": True
    },
    marks={
        1000: "1000",
        50000: "50.000"
    },
)

simulations_no_slider = filter_layout.create_filter_layout("No. of simulations", simulations_no_slider_component)
