import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app1, app2

server=app.server

app.layout=html.Div([
    dcc.Location(id='url', refresh=False),
    html.H1('MULTIPAGE DASH APP'),
    html.Li(children=html.A(href="/",children="Home")),
    html.Li(children=html.A(href="/apps/app1",children="Application 1")),
    html.Li(children=html.A(href="/apps/app2",children="Application 2")),
    html.Div(id='page-content'),
    ])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout()
    elif pathname == '/apps/app2':
        return app2.layout()
    else:
        return ''

if __name__ == '__main__':
    app.run_server(debug=True)