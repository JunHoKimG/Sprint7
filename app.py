import pandas as pd
import plotly as plot
import streamlit as st


 
data = pd.read_csv("vehicles_us.csv")

# Crear botones en la interfaz de Streamlit
build_hist = st.button('Mostrar histograma')
build_scatter = st.button('Mostrar gráfico de dispersión')

# Acción al presionar el botón del histograma
if build_hist:
    st.write('Generando un histograma con los datos de kilometraje de los vehículos.')

    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Histograma del kilometraje de los autos')

    st.plotly_chart(fig, use_container_width=True)

# Acción al presionar el botón del gráfico de dispersión
if build_scatter:
    st.write('Creando un gráfico de dispersión que relaciona el precio con el kilometraje.')

    fig = go.Figure(data=[go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers',
        marker=dict(opacity=0.6)
    )])

    fig.update_layout(
        title_text='Relación entre el kilometraje y el precio',
        xaxis_title='Kilometraje (odometer)',
        yaxis_title='Precio (USD)'
    )

    st.plotly_chart(fig, use_container_width=True)