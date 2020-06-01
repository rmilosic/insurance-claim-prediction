from datetime import datetime

import dash_core_components as dcc

from components import filter_layout
from app import features_data


unique_blind_makes = features_data[features_data["Blind_Make"].notnull()]["Blind_Make"].sort_values().unique()
car_make_select_component = dcc.Dropdown(
    id='make-select',
    options=[
        {'label': value, 'value': value} for value in unique_blind_makes
    ],
    value="AJ",
)
car_make_select = filter_layout.create_filter_layout("Select car make", car_make_select_component)


this_year = datetime.now().year
car_model_year_select_component = dcc.Dropdown(
    id="year-select",
    value=2019,
    options=[{'label': year, 'value': year} for year in range(1980, this_year)]
)
car_model_year_select = filter_layout.create_filter_layout("Car model year", car_model_year_select_component)

simulations_no_slider_component = dcc.Slider(
    className="mt-2",
    id="no-simulations-slider",
    min=1000,
    max=50000,
    value=5000,
    step=100,
    tooltip={
        "always_visible": True
    },
    marks={
        1000: "1000",
        50000: "50.000"
    },
)

simulations_no_slider = filter_layout.create_filter_layout("No. of simulations", simulations_no_slider_component)
