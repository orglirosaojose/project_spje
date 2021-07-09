import streamlit as st
from hinos_eucaristicos import hinos_eucaristicos
from santos_testemunhos import santos_testemunhos
from acao_gracas_sjpe import acao_de_gracas
from oracoes_fixas import oracoes_fixas
from save_on_firestore import cadastro_email

#Pagina incial - Fixo
st.sidebar.write("""
#### A.M.D.G
Ad maiorem Dei gloriam
""")
opcoes = ["Página inicial", "Ação de Graças", "Ação de Graças Personalizada(NLP)",
           "Orações fixas", "Testemunhos Eucarísticos", "Inteligência Artificial Eucarística",
           "N e w s - L e t t e r", "Hinos Eucarísticos(em vídeo)", "Contato"]

nav = st.sidebar.radio("Menu de navegação:", opcoes)

#Separação Menu
if nav == "Página inicial":
    st.title('Lírio Eucarístico')
    st.write("*Oferecido por:* Organização Lírios de São José")

    st.image('images/home.jpg')

    st.write('------------------------------------')
    st.title("Página inicial")
    st.subheader("Propósito, inspiração e funcionalidade")

    st.markdown('''
    ***Propósito***

     - Auxiliar de modo prático a Ação de Graças, com meditações, orações e ensinamentos da Igreja;
     - Realizar uma simples e constante formação Eucarística.
    
    ***Inspiração***
    
    A **Igreja Católica Apostólica Romana**, desde de sempre afirma que a Eucaristia é *verdadeiramente o Próprio Jesus Cristo!
    Seu Corpo, Sangue, Alma e Divindade.*

    Portanto o Sacramento da Comunhão, deve ser o momento mais sublime da vida de todo católico.
    Consequentemente a suma importância da Ação de graças por parte de cada fiel.

    *Um grande santo de nossa igreja, nomedo como **Apostolo da Eucaristia**, é São Pedro Julião Eymard.*
    
    Em seu livro **"Flores da Eucaristica"**, o qual será o pilar desta aplicação, ele diz:
    
    >"Consagrai à **ação de graças** meia hora se vos for possível, ou, pelo menos, um rigoroso quarto de hora(15 minutos). 
    >Daríeis prova de não ter coração e de não saber apreciar devidamente o que é a Comunhão, se, após haver recebido Nosso Senhor, nada sentísseis e não Lhe soubésseis agradecer.

    >E, durante o dia, sede como um santo que tivesse passado uma hora no Céu; não vos esqueçais da visita régia de Jesus."
    
    ***A flor.***

    Alem das meditações e orações, São Pedro Julião, reforça a importância de também oferecermos algo a Jesus Eucarístico.

    Ele diz:
    "Antes de vos retirar, oferecei-lhe um ramalhete de amor, isto é, algum sacrifício a praticar durante o dia. 
    
    >Ah! não olheis a cruz natural do sofrimento. Contemplai esta cruz em Nosso Senhor e ela mudará de aspecto. 
    
    >Lembrai-vos de que a cruz é Jesus vindo repousar um pouco em nossa alma, a caminhar para o Calvário, e daí para o Céu."

    ***Funcionalidade***

    A principal função deste pequeno portal é a opção *'Ação de graças'* localizado no menu a esquerda.

    Nesta opção, será realizado uma atualização periódica automática, 
    todas as **Quintas e Domingo, com diferentes meditações, orações e flores, seguindo um caminho 
    Eucarístico com São Pedro Julião Eymard.**
    ''')

elif nav == "Ação de Graças":
    acao_de_gracas()

elif nav == 'Orações fixas':
    oracoes_fixas()
    
elif nav == "Testemunhos Eucarísticos":
    santos_testemunhos()

elif nav == "Hinos Eucarísticos(em vídeo)":
    hinos_eucaristicos()

elif nav == "N e w s - L e t t e r":
    cadastro_email()

elif nav == "Inteligência Artificial Eucarística":
    st.header('Em construção...')

    st.image('images/construindo.jpg', width=500)

elif nav == "Ação de Graças Personalizada(NLP)":
    st.header('Em construção...')

    st.image('images/construindo.jpg', width=500)

elif nav == "Contato":
    st.title('Contato')

    st.markdown('''
    E-mail para contato:

    >org_lirios_sao_jose@hotmail.com
    
    ''')
#pass -> spje_rogai_nos
#pass github -> Spje_rogai_nos2
#user -> orglirosaojose