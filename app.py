import streamlit as st
import pandas as pd
import plotly.express as px
# Leer el archivo CSV
df = pd.read_csv('/Users/joseangelmercadovazquez/analisis_exploratorio_de_datos_/vehicles_us.csv')
# Título de la app
st.header("Cuadro de Mandos - Análisis Exploratorio de Datos")

# Botón para el histograma
if st.button('Mostrar Histograma de Precios'):
    # Crear un histograma con Plotly Express
    fig_hist = px.histogram(df, x="price", title="Distribución de Precios de Coches")
    st.write("Distribución de precios")
    st.plotly_chart(fig_hist)

# Botón para el gráfico de dispersión
if st.button('Mostrar Gráfico de Dispersión'):
    # Crear un gráfico de dispersión con Plotly Express
    fig_scatter = px.scatter(df, x="odometer", y="price", title="Precio vs. Kilometraje")
    st.write("Relación entre precio y kilometraje")
    st.plotly_chart(fig_scatter)

# Opción extra con checkbox (opcional)
show_histogram = st.checkbox("Mostrar Histograma de Precios")
show_scatter = st.checkbox("Mostrar Gráfico de Dispersión")

if show_histogram:
    fig_hist = px.histogram(df, x="price", title="Distribución de Precios de Coches")
    st.write("Distribución de precios")
    st.plotly_chart(fig_hist)

if show_scatter:
    fig_scatter = px.scatter(df, x="odometer", y="price", title="Precio vs. Kilometraje")
    st.write("Relación entre precio y kilometraje")
    st.plotly_chart(fig_scatter)
