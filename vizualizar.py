import pandas as pd
import plotly.graph_objects as go
import dash
import plotly.express as px
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

# Cargar el conjunto de datos original en un DataFrame
df = pd.read_csv('communities.data')
df2 = pd.read_csv('wine.data')
df3 = pd.read_csv('airqualityuci.csv')


# Seleccionar una muestra aleatoria de filas para crear el subset
subset = df.sample(n=1994)  # Ajusta el tamaño de la muestra según tus necesidades

#Crimen
# Crear las gráficas de las subpestañas
fig_age = go.Figure()
fig_age.add_trace(go.Scatter(x=subset['agePct12t21'], y=subset['ViolentCrimesPerPop'], mode='markers', name='Age_12To21'))
fig_age.add_trace(go.Scatter(x=subset['agePct12t29'], y=subset['ViolentCrimesPerPop'], mode='markers', name='Age_12To29'))
fig_age.add_trace(go.Scatter(x=subset['agePct16t24'], y=subset['ViolentCrimesPerPop'], mode='markers', name='Age_16To24'))
fig_age.add_trace(go.Scatter(x=subset['agePct65up'], y=subset['ViolentCrimesPerPop'], mode='markers', name='Age_65Up'))
fig_age.update_layout(title='Edades por Violencia', xaxis_title='Porcentaje de Edades', yaxis_title='Crímenes Violentos por Población')

fig_race = go.Figure()
fig_race.add_trace(go.Scatter(x=subset['racepctblack'], y=subset['ViolentCrimesPerPop'], mode='markers', name='Black'))
fig_race.add_trace(go.Scatter(x=subset['racePctWhite'], y=subset['ViolentCrimesPerPop'], mode='markers', name='White'))
fig_race.add_trace(go.Scatter(x=subset['racePctAsian'], y=subset['ViolentCrimesPerPop'], mode='markers', name='Asian'))
fig_race.add_trace(go.Scatter(x=subset['racePctHisp'], y=subset['ViolentCrimesPerPop'], mode='markers', name='Hispanic'))
fig_race.update_layout(title='Razas por Violencia', xaxis_title='Porcentaje de Raza', yaxis_title='Crímenes Violentos por Población')

fig_socioeconomic = go.Figure()
fig_socioeconomic.add_trace(go.Scatter(x=subset['medIncome'], y=subset['ViolentCrimesPerPop'], mode='markers', name='medIncome'))
fig_socioeconomic.add_trace(go.Scatter(x=subset['pctWWage'], y=subset['ViolentCrimesPerPop'], mode='markers', name='pctWWage'))
fig_socioeconomic.add_trace(go.Scatter(x=subset['pctWFarmSelf'], y=subset['ViolentCrimesPerPop'], mode='markers', name='pctWFarmSelf'))
fig_socioeconomic.add_trace(go.Scatter(x=subset['pctWInvInc'], y=subset['ViolentCrimesPerPop'], mode='markers', name='pctWInvInc'))
fig_socioeconomic.add_trace(go.Scatter(x=subset['pctWSocSec'], y=subset['ViolentCrimesPerPop'], mode='markers', name='pctWSocSec'))
fig_socioeconomic.add_trace(go.Scatter(x=subset['pctWPubAsst'], y=subset['ViolentCrimesPerPop'], mode='markers', name='pctWPubAsst'))
fig_socioeconomic.add_trace(go.Scatter(x=subset['pctWRetire'], y=subset['ViolentCrimesPerPop'], mode='markers', name='pctWRetire'))
fig_socioeconomic.update_layout(title='Características Socioeconómicas por Violencia', xaxis_title='Porcentaje', yaxis_title='Crímenes Violentos por Población')



fig_hist_alcohol = px.histogram(df2, x="alcohol", y="alcohol",color="class",title="Cantidad de alcohol", barmode="overlay",  category_orders={"Clases":["1","2","3"]})
fig_hist_malic_acid = px.histogram(df2, x="malic_acid", y="malic_acid",color="class",title="Cantidad de acido malico", barmode="overlay",  category_orders={"Clases":["1","2","3"]})

fig_phenols_flavanoids = px.scatter(df2, x = "total_phenols", y = "flavanoids", color = "class")

fig_od_flavanoids = px.scatter(df2, x = "proline", y = "flavanoids", color = "class")

#fig_phenols_flavanoids = go.Figure()
#fig_phenols_flavanoids.add_trace(go.Scatter(x=subset['total_phenols'], y=subset['flavanoids'],  mode='markers', name='Total Phenols'))
#fig_phenols_flavanoids.update_layout(title='Total Phenols vs. Flavanoids', xaxis_title='Total Phenols', yaxis_title='Flavanoids')

fig_ps3 = go.Figure()
fig_ps3.add_trace(go.Scatter(x=df3['CO(GT)'], y=df3['PT08.S3(NOx)'], mode='markers', name='CO(GT)'))
fig_ps3.add_trace(go.Scatter(x=df3['NMHC(GT)'], y=df3['PT08.S3(NOx)'], mode='markers', name='NMHC(GT)'))
fig_ps3.add_trace(go.Scatter(x=df3['C6H6(GT)'], y=df3['PT08.S3(NOx)'], mode='markers', name='C6H6(GT)'))
fig_ps3.add_trace(go.Scatter(x=df3['NOx(GT)'], y=df3['PT08.S3(NOx)'], mode='markers', name='NOx(GT)'))
fig_ps3.add_trace(go.Scatter(x=df3['NO2(GT)'], y=df3['PT08.S3(NOx)'], mode='markers', name='NO2(GT)'))
fig_ps3.update_layout(title='RGases para PT08.S3(NOx)')




# Crear la aplicación Dash
app = dash.Dash(__name__)

# Definir el diseño de la aplicación
app.layout = html.Div([
    html.H1("VIZUALIZACION"),  # Agregar el título aquí
    dcc.Tabs(id='tabs', value='tab1', children=[
        dcc.Tab(label='Crimen', value='tab1', children=[
            dcc.Tabs(id='subtabs1', value='subtab1A', children=[
                dcc.Tab(label='Edades', value='subtab1A'),
                dcc.Tab(label='Razas', value='subtab2A'),
                dcc.Tab(label='Características Socioeconómicas', value='subtab3A')
            ]),
            html.Div(id='subcontent1')
        ]),
        dcc.Tab(label='Wine', value='tab2', children=[
            dcc.Tabs(id='subtabs2', value='subtab1B', children=[
                dcc.Tab(label='Histogramas de clases', value='subtab1B'),
                dcc.Tab(label='Total Phenols vs. Flavanoids', value='subtab2B'),
                dcc.Tab(label='proline vs. Flavanoids', value='subtab3B')
            ]),
            html.Div(id='subcontent2')
        ]),
        dcc.Tab(label='Clima', value='tab3', children=[
            dcc.Tabs(id='subtabs3', value='subtab1C', children=[
                dcc.Tab(label='Histogramas', value='subtab1C'),
                dcc.Tab(label='PT08.S3(NOx)', value='subtab2C'),
                dcc.Tab(label='PT08.S1(CO),PT08.S2(NMHC), PT08.S4(NO2), PT08.S5(O3)', value='subtab3C')
            ]),
            html.Div(id='subcontent3')
        ])
    ]),
    html.Div(id='content')
])

# Definir la función para actualizar el contenido según la pestaña y subpestaña seleccionadas

@app.callback(Output('subcontent1', 'children'),Input('subtabs1', 'value'))
def display_sub1(subtab):
    if subtab == 'subtab1A':
        return dcc.Graph(figure=fig_age)
    elif subtab == 'subtab2A':
        return dcc.Graph(figure=fig_race)
    elif subtab == 'subtab3A':
        return dcc.Graph(figure=fig_socioeconomic)
    
@app.callback(Output('subcontent2', 'children'),Input('subtabs2', 'value'), prevent_initial_call=True)
def display_sub2(subtab):
    if subtab == 'subtab1B':
        return dcc.Graph(figure=fig_hist_alcohol), dcc.Graph(figure=fig_hist_malic_acid)
    elif subtab == 'subtab2B':
        return dcc.Graph(figure=fig_phenols_flavanoids)
    elif subtab == 'subtab3B':
        return dcc.Graph(figure=fig_od_flavanoids)
    

@app.callback(Output('subcontent3', 'children'),Input('subtabs3', 'value'), prevent_initial_call=True)
def display_sub3(subtab):
    if subtab == 'subtab1C':
        return dcc.Graph(figure=fig_hist_alcohol)
    elif subtab == 'subtab2C':
        return dcc.Graph(figure=fig_ps3)
    elif subtab == 'subtab3C':
        return dcc.Graph(figure=fig_od_flavanoids)

# Definir la función para actualizar el contenido según la pestaña seleccionada

def render_content(tab):
    if tab == 'tab1':
        return html.Div([
            dcc.Tabs(id='subtabs1', value='subtab1A', children=[
                dcc.Tab(label='Edades', value='subtab1A'),
                dcc.Tab(label='Razas', value='subtab2A'),
                dcc.Tab(label='Características Socioeconómicas', value='subtab3A')
            ]),
            html.Div(id='subcontent')
        ])
    elif tab == 'tab2':
        return html.Div([
            dcc.Tabs(id='subtabs2', value='subtab1B', children=[
                dcc.Tab(label='Histogramas de clases', value='subtab1B'),
                dcc.Tab(label='Total Phenols vs. Flavanoids', value='subtab2B'),
                dcc.Tab(label='proline vs. Flavanoids', value='subtab3B')
            ]),
            html.Div(id='subcontent')
        ])
    elif tab == 'tab3':
        return html.Div([
            dcc.Tabs(id='subtabs3', value='subtab1C', children=[
                dcc.Tab(label='Histogramas', value='subtab1c'),
                dcc.Tab(label='PT08.S3(NOx)', value='subtab2c'),
                dcc.Tab(label='PT08.S1(CO),PT08.S2(NMHC), PT08.S4(NO2), PT08.S5(O3)', value='subtab3c')
            ]),
            html.Div(id='subcontent')
        ])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
