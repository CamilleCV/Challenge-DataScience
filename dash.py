import streamlit as st
import pandas as pd
import plotly_express as px
from streamlit_option_menu import option_menu


st.set_page_config(layout="wide")

data = pd.read_csv('dados_tratados.csv')

st.title('''
    Analisando o DashBoard:
          ''')

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Churn', 'Gênero', 'Contrato','Idosos', 'Internet', 'Contrato'])
with tab1:
    fig = px.scatter(
        data.query('SeniorCitizen==0'),
        x='tenure',
        y='Charges.Total',
        color='Churn',
        title='Análise do Churn',
        labels={'Charges.Total':'Gastos Totais', 'tenure':'Tempo de Contrato Ativo'}
    )
    st.plotly_chart(fig)

with tab2:
    fig = px.scatter(
        data.query('SeniorCitizen==0'),
        x='tenure',
        y='Charges.Total',
        color='gender',
        title='Análise do Gênero',
        labels={'Charges.Total':'Gastos Totais', 'tenure':'Tempo de Contrato Ativo'}
    )
    st.plotly_chart(fig)

with tab3:

    tab1, tab2 = st.tabs(['Clientes', 'Não-Clientes'])
    with tab1:
        df = data[data['Churn'] == 'No']
        fig = px.scatter(
            df,
            x='tenure',
            y='Charges.Monthly',
            color='Contract',
            labels={'Charges.Monthly':'Gastos Mensais', 'tenure':'Tempo de Contrato Ativo'}
        )
        st.plotly_chart(fig)
    with tab2:
        df = data[data['Churn'] == 'Yes']
        fig = px.scatter(
            df,
            x='tenure',
            y='Charges.Monthly',
            color='Contract',
            labels={'Charges.Menthly':'Gastos Mensais', 'tenure':'Tempo de Contrato Ativo'}
        )
        st.plotly_chart(fig)

with tab4:
    fig = px.scatter(
        data.query('SeniorCitizen==1'),
        x='tenure',
        y='Charges.Total',
        color='Churn',
        title='Análise do Churn dos Idosos',
        labels={'Charges.Total':'Gastos Totais', 'tenure':'Tempo de Contrato Ativo'}
    )
    st.plotly_chart(fig)

with tab5:
    fig = px.histogram(data_frame=data, x='Churn', color='InternetService', title='Churn em relação ao Serviço de Internet dos Clientes', text_auto='True')
    st.plotly_chart(fig)

with tab6:
    fig = px.histogram(data_frame=data, x='tenure', color='Churn', title='Churn em relação ao Tempo de Contrato dos Clientes', text_auto='True')
    st.plotly_chart(fig)