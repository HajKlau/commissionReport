import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import dash_bootstrap_components as dbc
from dash import (
    Dash,
    html,
    dcc,
    Input,
    Output,
    callback,
    dash_table
)

connection = create_engine('postgresql+psycopg2://postgres:postgres@127.0.0.1/sales_network')

agencies_query_file = open('queries/agenciesMonthlyCommission.sql','r')
agencies_query = agencies_query_file.read()

agencies_df = pd.read_sql_query(agencies_query, con=connection)  

directors_query_file = open('queries/dirSrCommission.sql','r')
directors_query = directors_query_file.read()

directors_df = pd.read_sql_query(directors_query, con=connection)  

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1(
        "Commission Report",
        style={
            'textAlign':'center'
            }
        ),
    
    html.H3(
        "Share in commissions ",
        style={
            'textAlign':'center', 
            'margin-top':'50px'
            }
        ),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                figure=px.pie(
                    agencies_df, 
                    names='agencyname',
                    values='sum',
                    title="Agencies share in total commission (per year)"
                    )
                )], 
                width=6
            ),
    
        dbc.Col([
            dcc.Graph(
                figure=px.pie(
                    directors_df, 
                    names='directorlastname',
                    values='total_director_commission',
                    title="Directors share in total commission (per year)"
                    )
                )],
                width=6,
        ),
    ]),

    html.H3(
        "Agencies",
        style={
            'textAlign':'center', 
            'margin-top':'50px',
            'margin-bottom':'30px'
            }
        ),

    html.H5(
        "Select agency",
        style={'textAlign':'left'}
        ),

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                agencies_df.agencyname.unique(), 
                agencies_df.agencyname[0], 
                id='dropdown-selection-sr'
                )
        ], width=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='commission-graph-sr',
                )
        ], width=8),
        
        dbc.Col([
            dash_table.DataTable(
                id='commission-table-sr'
                )
        ], width=4)
    ]),

    html.H3(
        "Directors",
        style={
            'textAlign':'center', 
            'margin-top':'50px',
            'margin-bottom':'30px'
            }
        ),

    html.H5(
        "Select director",
        style={'textAlign':'left'}
        ),

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                directors_df.directorlastname.unique(), 
                directors_df.directorlastname[0], 
                id='dropdown-selection-dir'
                )
        ], width=6)
    ]),
                
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='commission-graph-dir'
                )
        ], width=8),
        
        dbc.Col([
            dash_table.DataTable(
                id='commission-table-dir'
                )
        ], width=4)
    ]),
])

@callback(
    Output(
        component_id='commission-graph-sr', 
        component_property='figure'
        ),
    
    Output(
        component_id='commission-table-sr',
        component_property='data'
    ),
    
    Input(
        component_id='dropdown-selection-sr', 
        component_property='value'
        )
)

def update_graph_sr(chosen_agency):
    
    formatted_table = []
    
    fig = px.bar(
        agencies_df, 
        x=agencies_df.loc[agencies_df['agencyname'] == chosen_agency, 'month'], 
        y=agencies_df.loc[agencies_df['agencyname'] == chosen_agency, 'sum'],
        title=f"Agency commissions per month for {chosen_agency}"
        ).update_layout(
            xaxis_title="Month", 
            yaxis_title="Commission",
        )
    
    table_dict = agencies_df.loc[agencies_df['agencyname'] == chosen_agency].to_dict('records')

    for item in table_dict:
        formatted_table.append(
            {
                'Month': int(item['month']), 
                'Commission': float(item['sum'])
            }
        )

    return fig, formatted_table


@callback(
    Output(
        component_id='commission-graph-dir', 
        component_property='figure'
        ),
    
    Output(
        component_id='commission-table-dir',
        component_property='data'
    ),
    
    Input(
        component_id='dropdown-selection-dir', 
        component_property='value'
        )
)

def update_graph_dir(chosen_director):
    
    formatted_table = []
    
    fig = px.bar(
        directors_df, 
        x=directors_df.loc[directors_df['directorlastname'] == chosen_director, 'month'], 
        y=directors_df.loc[directors_df['directorlastname'] == chosen_director, 'total_director_commission'],
        title=f"Agency commissions per month for {chosen_director}"
        ).update_layout(
            xaxis_title="Month", 
            yaxis_title="Commission"
        )
    
    table_dict = directors_df.loc[directors_df['directorlastname'] == chosen_director].to_dict('records')
    
    for item in table_dict:
        formatted_table.append(
            {
                'Month': int(item['month']), 
                'Commission': float(item['total_director_commission'])
            }
        )

    return fig, formatted_table

if __name__ == '__main__':
    app.run(debug=False)
