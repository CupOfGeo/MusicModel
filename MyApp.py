import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

import pandas as pd

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
df = pd.read_csv('data.csv')
net_df = pd.read_csv('net_preds.csv')

df_pred = pd.read_csv('predicted_genera.csv')
df_pred.drop(['genera','Unnamed: 0'], inplace=True, axis=1)
net_df.drop(['genera','Unnamed: 0'], inplace=True, axis=1)

df_lab = pd.read_csv("labeled_genera.csv")
df = df_pred.copy()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='beer'


app.layout = html.Div([
    html.H4(children='Music'),

    dcc.Input(id="art_text", type="text", value="", placeholder='Artist'),
    dcc.Input(id="song_text", type="text", value="", placeholder='Song'),

    #dash_table.DataTable(
    #id='data-table',
    #columns=[{"name": i, "id": i} for i in df.columns],
    #data=[]),
    dcc.Graph(id='graph-with-slider'),
    dcc.Graph(id='net-graph'),

    dcc.Dropdown(
        id='y-slider',
        options=[{'label': i, 'value': i} for i in df.columns],
        value='popularity'
    ),
    dcc.Dropdown(
        id='x-slider',
        options=[{'label': i, 'value': i} for i in df.columns],
        value='year')
    # ),
    # dcc.Dropdown(
    #     id='c-slider',
    #     options=[{'label': i, 'value': i} for i in df.columns],
    #     value='energy'
    # )

])


@app.callback(
    Output('graph-with-slider', 'figure'),
    Output('net-graph', 'figure'),
    Input('y-slider', 'value'),
    Input('x-slider', 'value'),
    #Input('c-slider', 'value'),
    Input('art_text', 'value'),
    Input('song_text', 'value'))
def update_figure(selected_y, selected_x,art,song_name):
    #filtered_df = df[df.year == selected_year]
    filtered_df = df.copy()[0:0]
    f_net = net_df.copy()[0:0]
    if art != '':
        art = art.split(',')
        filtered_df = df[df.artists.str.contains(art[0])]
        f_net = net_df[net_df.artists.str.contains(art[0])]
        for i in range(0,len(art)):
            filtered_df = filtered_df.append(df[df.artists.str.lower().str.contains(art[i].lower())])
            f_net = f_net.append(net_df[net_df.artists.str.lower().str.contains(art[i].lower())])

        if song_name != "":
            filtered_df = filtered_df[filtered_df.name.str.lower().str.contains(song_name.lower())]
            f_net = f_net[f_net.name.str.lower().str.contains(song_name.lower())]

    elif song_name != "" and art == None:
        if song_name != "":
            filtered_df = df[df.name.str.lower().str.contains(song_name.lower())]
            f_net = net_df[net_df.name.str.lower().str.contains(song_name.lower())]
    elif art == None or art == '' and song_name =='':
        #art = 'Bob Dylan'
        filtered_df = df#[df.artists.str.contains(art)]
        f_net = net_df#[df.artists.str.contains(art)]



    color_dict = {
    'hip-hop':'purple',
    'jazz':'blue',
    'rock':'red',
    'classical':'yellow',
    'metal':'black',
    'reggae':'green'
    }

    print(filtered_df.columns)
    size = f_net[["jazz", "classical", "rock", "hip-hop", "reggae", "metal"]].max(axis=1) 
    size_norm = []

    for element in size:
        if element > 0.5:
            size_norm.append((element - 0.5) * 2)
        else:
            size_norm.append(0.1)
            
    fig = px.scatter(
        filtered_df, y=selected_y, x=selected_x, color='pred',
        color_discrete_map=color_dict, hover_data=["name","artists"],opacity=0.7
    )

    fig_net = px.scatter(f_net, y=selected_y, x=selected_x, hover_data=[
            "name","artists", "jazz", "classical", "rock", "hip-hop", "reggae", "metal"
        ],opacity=1, color=f_net[["jazz", "classical", "rock", "hip-hop", "reggae", "metal"]].idxmax(axis=1),
        size=size_norm)
    fig.update_layout(transition_duration=500)
    fig_net.update_layout(transition_duration=500)

    #return filtered_df.to_dict('records'),fig
    #print(filtered_df.columns)
    return fig, fig_net


if __name__ == '__main__':
    app.run_server(debug=True)#,host='192.168.86.57',port=8052)
    #192.168.86.57
