import streamlit as st
import random
from conecta_db import conecta_db  

def cadastro_email():
    db = conecta_db()
    st.header('News Letter')
    
    email = st.text_input("Insira seu e-mail ou celular abaixo para receber nossa NewsLetter mensalmente:")
    nome = st.text_input("Seu nome(Opcional):")
    submit = st.button("Cadastrar")

    st.markdown(''' 
    ***Funcionalidade***
    
    Toda **primeira Quinta-Feira do mês,** será enviado uma News Letter 
    via E-mail ou WhatsApp(de acordo com modo escolhido acima).

    Nela constará alguns artigos e conteúdos da doutrina católica. 
    Além de um informativo das principais celebrações, liturgias e dias santos do respectivo mês.
    
    *E muito mais...*

    ''')

    if email and submit:

        try:
            data={"nome": nome, "email": email}

            id_fiel = 'fiel_{}'.format(random.randrange(1, 501))

            db.child("prod").child(id_fiel).set(data)
            st.info('Cadastro do e-mail realizado com Sucesso.')
            st.info('Deus abençõe!')

        except Exception as error:
            st.error('Infelizmente não foi possível realizar o cadastro, tente novamente mais tarde. Deus abençoe!')
            st.error(error)