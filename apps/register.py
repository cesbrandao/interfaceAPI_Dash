import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import flask
import requests
import base64

#from dash import app
external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

#logo crime.data
img_logo = "assets/logo1.png"
encoded_image = base64.b64encode(open(img_logo, 'rb').read())
navbar = dbc.Navbar(
    children=[
        html.A(
            dbc.Row(
                [
                    dbc.Col(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),height="80px")),
                ],
            ),
        )
    ],
    color='#F7F7F7',
    sticky="top",
    #className='container'
)

#entrada email
email_input = dbc.FormGroup(
    [
        dbc.Label("Email", html_for="email"),
        dbc.Input(type="email", id="email", placeholder="Insira seu email"),
        html.Div(id='container-button-basic',
             children='Enter a value and press submit',style={'display':'none'}),
    ]
    )
#entrada senha
password_input = dbc.FormGroup(
    [
        dbc.Label("Senha", html_for="password"),
        dbc.Input(type="password", id="password", placeholder="Insira sua senha"),
        
    ]
    )
submit = dbc.Button("Cadastrar", id='submit_register', n_clicks=0, color="primary")
#html.Div(id = 'confirma', children = '')

body=html.Div(
    [
        html.Br(),
        dbc.Card([
            dbc.CardHeader("Cadastro de usuário"),
            dbc.CardBody(
                [
                    dbc.FormGroup([
                        email_input,
                        password_input,
                        submit
                    ])
            
                ]
            ),
            
        ],className="container w-50 mb-3 ", color="info", outline=True, body=True, style={"width": "100rem",})
    ]
)
app._layout = html.Div([navbar,body])

@app.callback(
    Output('container-button-basic', 'children'),
    [Input('submit_register', 'n_clicks')],
    [State('email', 'value'), State('password', 'value')])
def update_output(n_clicks, value1, value2):
    #requisição para a API e registro do novo usuário
    url = 'http://54.174.134.220:8080/cadastro'
    headers = {"Content-Type":"application/json"}
    if (value1 and value2) is not None:
        payload = '{"email": " ' + str(value1) + ' ","password": "' + str(value2) + '"}'
        print(type(payload))
        print(payload)
        response = requests.request('POST', url, data=payload, headers=headers)
        print(response.text)
    return 0

if __name__ == "__main__":
    app.run_server(debug = True)