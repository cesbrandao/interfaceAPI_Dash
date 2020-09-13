import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import base64
import plotly.express as px
import requests
import json
import dash_table
from dash.exceptions import PreventUpdate

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
                    dbc.Col(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),height="30px")),
                ],
            ),
        )
    ],
    color='#F7F7F7',
    sticky="top",
    #className='container'
)
##### DROPDOWNS PARA QUANTIDADES ##### [OK]
#dropdown com os anos no campo de quantidade de crimes por ano
dropdown1_crimes_ano = dbc.FormGroup(
    [
        html.P('Ano', style = {
            'textAlign': 'left', 
        }),
        dcc.Dropdown(
            id="crimes_ano",
            options=[{'label':2015,'value':2015},{'label':2016,'value':2016},{'label':2017,'value':2017},
            {'label':2018,'value':2018},{'label':2019,'value':2019},{'label':2020,'value':2020},
            #{'label':"Todos",'value':'todos'}
            ],
            #value = 2020
        )                                    
    ], style = {'width' : '100%', 
               'fontSize' : '15px', 
               'color' : '#007CBA', 
               'font-weight': 'bold',
            }
)
#dropdown com UFs no campo de quantidade total de ocorrÊncias
dropdown2_ocorrencias = dbc.FormGroup(
    [
        html.P('UF', style = {
            'textAlign': 'left',
        }),
        dcc.Dropdown(
            id="uf_ocorrencias",
            options=[{'label':'Acre','value':'acre'},{'label':'Alagoas','value':'alagoas'},
            {'label':'Amapá','value':'amapa'},{'label':'Amazonas','value':'amazonas'},
            {'label':'Bahia','value':'bahia'},{'label':'Ceará','value':'ceara'},
            {'label':'Distrito Federal','value':'df'},{'label':'Espírito Santo','value':'espirito_santo'},
            {'label':'Goiás','value':'goias'},{'label':'Maranhão','value':'maranhao'},
            {'label':'Mato Grosso','value':'mato_grosso'},{'label':'Mato Grosso do Sul','value':'mato_grosso_do_sul'},
            {'label':'Minas Gerais','value':'minas_gerais'},{'label':'Pará','value':'para'},
            {'label':'Paraíba','value':'paraiba'},{'label':'Paraná','value':'parana'},
            {'label':'Pernambuco','value':'pernambuco'},{'label':'Piauí','value':'piaui'},
            {'label':'Rio de Janeiro','value':'rio_de_janeiro'},{'label':'Rio Grande do Norte','value':'rio_grande_do_norte'},
            {'label':'Rio Grande do Sul','value':'rio_grande_do_sul'},{'label':'Rondônia','value':'rondonia'},
            {'label':'Roraima','value':'roraima'},{'label':'Santa Catarina','value':'santa_catarina'},
            {'label':'São Paulo','value':'são_paulo'},{'label':'Sergipe','value':'sergipe'},
            {'label':'Tocantins','value':'tocatins'}
            ],
        )
    ], style = {'width' : '100%', 
               'fontSize' : '15px', 
               'color' : '#007CBA', 
               'font-weight': 'bold',
            }
)
#dropdown com o tipo de crime no campo de quantidade total de ocorrÊncias
dropdown3_ocorrencias = dbc.FormGroup(
    [
        html.P('Tipo de crime', style = {
            'textAlign': 'left',
        }),
        dcc.Dropdown(
            id="nome_crime_ocorrencias",
            options=[{'label':'Furto de veículo','value':'furto_de_veiculo'},
            {'label':'Roubo de veículo','value':'roubo_de_veiculo'},
            {'label':'Roubo a instituição financeira','value':'roubo_a_instituiçao_financeira'},
            {'label':'Roubo de carga','value':'roubo_de_carga'},
            {'label':'Estupro','value':'estupro'},
            {'label':'Tentativa de homicídio','value':'tentativa_de_homicidio'}
            ],
        )
    ], style = {'width' : '100%', 
               'fontSize' : '15px', 
               'color' : '#007CBA', 
               'font-weight': 'bold',
            }
)
#dropdown com UFs no campo de quantidade total de vítimas
dropdown4_vitimas = dbc.FormGroup(
    [
        html.P('UF', style = {
            'textAlign': 'left',
        }),
        dcc.Dropdown(
            id="uf_vitimas",
            options=[{'label':'Acre','value':'acre'},{'label':'Alagoas','value':'alagoas'},
            {'label':'Amapá','value':'amapa'},{'label':'Amazonas','value':'amazonas'},
            {'label':'Bahia','value':'bahia'},{'label':'Ceará','value':'ceara'},
            {'label':'Distrito Federal','value':'df'},{'label':'Espírito Santo','value':'espirito_santo'},
            {'label':'Goiás','value':'goias'},{'label':'Maranhão','value':'maranhao'},
            {'label':'Mato Grosso','value':'mato_grosso'},{'label':'Mato Grosso do Sul','value':'mato_grosso_do_sul'},
            {'label':'Minas Gerais','value':'minas_gerais'},{'label':'Pará','value':'para'},
            {'label':'Paraíba','value':'paraiba'},{'label':'Paraná','value':'parana'},
            {'label':'Pernambuco','value':'pernambuco'},{'label':'Piauí','value':'piaui'},
            {'label':'Rio de Janeiro','value':'rio_de_janeiro'},{'label':'Rio Grande do Norte','value':'rio_grande_do_norte'},
            {'label':'Rio Grande do Sul','value':'rio_grande_do_sul'},{'label':'Rondônia','value':'rondonia'},
            {'label':'Roraima','value':'roraima'},{'label':'Santa Catarina','value':'santa_catarina'},
            {'label':'São Paulo','value':'são_paulo'},{'label':'Sergipe','value':'sergipe'},
            {'label':'Tocantins','value':'tocatins'}
            ],
        )
    ], style = {'width' : '100%', 
               'fontSize' : '15px', 
               'color' : '#007CBA', 
               'font-weight': 'bold',
            }
)
#dropdown com o tipo de crime no campo de quantidade total de vítimas
dropdown5_vitimas = dbc.FormGroup(
    [
        html.P('Tipo de crime', style = {
            'textAlign': 'left',
        }),
        dcc.Dropdown(
            id="nome_crime_vitimas",
            options=[{'label':'Homicídio doloso','value':'homicidio_doloso'},
            {'label':'Lesão corporal seguida de morte','value':'lesao_corporal_seguida_de_morte'},
            {'label':'Roubo seguido de morte (latrocínio)','value':'latrocinio'},
            ],
        )
    ], style = {'width' : '100%', 
               'fontSize' : '15px', 
               'color' : '#007CBA', 
               'font-weight': 'bold',
            }
)
##### DROPDOWNS PARA MÉDIAS #####
#dropdown com UFs no campo de média mensal de ocorrências
dropdown6_ocorrencias_mensais = dbc.FormGroup(
    [
        html.P('UF', style = {
            'textAlign': 'left',
        }),
        dcc.Dropdown(
            id="uf_ocorrencias_mensais",
            options=[{'label':'Acre','value':'acre'},{'label':'Alagoas','value':'alagoas'},
            {'label':'Amapá','value':'amapa'},{'label':'Amazonas','value':'amazonas'},
            {'label':'Bahia','value':'bahia'},{'label':'Ceará','value':'ceara'},
            {'label':'Distrito Federal','value':'df'},{'label':'Espírito Santo','value':'espirito_santo'},
            {'label':'Goiás','value':'goias'},{'label':'Maranhão','value':'maranhao'},
            {'label':'Mato Grosso','value':'mato_grosso'},{'label':'Mato Grosso do Sul','value':'mato_grosso_do_sul'},
            {'label':'Minas Gerais','value':'minas_gerais'},{'label':'Pará','value':'para'},
            {'label':'Paraíba','value':'paraiba'},{'label':'Paraná','value':'parana'},
            {'label':'Pernambuco','value':'pernambuco'},{'label':'Piauí','value':'piaui'},
            {'label':'Rio de Janeiro','value':'rio_de_janeiro'},{'label':'Rio Grande do Norte','value':'rio_grande_do_norte'},
            {'label':'Rio Grande do Sul','value':'rio_grande_do_sul'},{'label':'Rondônia','value':'rondonia'},
            {'label':'Roraima','value':'roraima'},{'label':'Santa Catarina','value':'santa_catarina'},
            {'label':'São Paulo','value':'são_paulo'},{'label':'Sergipe','value':'sergipe'},
            {'label':'Tocantins','value':'tocatins'}
            ],
        )
    ], style = {'width' : '100%', 
               'fontSize' : '15px', 
               'color' : '#007CBA', 
               'font-weight': 'bold',
            }
)
#dropdown com o tipo de crime no campo de média mensal de ocorrências
dropdown7_ocorrencias = dbc.FormGroup(
    [
        html.P('Tipo de crime', style = {
            'textAlign': 'left',
        }),
        dcc.Dropdown(
            id="nome_crime_ocorrencias_mensais",
            options=[{'label':'Furto de veículo','value':'furto_de_veiculo'},
            {'label':'Roubo de veículo','value':'roubo_de_veiculo'},
            {'label':'Roubo a instituição financeira','value':'roubo_a_instituiçao_financeira'},
            {'label':'Roubo de carga','value':'roubo_de_carga'},
            {'label':'Estupro','value':'estupro'},
            {'label':'Tentativa de homicídio','value':'tentativa_de_homicidio'}
            ],
        )
    ], style = {'width' : '100%', 
               'fontSize' : '15px', 
               'color' : '#007CBA', 
               'font-weight': 'bold',
            }
)
##### DROPDOWNS PARA RANKINGS ##### [OK]
#dropdown para o ranking de estados a partir de determinado crime
dropdown8_estadual_crime = dbc.FormGroup(
    [
        html.P('Tipo de crime', style = {
            'textAlign': 'left',
        }),
        dcc.Dropdown(
            id="ranking_estadual_crime",
            options=[{'label':'Furto de veículo','value':'furto_de_veiculo'},
            {'label':'Roubo de veículo','value':'roubo_de_veiculo'},
            {'label':'Roubo a instituição financeira','value':'roubo_a_instituiçao_financeira'},
            {'label':'Roubo de carga','value':'roubo_de_carga'},
            {'label':'Estupro','value':'estupro'},
            {'label':'Tentativa de homicídio','value':'tentativa_de_homicidio'},
            {'label':'Homicídio doloso','value':'homicidio_doloso'},
            {'label':'Lesão corporal seguida de morte','value':'lesao_corporal_seguida_de_morte'},
            {'label':'Roubo seguido de morte (latrocínio)','value':'latrocinio'}
            ],
        )
    ], style = {'width' : '100%', 
               'fontSize' : '15px', 
               'color' : '#007CBA', 
               'font-weight': 'bold',
            }
)
#dropdown para o ranking de crimes a partir de determinado estado
dropdown9_criminal_estado = dbc.FormGroup(
    [
        html.P('UF', style = {
            'textAlign': 'left',
        }),
        dcc.Dropdown(
            id="ranking_criminal_estado",
            options=[{'label':'Acre','value':'acre'},{'label':'Alagoas','value':'alagoas'},
            {'label':'Amapá','value':'amapa'},{'label':'Amazonas','value':'amazonas'},
            {'label':'Bahia','value':'bahia'},{'label':'Ceará','value':'ceara'},
            {'label':'Distrito Federal','value':'df'},{'label':'Espírito Santo','value':'espirito_santo'},
            {'label':'Goiás','value':'goias'},{'label':'Maranhão','value':'maranhao'},
            {'label':'Mato Grosso','value':'mato_grosso'},{'label':'Mato Grosso do Sul','value':'mato_grosso_do_sul'},
            {'label':'Minas Gerais','value':'minas_gerais'},{'label':'Pará','value':'para'},
            {'label':'Paraíba','value':'paraiba'},{'label':'Paraná','value':'parana'},
            {'label':'Pernambuco','value':'pernambuco'},{'label':'Piauí','value':'piaui'},
            {'label':'Rio de Janeiro','value':'rio_de_janeiro'},{'label':'Rio Grande do Norte','value':'rio_grande_do_norte'},
            {'label':'Rio Grande do Sul','value':'rio_grande_do_sul'},{'label':'Rondônia','value':'rondonia'},
            {'label':'Roraima','value':'roraima'},{'label':'Santa Catarina','value':'santa_catarina'},
            {'label':'São Paulo','value':'são_paulo'},{'label':'Sergipe','value':'sergipe'},
            {'label':'Tocantins','value':'tocatins'}
            ],
        )
    ], style = {'width' : '100%', 
               'fontSize' : '15px', 
               'color' : '#007CBA', 
               'font-weight': 'bold',
            }
)
body = html.Div(
    [
        #quantidades [OK]
        dbc.Row(
            [
                #quantidade de vítimas e ocorrências por ano
                dbc.Col(
                    [
                        html.H4(children = 'Número de ocorrências e vítimas por ano', style = {'textAlign': 'center','color' : '#007CBA'}),
                        dbc.Row([
                            dbc.Col([dropdown1_crimes_ano], md = 3)
                        ]),
                        dcc.Graph(id = 'crimes_ano_graph')
                    ], md = 6),
                dbc.Col(
                    [
                        #quantidade total de ocorrências por estado
                        html.H4(children = 'Número total de ocorrências por estado', style = {'textAlign': 'center','color' : '#007CBA'}),
                        dbc.Row([
                            dbc.Col([dropdown2_ocorrencias], md = 6),
                            dbc.Col([dropdown3_ocorrencias], md = 6)
                        ]
                        ),
                        html.Div(id='output_ocorrencias', children=['']
                            ,style={'background-color':'#39B5E6',
                                    'fontSize' : '16px', 
                                    'color' : '#FFFFFF', 
                                    'textAlign': 'center',
                                    'font-weight': 'bold',
                                    }            
                            ),
                        #quantidade total de vítimas por estado
                        html.Br(),
                        html.H4(children = 'Número total de vítimas por estado', style = {'textAlign': 'center','color' : '#007CBA'}),
                        dbc.Row([
                            dbc.Col([dropdown4_vitimas], md = 6),
                            dbc.Col([dropdown5_vitimas], md = 6)
                        ]
                        ),
                        html.Div(id='output_vitimas', children=["Selecione uma UF e o tipo de crime"]
                            ,style={'background-color':'#39B5E6',
                                    'fontSize' : '16px', 
                                    'color' : '#FFFFFF', 
                                    'textAlign': 'center',
                                    'font-weight': 'bold',
                                    }            
                            ),
                    ], md = 6),
            ],
            align="center",
        ),
        #médias
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
            ],
            align="center",
        ),
        #rankings [OK]
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4(children = 'Ranking estadual por crime', style = {'textAlign': 'center','color' : '#007CBA'}),
                        dbc.Row(
                            [
                                dbc.Col([dropdown8_estadual_crime], md = 6),
                                dbc.Col(
                                    [
                                        html.P('Número de estados', style = {
                                            'textAlign': 'left','color' : '#007CBA','font-weight': 'bold'
                                        }),
                                        dcc.Slider(id='num_estados', min=1, max=27, step=1, tooltip={'always_visible':False, 'placement':'bottom'})
                                    ]
                                )
                            ],
                        
                        ),
                    dcc.Graph(id ='ranking_estadual_crime_graph')
                    ],md = 6
                ),
                dbc.Col(
                    [
                        html.H4(children = 'Ranking criminal por estado', style = {'textAlign': 'center','color' : '#007CBA'}),
                        dbc.Row(
                            [
                                dbc.Col([dropdown9_criminal_estado], md = 6),
                                dbc.Col(
                                    [
                                        html.P('Número de crimes', style = {
                                            'textAlign': 'left','color' : '#007CBA','font-weight': 'bold'
                                        }),
                                        dcc.Slider(id='num_crimes', min=1, max=9, step=1, tooltip={'always_visible':False, 'placement':'bottom'})
                                    ]
                                )
                            ]
                        ),
                    dcc.Graph(id='ranking_criminal_estado_graph')
                    ],md=6
                ),
            ],
            align="center",
        )
    ],style = {'margin-left': '5%',
            'margin-right': '5%',
            'padding': '20px 20p'}
)

app._layout = html.Div([navbar, body])

#callback para a comparação entre o número de ocorrências e vítimas em um determinado ano
@app.callback(
    Output('crimes_ano_graph','figure'),
    [Input('crimes_ano','value')]
)

def update_crimes_ano_graph(value):
    if value is None:
        raise PreventUpdate
    else:
        data_crime_ano = requests.get("http://54.174.134.220:8080/quantidade/crimes/"+str(value))
        data_crime_ano = data_crime_ano.json()
        #print(data_crime_ano)
        figure = {
            'data':[
                {'x': [data_crime_ano['Ano']], 'y': [data_crime_ano['Ocorrências']], 'type': 'bar', 'name': 'Ocorrências'},
                {'x': [data_crime_ano['Ano']], 'y': [data_crime_ano['Vítimas']], 'type': 'bar', 'name': 'Vítimas'}
            ],
            #'layout': {'title': 'Crimes por ano'}
        }
        return figure

#callback para o número total de ocorrências
@app.callback(
    Output('output_ocorrencias','children'),
    [Input('uf_ocorrencias','value'),Input('nome_crime_ocorrencias','value')]
)

def update_ocorrencias(value_uf, value_nome_crime):
    data_ocorrencias = requests.get("http://54.174.134.220:8080/quantidade/ocorrencias/"+str(value_nome_crime)+"/"+str(value_uf))
    data_ocorrencias = data_ocorrencias.json()

    label = "Selecione uma UF e o tipo de crime"
    if (value_uf and value_nome_crime) is not None:
        label = str(data_ocorrencias['quantidade'])+" ocorrências no estado."
    return label

#callback para o número total de vítimas
@app.callback(
    Output('output_vitimas','children'),
    [Input('uf_vitimas','value'),Input('nome_crime_vitimas','value')]
)

def update_vitimas(value_uf, value_nome_crime):
    if (value_uf and value_nome_crime) is None:
        raise PreventUpdate
    else:
        data_vitimas = requests.get("http://54.174.134.220:8080/quantidade/vitimas/"+str(value_nome_crime)+"/"+str(value_uf))
        data_vitimas = data_vitimas.json()
        label = str(data_vitimas['quantidade'])+" vítimas no estado."
        return label

#callback para o ranking estadual por crime
@app.callback(
    Output('ranking_estadual_crime_graph','figure'),
    [Input('ranking_estadual_crime','value'),Input('num_estados','value')]
)

def update_ranking_estadual_crime(value_nome_crime,value_num):
    if (value_nome_crime and value_num) is None:
        raise PreventUpdate
    else:
        data_estadual_crime = requests.get("http://54.174.134.220:8080/ranking/"+str(value_num)+"/estadual/"+str(value_nome_crime))
        data_estadual_crime = data_estadual_crime.json()
        cidades = []
        quantidade = []
        for k,v in data_estadual_crime.items():
            cidades.append(k)
            quantidade.append(v)
        figure = {
            'data':[
                    {'x': [cidades[i]], 'y': [quantidade[i]], 'type': 'bar', 'name':str(cidades[i])} for i in range(len(cidades))

            ],
            'layout': {'showlegend': False}
        }
        return figure

#callback para o ranking criminal por estado
@app.callback(
    Output('ranking_criminal_estado_graph','figure'),
    [Input('ranking_criminal_estado','value'),Input('num_crimes','value')]
)

def update_ranking_criminal_estado(value_uf,value_num):
    if (value_uf and value_num) is None:
        raise PreventUpdate
    else:
        data_criminal_estado = requests.get("http://54.174.134.220:8080/ranking/"+str(value_num)+"/criminal/"+str(value_uf))
        data_criminal_estado = data_criminal_estado.json()
        crimes = []
        quantidade = []
        #print(data_criminal_estado)
        #print(type(data_criminal_estado))
        for element in data_criminal_estado:
                crimes.append(element['crime'])
                quantidade.append(element['ocorrencias'])
        figure = {
            'data':[
                    {'x': [crimes[i]], 'y': [quantidade[i]], 'type': 'bar', 'name':str(crimes[i])} for i in range(len(crimes))
            ],
            'layout': {'showlegend': False}
        }
        return figure
    
if __name__ == '__main__':
    app.run_server(debug = True)