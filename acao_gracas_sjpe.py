import streamlit as st
from conecta_db import conecta_db 
from datetime import datetime, timedelta

def import_content(hoje):

    db = conecta_db()

    cod_med = 'med' + str(hoje.day) + str(hoje.month) + '_' + str(hoje.year)
    cod_ora = 'ora' + str(hoje.day) + str(hoje.month) + '_' + str(hoje.year)
    cod_flo = 'flo' + str(hoje.day) + str(hoje.month) + '_' + str(hoje.year)

    posts_ref = db.child("prod").get()
    for doc in posts_ref.each():
        if doc.key() == cod_med:
            data_encontrada = doc.val()['data']
            meditacao = doc.val()["meditacao"]
        
        if doc.key() == cod_ora:
            oracao = doc.val()["oracao"]

        if doc.key() == cod_flo:
            flor = doc.val()["flor"]
    
    return meditacao, oracao, flor

def acao_de_gracas():

    hoje = datetime.today()

    try: 

        if hoje.weekday() == 3 or hoje.weekday() == 6:
            dt_tratada = hoje
        
        elif hoje.weekday() == 0:
            dt_tratada = hoje - timedelta(days=1)
        
        elif hoje.weekday() == 1:
            dt_tratada = hoje - timedelta(days=2)
        
        elif hoje.weekday() == 2:
            dt_tratada = hoje - timedelta(days=3)
        
        elif hoje.weekday() == 4:
            dt_tratada = hoje - timedelta(days=1)
        
        elif hoje.weekday() == 5:
            dt_tratada = hoje - timedelta(days=2)
        
        meditacao, oracao, flor = import_content(dt_tratada)

        st.title('Ação de Graças')
        st.header('Meditação do dia {}'.format(dt_tratada.strftime('%d/%m/%Y')))
        st.write('Segundo ensinamentos de São Pedro Julião Eymard')

        st.write('------------------')
        st.header('Meditação')
        st.markdown(meditacao)

        if st.checkbox('Oração'):
            st.markdown(oracao)

        st.write('------------------')

        if st.checkbox('Flor'):
            
            st.markdown(flor)

            st.markdown('''
            *Maria Santíssima, oferece a Jesus por nós estas minhas pequeninas flores. 
            Que por seus grandiosos méritos e intercessão, 
            que elas se tornem belíssimos ramalhetes, agradáveis ao teu filho, Jesus Cristo.*

            
>Nossa Senhora do Santíssimo Sacramento, *rogai por nós!*

**Amém.**''')
    
    except Exception as error:
        st.info('Opa! Tivemos um pequeno problema para exibir este conteudo :(')

        st.error(error)

        st.error('Este é o nome técnico do problema. Estamos trabalhando para arrumar, caso permaneça o problema, por gentileza entrar em contato conosco através da aba "Contato". Deus abençoe!')