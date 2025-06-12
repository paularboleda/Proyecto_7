import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Analisis de Venta de Vehículos Usados')

st.write('Esta aplicación muestra la frecuencia la distribución y relación con el precio en los datos de vehículos usados')

hist_button = st.button('Construir histograma según Odómetro') # crear un botón
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de venta de vehículos')
         
    # crear un histograma
    fig_1= px.histogram(car_data, x="odometer", color='condition', nbins=50)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_1, use_container_width=True)

    st.write('El histograma muestra la frecuencia de vehículos usados según su odometro, segmentado por condición del vehículo')

hist_button = st.button('Construir Gráfico de Dispersión: Odómetro vs. Precio') # crear un botón
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de gráfico de dispersión de odómetro vs. precio del vehículo usado por condición.')
         
    # crear gráfico de dispersión
    
    fig_2 = px.scatter(car_data, x="odometer", y="price", color='condition')
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_2, use_container_width=True)

    st.write('El gráfico de dispersión muestra la relación entre el odómetro de cada vehículo y su precio, segmentado por la condición.')
