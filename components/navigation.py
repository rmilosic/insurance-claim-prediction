import dash_bootstrap_components as dbc


layout = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Trendi", href="/trendi")),
        dbc.NavItem(dbc.NavLink("Leto", href="/leto")),

    ],
    className="mb-4",
    brand="PORABA ZDRAVIL V SLOVENIJI",
    brand_href="/"
)