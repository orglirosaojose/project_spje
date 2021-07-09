import streamlit as st

def hinos_eucaristicos():

    st.title("Hinos Eucaristicos(em vídeo)")

    opcao = st.selectbox('Escolha o hino que gostaria de assistir:', ['Selecione o hino desejado', 'Adoro-Te Devote', 
                                                    'Eterna União', 'Anima Criste', 'Hóstia Santa'])

    if opcao == 'Selecione o hino desejado':

        st.image('images/sjpii_music.jpg')

    elif opcao == 'Adoro-Te Devote':
        st.header('Adoro te')
        st.video('https://www.youtube.com/watch?v=ON9srmxr1LQ')
    
    elif opcao == 'Eterna União':
        st.header('Eterna União - Coral Canção Nova')
        st.video('https://www.youtube.com/watch?v=s1VjNZ6p2cs&t=28s')

    elif opcao == 'Hóstia Santa':
        st.header('Oh, Hóstia Santa - Coral Canção Nova')
        st.video('https://www.youtube.com/watch?v=Gxh-I0ax9mQ')
    


        