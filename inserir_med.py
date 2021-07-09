import streamlit as st
from conecta_db import conecta_db  

db = conecta_db()

data = st.date_input("Insira a data de publicação:")
codigo_dma = str(data.day) + str(data.month) + '_' + str(data.year)

meditacao = st.text_area("Meditação:")
oracao = st.text_area('Oração:')
flor = soracao = st.text_area('Flor:')

submit = st.button("Cadastrar")

if meditacao and data and oracao and flor and submit:
    
    try:

        dic_insert={"data": str(data), "meditacao": meditacao}
        cod_med = 'med{}'.format(codigo_dma)
        db.child("prod").child(cod_med).set(dic_insert)


        dic_insert_ora={"data": str(data), "oracao": oracao}
        cod_ora = 'ora{}'.format(codigo_dma)
        db.child("prod").child(cod_ora).set(dic_insert_ora)


        dic_insert_flor={"data": str(data), "flor": flor}
        cod_flor = 'flo{}'.format(codigo_dma)
        db.child("prod").child(cod_flor).set(dic_insert_flor)

        st.info('Todos os cadastros foram realizados com sucesso.')
    
    except Exception as error:
        st.error('Infelizmente não foi possível realizar o cadastro')
        st.error(error)