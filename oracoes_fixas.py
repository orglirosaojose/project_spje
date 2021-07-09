import streamlit as st


def oracoes_fixas():
    oracoes_fixas = st.selectbox('Belíssimas orações Eucaristicas escritas por Santos da Igreja, selecione:', 
                                                        ['Selecione a oração desejada', 
                                                         'Santo Inácio – Anima Christi',
                                                         'Santo Afonso – Jesus no Santissimo Sacramento',
                                                         'São Tomas - Adoro-te devote', 
                                                         'São Padre Pio - Fica comigo Senhor', 'São José'])

    if oracoes_fixas == 'Selecione a oração desejada':
        st.image('images/oracao_santos.png')
    
    elif oracoes_fixas == 'Santo Inácio – Anima Christi':
        st.markdown('''
        Alma de Cristo,* santificai-me.*  
          
        Corpo de Cristo,* salvai-me.*  
          
        Sangue de Cristo,* inebriai-me.*  
          
        Água do lado de Cristo,* lavai-me.*  
          
        Paixão de Cristo,* confortai-me.*  
          
        Ó bom Jesus,* ouvi-me.*  
          
        Dentro de Vossas chagas,* escondei-me.*  
          
        Não permitais que me separe de Vós.  
          
        Do espírito maligno,* defendei-me.*  
          
        Na hora da minha morte,* chamai-me*  
          
        e mandai- me ir para Vós,   
         
        para que com os vossos Santos Vos louve *por todos os séculos dos séculos*.  
          
        ***Amém.***
        ''')

    elif oracoes_fixas == 'Santo Afonso – Jesus no Santissimo Sacramento':
        st.markdown('''
        ***Senhor meu Jesus Cristo***, que pelo amor que tendes aos homens estais de noite e de dia neste Sacramento, todo cheio de piedade e de amor, esperando, chamando e recebendo a todos os que vêem a visitar-vos: *eu creio que estais presente no Augusto Mistério do altar, Vos adoro desde o abismo de meu nada e vos dou graças por todas as mercês que me haveis feito, especialmente por haver-me dado neste Sacramento vosso Corpo, vosso Sangue, vossa Alma e vossa Divindade, por haver-me concedido como advogada a vossa Santíssima Mãe a Virgem Maria*, e por haver-me chamado a visitar-vos neste lugar santo.

        ***Adoro vosso amantíssimo Coração***, e desejo adorar-vos com três fins: *o primeiro, em agradecimento desta tão preciosa dádiva; o segundo, para desagravar-vos de todas as injurias que haveis recebido de vossos inimigos neste Sacramento, e o terceiro, porque desejo nesta visita adorar-vos em todos os lugares da terra, onde estais sacramentado com menos culto e mais esquecimento.*

        ''')

    elif oracoes_fixas == 'São Tomas - Adoro-te devote':
        st.markdown('''
        Eu vos adoro devotamente, ó Divindade escondida,
          
        Que verdadeiramente oculta-se sob estas aparências,
  
        A Vós, meu coração submete-se todo por inteiro,
  
        Porque, vos contemplando, tudo desfalece.
  
        A vista, o tato, o gosto falham com relação a Vós

        Mas, somente em vos ouvir em tudo creio.

        Creio em tudo aquilo que disse o Filho de Deus,

        Nada mais verdadeiro que esta Palavra de Verdade.

        Na cruz, estava oculta somente a vossa Divindade,

        Mas aqui, oculta-se também a vossa Humanidade.

        Eu, contudo, crendo e professando ambas,

        Peço aquilo que pediu o ladrão arrependido.

        Não vejo, como Tomé, as vossas chagas

        Entretanto, vos confesso meu Senhor e meu Deus

        Faça que eu sempre creia mais em Vós,

        Em vós esperar e vos amar.

        Ó memorial da morte do Senhor,

        Pão vivo que dá vida aos homens,

        Faça que minha alma viva de Vós,

        E que à ela seja sempre doce este saber.

        Senhor Jesus, bondoso pelicano,

        Lava-me, eu que sou imundo, em teu sangue

        Pois que uma única gota faz salvar

        Todo o mundo e apagar todo pecado.

        Ó Jesus, que velado agora vejo

        Peço que se realize aquilo que tanto desejo

        Que eu veja claramente vossa face revelada

        Que eu seja feliz contemplando a vossa glória. 

        Amem.
        ''')

    elif oracoes_fixas == 'São Padre Pio - Fica comigo Senhor':
        st.markdown('''
        *Fica, Senhor, comigo,* porque é necessária a Vossa presença para não Vos esquecer; sabeis quão facilmente Vos abandono.
        
        *Permanecei, Senhor, comigo,* pois sou fraco e preciso da Vossa força para não cair tantas vezes;
        porque Vós sois a minha luz e sem Vós estou nas trevas;
        pois Vós sois a minha vida e sem Vós esmoreço no fervor;
        para me dares a conhecer a Vossa vontade;
        para que ouça a Vossa voz e Vos siga, pois desejo amar-Vos muito e estar sempre em Vossa companhia.

        *Permanecei, Senhor, comigo,* se quereis que Vos seja fiel.
        
        *Permanecei, Senhor, comigo,* porque, por mais pobre que seja minha alma, deseja ser para Vós um lugar de consolação e um ninho de amor.
        
        *Permanecei, Jesus, comigo,* pois é tarde e o dia declina… Isto é, a vida passa, a morte, o juízo, a eternidade se aproximam e é preciso refazer minhas forças para não me demorar no caminho, e para isso tenho necessidade de Vós.

        Já é tarde e a morte se aproxima. Temo as trevas, as tentações, a aridez, a cruz, os sofrimentos, e quanta necessidade tenho de Vós, meu Jesus, nesta noite de exílio.
        *Permanecei, Jesus, comigo,* porque nesta noite da vida, de perigos, preciso de Vós. Fazei que, como Vossos discípulos, Vos reconheça na fração do pão, isto é, que a comunhão eucarística seja a luz que dissipe as trevas, a força que me sustente e a única alegria do meu coração.

        *Permanecei, Senhor, comigo,* porque na hora da morte quero ficar unido a Vós, senão pela comunhão, ao menos pela graça e pelo amor.
        
        *Permanecei, Jesus, comigo,* não Vos peço consolações divinas porque não as mereço, mas o dom de Vossa presença, assim, Vo-lo peço.
        
        *Permanecei, Senhor, comigo,* é só a Vós que procuro, Vosso amor, Vossa graça, Vossa vontade, Vosso coração, Vosso Espírito, porque Vos amo e não peço outra recompensa senão amar-Vos mais. Com um amor firme, prático, amar-Vos de todo o meu coração na terra para continuar a Vos amar perfeitamente por toda a eternidade. 
        
        Amém.

        ''')
    elif oracoes_fixas == 'São José':
        st.markdown(''' 
        Ó meu Pai e protetor, socorrei-me agora que não sei como agradecer a Jesus o singularíssimo benefício que me fez. 
        
        Vinde a meu coração, agradecei por mim e suplicai com vosso poder o que não podem os meus poucos méritos.

        Vós tivestes tantas vezes o menino Jesus em vosso braços e Ele agradava-se tanto em estar convosco

        Fazei-me companhia agora que está comigo e alcançai-me dele o que eu tanto vos peço.

        Amém. 
        ''')
