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
img_logo = "assets/Logo -  (5).png"
encoded_image = base64.b64encode(open(img_logo, 'rb').read())
navbar = dbc.Navbar(
    children=[
        html.A(
            dbc.Row(
                [
                    dbc.Col(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),height="75px")),
                    dbc.Col(html.P("Carlos Eduardo, Gerônimo, Lucas Natanael, Raíssa e Sérgio", style={'font-size':'10px','font-weight': 'bold'}),align='center',md=12)
                ],
            ),
        )
    ],
    color='#F7F7F7',
    sticky="top",
    #className='container'
)
##### DROPDOWNS PARA QUANTIDADES #####
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
            options=[{'label':'Brasil','value':'brasil'},{'label':'Acre','value':'acre'},{'label':'Alagoas','value':'alagoas'},
            {'label':'Amapá','value':'amapa'},{'label':'Amazonas','value':'amazonas'},
            {'label':'Bahia','value':'bahia'},{'label':'Ceará','value':'ceara'},
            {'label':'Distrito Federal','value':'df'},{'label':'Espírito Santo','value':'espirito_santo'},
            {'label':'Goiás','value':'goias'},{'label':'Maranhão','value':'maranhao'},
            {'label':'Mato Grosso','value':'mato_grosso'},{'label':'Mato Grosso do Sul','value':'mato_grosso_do_sul'},
            {'label':'Minas Gerais','value':'minas_gerais'},{'label':'Pará','value':'para'},
            {'label':'Paraíba','value':'paraiba'},{'label':'Paraná','value':'parana'},
            {'label':'Pernambuco','value':'pernambuco'},{'label':'Piauí','value':'piaui'},
            {'label':'Rio de Janeiro','value':'rio_de_janeiro'},{'label':'Rio Grande do Norte','value':'rio_grande_do_norte'},
            {'label':'Rio Grande do Sul','value':'rio_grande_do_sul'},{'label':'Rondônia','value':'rondõnia'},
            {'label':'Roraima','value':'roraima'},{'label':'Santa Catarina','value':'santa_catarina'},
            {'label':'São Paulo','value':'são_paulo'},{'label':'Sergipe','value':'sergipe'},
            {'label':'Tocantins','value':'tocantins'}
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
            options=[{'label':'Brasil','value':'brasil'},{'label':'Acre','value':'acre'},{'label':'Alagoas','value':'alagoas'},
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
            {'label':'Tocantins','value':'tocantins'}
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
            {'label':'Roubo seguido de morte (latrocínio)','value':'roubo_seguido_de_morte_(latrocinio)'},
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
            {'label':'Tocantins','value':'tocantins'}
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
#dropdown com o mês de início no campo de média mensal de ocorrências
dropdown8_mes_incio_ocorrencias = dbc.FormGroup(
    [
        html.P('Mês inicio', style = {
            'textAlign': 'left',
        }),
        dcc.Dropdown(
            id="mes_inicio_ocorrencias_mensais",
            options=[{'label':'Janeiro','value':1},
            {'label':'Fevereiro','value':2},
            {'label':'Março','value':3},
            {'label':'Abril','value':4},
            {'label':'Maio','value':5},
            {'label':'Junho','value':6},
            {'label':'Julho','value':7},
            {'label':'Agosto','value':8},
            {'label':'Setembro','value':9},
            {'label':'Outubro','value':10},
            {'label':'Novembro','value':11},
            {'label':'Dezembro','value':12}
            ],
        )
    ], style = {'width' : '100%', 
               'fontSize' : '15px', 
               'color' : '#007CBA', 
               'font-weight': 'bold',
            }
)
#dropdown com o mês de fim no campo de média mensal de ocorrências
dropdown9_mes_fim_ocorrencias = dbc.FormGroup(
    [
        html.P('Mês final', style = {
            'textAlign': 'left',
        }),
        dcc.Dropdown(
            id="mes_fim_ocorrencias_mensais",
            options=[{'label':'Janeiro','value':1},
            {'label':'Fevereiro','value':2},
            {'label':'Março','value':3},
            {'label':'Abril','value':4},
            {'label':'Maio','value':5},
            {'label':'Junho','value':6},
            {'label':'Julho','value':7},
            {'label':'Agosto','value':8},
            {'label':'Setembro','value':9},
            {'label':'Outubro','value':10},
            {'label':'Novembro','value':11},
            {'label':'Dezembro','value':12}
            ],
        )
    ], style = {'width' : '100%', 
               'fontSize' : '15px', 
               'color' : '#007CBA', 
               'font-weight': 'bold',
            }
)
#dropdown com UFs no campo de média mensal de vitimas
dropdown10_vitimas_mensais = dbc.FormGroup(
    [
        html.P('UF', style = {
            'textAlign': 'left',
        }),
        dcc.Dropdown(
            id="uf_media_vitimas",
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
            {'label':'Tocantins','value':'tocantins'}
            ],
        )
    ], style = {'width' : '100%', 
               'fontSize' : '15px', 
               'color' : '#007CBA', 
               'font-weight': 'bold',
            }
)
#dropdown com o tipo de crime no campo de média mensal de vítimas
dropdown11_vitimas = dbc.FormGroup(
    [
        html.P('Tipo de crime', style = {
            'textAlign': 'left',
        }),
        dcc.Dropdown(
            id="media_crime_vitimas",
            options=[{'label':'Homicídio doloso','value':'homicidio_doloso'},
            {'label':'Lesão corporal seguida de morte','value':'lesao_corporal_seguida_de_morte'},
            {'label':'Roubo seguido de morte (latrocínio)','value':'roubo_seguido_de_morte_(latrocinio)'},
            ],
        )
    ], style = {'width' : '100%', 
               'fontSize' : '15px', 
               'color' : '#007CBA', 
               'font-weight': 'bold',
            }
)
#dropdown com o mês de início no campo de média mensal de vítimas
dropdown12_mes_incio_vitimas = dbc.FormGroup(
    [
        html.P('Mês inicial', style = {
            'textAlign': 'left',
        }),
        dcc.Dropdown(id="mes_inicio_vitimas_mensais",
            options=[{'label':'Janeiro','value':1},
            {'label':'Fevereiro','value':2},
            {'label':'Março','value':3},
            {'label':'Abril','value':4},
            {'label':'Maio','value':5},
            {'label':'Junho','value':6},
            {'label':'Julho','value':7},
            {'label':'Agosto','value':8},
            {'label':'Setembro','value':9},
            {'label':'Outubro','value':10},
            {'label':'Novembro','value':11},
            {'label':'Dezembro','value':12}
            ],
        )
    ], style = {'width' : '100%', 
               'fontSize' : '15px', 
               'color' : '#007CBA', 
               'font-weight': 'bold',
            }
)
#dropdown com o mês de fim no campo de média mensal de vítimas
dropdown13_mes_fim_vitimas = dbc.FormGroup(
    [
        html.P('Mês final', style = {
            'textAlign': 'left',
        }),
        dcc.Dropdown(
            id="mes_fim_vitimas_mensais",
            options=[{'label':'Janeiro','value':1},
            {'label':'Fevereiro','value':2},
            {'label':'Março','value':3},
            {'label':'Abril','value':4},
            {'label':'Maio','value':5},
            {'label':'Junho','value':6},
            {'label':'Julho','value':7},
            {'label':'Agosto','value':8},
            {'label':'Setembro','value':9},
            {'label':'Outubro','value':10},
            {'label':'Novembro','value':11},
            {'label':'Dezembro','value':12}
            ],
        )
    ], style = {'width' : '100%', 
               'fontSize' : '15px', 
               'color' : '#007CBA', 
               'font-weight': 'bold',
            }
)
##### DROPDOWNS PARA RANKINGS ##### []
#dropdown para o ranking de estados a partir de determinado crime
dropdown14_estadual_crime = dbc.FormGroup(
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
            #{'label':'Homicídio doloso','value':'homicidio_doloso'},
            #{'label':'Lesão corporal seguida de morte','value':'lesao_corporal_seguida_de_morte'},
            #{'label':'Roubo seguido de morte (latrocínio)','value':'roubo_seguido_de_morte_(latrocinio)'},
            #{'label':'Todos','value':'todos'}
            ],
        )
    ], style = {'width' : '100%', 
               'fontSize' : '15px', 
               'color' : '#007CBA', 
               'font-weight': 'bold',
            }
)
#dropdown para o ranking de crimes a partir de determinado estado
dropdown15_criminal_estado = dbc.FormGroup(
    [
        html.P('UF', style = {
            'textAlign': 'left',
        }),
        dcc.Dropdown(
            id="ranking_criminal_estado",
            options=[{'label':'Brasil','value':'brasil'},{'label':'Acre','value':'acre'},{'label':'Alagoas','value':'alagoas'},
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
            {'label':'Tocantins','value':'tocantins'}
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
        #quantidades
        dbc.Row(
            [
                #quantidade de vítimas e ocorrências por ano
                dbc.Col(
                    [
                        html.Br(),
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
                dbc.Col(
                    [
                        html.H4(children = 'Média mensal de vítimas por estado', style = {'textAlign': 'center','color' : '#007CBA'}),
                        dbc.Row(
                            [
                                #dropdown UF
                                dbc.Col([dropdown10_vitimas_mensais],md=6),
                                #dropdown tipo de crime
                                dbc.Col([dropdown11_vitimas],md=6)
                            ]
                        ),
                        dbc.Row(
                            [
                                #slider "entre anos"
                                dbc.Col(
                                    [
                                        html.Br(),
                                        dcc.RangeSlider(
                                        id='entre_anos1', 
                                        min=2015, 
                                        max=2020, 
                                        step=1,
                                        marks={
                                            2015: '2015',
                                            2016: '2016',
                                            2017: '2017',
                                            2018: '2018',
                                            2019: '2019',
                                            2020: '2020',
                                        },
                                        value=[2015, 2016]
                                        )
                                    ]
                                )
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Br(),
                                        dbc.Row(
                                            [
                                                #dropdown mês inicial
                                                dbc.Col([dropdown12_mes_incio_vitimas], md=6),
                                                #dorpdown mês final
                                                dbc.Col([dropdown13_mes_fim_vitimas],md=6)
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(id='output_media_vitimas', children=["Selecione uma UF, o tipo de crime e o período de tempo"]
                                        ,style={'background-color':'#39B5E6',
                                                'fontSize' : '16px', 
                                                'color' : '#FFFFFF', 
                                                'textAlign': 'center',
                                                'font-weight': 'bold',
                                            }            
                                        ),
                                    ]
                                )
                            ]
                        )
                    ],md=6,
                ),
                dbc.Col(
                    [
                        html.H4(children = 'Média mensal de ocorrências por estado', style = {'textAlign': 'center','color' : '#007CBA'}),
                        dbc.Row(
                            [
                                #dropdown UF
                                dbc.Col([dropdown6_ocorrencias_mensais],md=6),
                                #dropdown tipo de crime
                                dbc.Col([dropdown7_ocorrencias],md=6)
                            ]
                        ),
                        dbc.Row(
                            [
                                #slider "entre anos"
                                dbc.Col(
                                    [
                                        html.Br(),
                                        dcc.RangeSlider(
                                            id='entre_anos2',
                                            min=2015,
                                            max=2020,
                                            step=1,
                                            marks={
                                                2015: '2015',
                                                2016: '2016',
                                                2017: '2017',
                                                2018: '2018',
                                                2019: '2019',
                                                2020: '2020',
                                            },
                                            value=[2015, 2016]
                                        )
                                    ]
                                )
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Br(),
                                        dbc.Row(
                                            [
                                                #dorpdown mês inicial
                                                dbc.Col([dropdown8_mes_incio_ocorrencias], md=6),
                                                #dropdown Mês final
                                                dbc.Col([dropdown9_mes_fim_ocorrencias], md=6)
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(id='output_media_ocorrencias', children=["Selecione uma UF, o tipo de crime e o período de tempo"]
                                        ,style={'background-color':'#39B5E6',
                                                'fontSize' : '16px', 
                                                'color' : '#FFFFFF', 
                                                'textAlign': 'center',
                                                'font-weight': 'bold',
                                            }            
                                        ),
                                    ]
                                )
                            ]
                        )
                    ], md=6,
                )
            ],
            align="center",
        ),
        #rankings
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.Br(),
                        html.H4(children = 'Ranking estadual por crime', style = {'textAlign': 'center','color' : '#007CBA'}),
                        dbc.Row(
                            [
                                dbc.Col([dropdown14_estadual_crime], md = 6),
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
                        html.Br(),
                        html.Br(),
                        html.H4(children = 'Ranking criminal por estado', style = {'textAlign': 'center','color' : '#007CBA'}),
                        dbc.Row(
                            [
                                dbc.Col([dropdown15_criminal_estado], md = 6),
                                dbc.Col(
                                    [
                                        html.P('Número de crimes', style = {
                                            'textAlign': 'left','color' : '#007CBA','font-weight': 'bold'
                                        }),
                                        dcc.Slider(id='num_crimes', min=1, max=6, step=1, tooltip={'always_visible':False, 'placement':'bottom'})
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
        data_crime_ano = requests.get("https://crimepontodata.tk/quantidade/crimes/"+str(value))
        data_crime_ano = data_crime_ano.json()
        figure = {
            'data':[
                {'x': [data_crime_ano['Ano']], 'y': [data_crime_ano['Ocorrências']], 'type': 'bar', 'name': 'Ocorrências'},
                {'x': [data_crime_ano['Ano']], 'y': [data_crime_ano['Vítimas']], 'type': 'bar', 'name': 'Vítimas'}
            ],
        }
        return figure

#callback para o número total de ocorrências
@app.callback(
    Output('output_ocorrencias','children'),
    [Input('uf_ocorrencias','value'),Input('nome_crime_ocorrencias','value')]
)

def update_ocorrencias(value_uf, value_nome_crime):
    data_ocorrencias = requests.get("https://crimepontodata.tk/quantidade/ocorrencias/"+str(value_nome_crime)+"/"+str(value_uf))
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
    print(value_uf)
    if (value_uf and value_nome_crime) is None:
        raise PreventUpdate
    else:
        data_vitimas = requests.get("https://crimepontodata.tk/quantidade/vitimas/"+str(value_nome_crime)+"/"+str(value_uf))
        data_vitimas = data_vitimas.json()
        label = str(data_vitimas['quantidade'])+" vítimas no estado."
        return label

#callback média de vítimas mensais
@app.callback(
    Output('output_media_vitimas','children'),
    [Input('media_crime_vitimas','value'),Input('uf_media_vitimas','value'),
    Input('entre_anos1','value'),Input('mes_inicio_vitimas_mensais','value'),
    Input('mes_fim_vitimas_mensais','value')]
)

def update_vitimas_mensais(value_nome_crime,value_uf,value_anos,value_mes_ini,value_mes_fim):
    if (value_uf and value_nome_crime and value_anos and value_mes_ini and value_mes_fim) is None:
        raise PreventUpdate
    else:
        if (value_anos[0] == value_anos[1] and value_mes_ini > value_mes_fim):
            label = "Insira um período de tempo válido!"
            return label
        else:
            data_media_vitimas = requests.get(
                "https://crimepontodata.tk/media/vitimas/"+str(value_nome_crime)+"/"+str(value_uf)+
                "/"+str(value_mes_ini)+"-"+str(value_anos[0])+"/"+str(value_mes_fim)+"-"+str(value_anos[1]))
            data_media_vitimas = data_media_vitimas.json()
            label = str(round(data_media_vitimas['vitimas'],2))+" é a média de vítimas no estado."
            return label

#callback média de ocorrencias mensais
@app.callback(
    Output('output_media_ocorrencias','children'),
    [Input('nome_crime_ocorrencias_mensais','value'),Input('uf_ocorrencias_mensais','value'),
    Input('entre_anos2','value'),Input('mes_inicio_ocorrencias_mensais','value'),
    Input('mes_fim_ocorrencias_mensais','value')]
)

def update_ocorrencias_mensais(value_nome_crime,value_uf,value_anos,value_mes_ini,value_mes_fim):
    if (value_uf and value_nome_crime and value_anos and value_mes_ini and value_mes_fim) is None:
        raise PreventUpdate
    else:
        if (value_anos[0] == value_anos[1] and value_mes_ini > value_mes_fim):
            label = "Insira um período de tempo válido!"
            return label
        else:
            data_media_ocorrencias = requests.get(
                "https://crimepontodata.tk/media/ocorrencias/"+str(value_nome_crime)+"/"+str(value_uf)+
                "/"+str(value_mes_ini)+"-"+str(value_anos[0])+"/"+str(value_mes_fim)+"-"+str(value_anos[1]))
            data_media_ocorrencias = data_media_ocorrencias.json()
            #print(data_media_ocorrencias)
            label = str(round(data_media_ocorrencias['ocorrencias'],2))+" é a média de ocorrências no estado."
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
        data_estadual_crime = requests.get("https://crimepontodata.tk/ranking/"+str(value_num)+"/estadual/"+str(value_nome_crime))
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
        data_criminal_estado = requests.get("https://crimepontodata.tk/ranking/"+str(value_num)+"/criminal/"+str(value_uf))
        data_criminal_estado = data_criminal_estado.json()
        crimes = []
        quantidade = []
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
    app.run_server( host='0.0.0.0', port=8050, debug = False)
