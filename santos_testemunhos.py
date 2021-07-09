import streamlit as st

def imagem_centralizada(caminho):
    col1, col2, col3 = st.beta_columns(3)

    with col2:
        st.image(caminho)

def santos_testemunhos():

    st.title('Testemunhos Eucaristicos')

    opcao = st.selectbox('Ver testemunho de:', ['Selecione a opção desejada', 'São João Paulo II', 
                                                'São João Maria Vianney', 'Irmã Clare Crockett', 
                                                'Santa Teresa D´Avila', 'Beato Carlo Acutis', 
                                                'São Pio X'])

    if opcao == 'Selecione a opção desejada':
        st.image('images/todos_santos3.jpg')

    elif opcao == 'São João Paulo II':
        st.markdown('''
        
        Quem o conheceu de perto relata que **São João Paulo passava horas diante do sacrário, ajoelhado ou prostrado**, várias vezes ao dia (chegando a vinte visitas por dia, segundo um sacerdote que vivia próximo do Papa), em momentos de intimidade e silêncio.

        Enquanto todos ainda estavam dormindo, 5:30h da manhã, já estava ele em sua capela particular. Depois celebrava a missa, durante o dia fazia a liturgia das horas, rezava pelos pedidos do mundo inteiro que chegavam até ele, fazia seus escritos e era assim até anoitecer quando todos novamente já estavam dormindo.

        O Cardeal Português, José Saraiva Martins, descreve o Papa como “o enamorado de Cristo”, e conta da maneira como ele se desligava de tudo quando estava em sua capela, era como se existisse somente ele e Deus.

        Certo dia, um de seus secretários, o Pe. John Magee, ao procurar João Paulo em seu quarto e na capela, não o encontrou. Pediram então que procurasse melhor na capela. Ao retornar no local, **o Papa estava sim na capela, prostrado no chão, em adoração ao Santíssimo Sacramento.**

        Seu professor de português, um brasileiro, Dom Fernando Guimarães, lembra das missas de que participou em sua capela particular. Eram apenas seis ou sete freiras brasileiras, quatro freiras polonesas que cuidavam do apartamento papal e os dois padres secretários. Ele conta que, quando chegavam de manhã à capela, o Papa já estava ajoelhado diante do sacrário, completamente absorvido pela presença de Deus, e essa absorção continuava durante toda a celebração. Dom Fernando diz que sempre tinha a impressão de ver um homem em diálogo com Deus o tempo inteiro da Missa.

        Em entrevista para agência Zenit, o postulador da causa de canonização, Slawomir Oder, conta que em uma de suas últimas viagens, o Papa já estava doente e precisou ser arrastado até o seu quarto. No dia seguinte sua cama estava intacta, pois havia passado a noite em oração, de joelhos no chão. Para ele, a oração era tão importante que, nos últimos meses de vida, ***pediu um espaço no seu quarto para o Santíssimo Sacramento.***
        
        São João Paulo II, rogai por nós!
        ''')

        imagem_centralizada('images/jpii.jpg')
    
    elif opcao == 'São João Maria Vianney':
        st.markdown(''' 
        
        São João Maria Vianney, o padroeiro dos sacerdotes, desponta para todos nós como um admirável exemplo a imitar no amor a Deus, que se faz presente no sacramento da Eucaristia. O amor do Cura D’Ars à Eucaristia era algo fascinante, pois, com simplicidade e humildade, ele demonstrava que há uma estreita relação entre o sacerdote e o sacrifício da Santa Missa, a Fonte primordial da santificação pessoal dos padres.

        Com admiráveis zelos pastorais, litúrgicos e eucarísticos, o Cura D’Ars foi um incansável catequista e um exímio pregador do Augustíssimo Sacramento do Altar. Aos sacerdotes, ele dizia: “Só no céu compreenderemos a felicidade de poder celebrar a Missa”.  Por ter sido um nobre adorador eucarístico, ele alimentava a sua vida de oração no sacrário da sua igreja, exercitando o silêncio da contemplação.

        Adoração e oração constituíam para ele a fonte bifocal de sua vida de sacerdote. Pela sua etiqueta eucarística, que se expressava nos cuidados com o material litúrgico e no zelo em realizar as genuflexões, ao passar diante do sacrário, com requintada piedade, o Cura D’Ars testemunhou aos habitantes de Ars e de outras cidades da França que nós necessitamos da união que o Cristo eucarístico nos propõe no cotidiano da História.

        Quando chegou à cidade de Ars, os habitantes da pequena localidade não vivenciavam a fidelidade aos mandamentos e à participação nos sacramentos como prioridades pessoais. Mas, com o passar do tempo e com a constante pregação de São João Maria Vianney, os habitantes daquela simples e rude aldeia **formaram uma comunidade penitencial e eucarística. E não poderia ser diferente, pois, como sabemos, um sacerdote eucarístico é um grande incentivador de almas eucarísticas, é um exemplo visível das maravilhas que o Corpo e o Sangue do Senhor realizam no íntimo das almas.** Nos dias do Cura D’Ars, e nestes nossos dias, os testemunhos eucarísticos dos sacerdotes dão inúmeros frutos na vida espiritual dos fiéis e colaboram no despertar de novas e generosas vocações.

        De joelhos e em silêncio diante do Tabernáculo do Altíssimo, São João Maria Vianney bradava que todos nós precisamos implantar, nas diversas horas do nosso dia, um autêntico e apropriado diálogo de salvação com o nosso Redentor. Este diálogo é mais fecundo quando é realizado na ação de graças da Santa Missa.

        ***O amor eucarístico do Cura D’Ars era manifestado também em seu trabalho pastoral, pois, em suas catequeses, apostolado e pregações, ele evidenciava a grandeza, a misericórdia e a sublimidade da bondade de Cristo que está à nossa espera no Sublime Sacramento do Altar.*** Em suas aulas de Catequese era comum ele dizer: “Quando se comungou, a alma impregna-se do bálsamo do amor como a abelha do perfume das flores”. Diante do sacrário, ele afirmava: “Sabemos pela fé que Deus está ali, no sacrário; abrimos-lhe o nosso coração e sentimo-nos felizes por sermos admitidos à Sua presença. É a melhor maneira de rezar”.

        Pelo conhecimento das palavras, gestos e atitudes do Cura D’Ars, nós percebemos que as diversas horas que ele destinava para ouvir as confissões dos penitentes eram, de uma certa forma, um cuidado e um zelo pela Eucaristia, pois, por ser um sacerdote de Cristo, ele tinha a plena certeza de que Deus não rejeita um coração puro, contrito e arrependido. Com esmero, ele também ensinava que, somente em estado de graça, nós podemos aproximar-nos do Altar do Senhor.

        A devoção do Santo Cura D’Ars para com nosso Senhor Jesus Cristo, que está presente no Sublime Sacramento, era realmente extraordinária. Guiados pelo exemplo do padroeiro dos sacerdotes, em suas Paróquias e Comunidades, os sacerdotes do mundo inteiro são convocados pelo próprio Cristo Eucarístico a se colocarem como instrumentos da comunhão que a Eucaristia realiza nas almas eucarísticas por meio do testemunho do acolhimento, da oração e pelo aprendizado da adoração.

        Por serem adoradores eucarísticos, os sacerdotes sabem e podem infundir em nossos corações o necessário respeito pelo sagrado e o imprescindível apreço pela presença de Deus em nosso meio. Desse modo, ao recordar os traços da piedade eucarística de São João Maria Vianney, ao relembrar as longas horas de adoração que ele passava diante do sacrário, nós somos chamados a colocar em destaque o nosso amor pela Eucaristia, o Alimento da vida sacerdotal e o Manancial de todas as graças.

        **Que São João Maria Vianney, o Cura d’Ars, nos ajude a compreender que precisamos participar da Eucaristia, pois não somos nada por nós mesmos.** Que a consciência da Presença real de Cristo no sacrário fortaleça sempre mais a nossa vontade de penetrar nos átrios do Banquete eucarístico e ali, em estado de graça, podermos bradar, juntos com o Cura D’Ars: “Jesus Cristo é nosso Senhor. Ele nos salva por Sua Cruz. O sofrimento dos homens os une à Cruz de Jesus e contribui para salvá-los. Ele está presente na Eucaristia”.

        ***Que o Cristo Eucarístico, pela intercessão do Santo Cura d’Ars, infunda em nosso coração um irrestrito amor pela Eucaristia*** e um infindável agradecimento pela doação, entrega e constante ajuda dos sacerdotes que, em nome de Deus, nos convocam a participar da comensalidade onde o nosso Redentor nos oferece o Seu Corpo, Sangue, Alma e Divindade, a fim de que possamos permanecer unidos a Ele na senda da justiça, da fé e da esperança.
        
        ''')

        imagem_centralizada('images/sao_joao_vianney.jpg')

    elif opcao == 'Irmã Clare Crockett':
        st.subheader('Irmã Clare Crockett')
        
        st.markdown('''
        
*Diz um sacerdote que há conheceu:*

> "O entusiasmo que ela tinha pela Eucaristia contagiava as crianças." 

*Mattehew Schmidt, aluno da Irmã Clare:*

> "A Irmã Clare transportava-nos verdadeiramente para o significado mais profundo da Eucaristia."
        
*Um relato de sua vida:*

> "Certa vez, quando as irmãs estavam indo levar a comunhão aos doentes, uma Hóstia consagrada acabou caindo na terra, Clare ficou em espantada e profundamente entristecida.
A Irmã Sara, logo pegou a comunhão do chão, Clare foi e beijou a terra, não se importando em ficar assim com o rosto todo sujo.

Equador, 2014/2015.

*Trecho de e-mail escrito pela própria Irmã Clare:*

> Por vezes imagino uma igreja antiga, pequena, numa pequena aldeia em Espanha. Tem um tabernáculo com a Eucaristia no seu interior. Quase ninguém lá vai para visitar o Senhor. Durante o dia, fujo para lá, para aquela pequena aldeia, descanso a minha testa no tabernáculo e acompanho o Senhor durante algum tempo. Isto faz-me UM BEM IMENSO.

        
Irmã Clare passou por um processo de conversão, antes vivia uma vida mundana e desregrada. 
Tinha o sonho de ser uma atriz famosa, *uma estrela de cinema com milhares e milhares de fãs*.
Entretanto graças a Misericórdia Divina, e o mérito da Clare em acolher, dizendo *sim* a sua vocação 
fez ela mudar completamente.

A partir dai a Irmã Clare entendeu que apenas **Um Fã é necessário**, apenas Um de sua plateia a motivava 
em dar seu melhor e sempre com uma alegria contagiante.

Sabemos que certamente este Fã é ***Jesus Eucarístico.***

Santo Afonso Maria de Ligório diz:
> "Quem não quer nada além de Deus, está sempre feliz em tudo o que acontece."
                
Em sua vida podemos ver o quão perfeito e esplêndido é o planos de Deus, em relação ao nosso. 
Em 2020 foi a primeira vez que ouvi falar dela, através do comentário de um amigo.
Então, já corri para o Google e digitei o nome dela.. 
*E PAH!* Logo de cara já apareceu diversos jornais, sites e revistas contando sua história, relatos de irmãs de sua congregação, 
tudo com uma grande quantidade de espectadores e acessos.
Tem um documentário só dela com milhares de visualizações.

Mas o melhor de tudo, e o que certamente ela nem **imaginava ou ousava pedir,** 
é o exemplo e impacto de sua vida nas pessoas *de todo o mundo*, transformando famílias,
suscitando jovens a buscar cada vez mais a santidade.

Isso perpetua até hoje em dia, fazendo dela ***sim*** uma **estrela, porem bem maior que 
uma estrela de Hollywood aqui do mundo, a Irmã Clare é uma estrela agora do Céu 
iluminando, intercedendo e dando exemplo a todos nós.**

Eis a verdadeira fama, a fama que todos nós deveríamos pedir e exalar em todos os lugares 
onde formos, assim como Clare fez.

Seu documentário, o qual se chama: "Ou Tudo ou nada", resume bem sua entrega, "tudo, 
pelo Tudo", como sempre diz São João da Cruz.

Todavia tudo isso não é uma surpresa, é apenas a loucura do Evangelho:
        
> "Porque o que quiser salvar a sua vida, irá perdê-la; mas o que perder a sua vida por amor de mim e do Evangelho, irá salvá-la." (Mc 8, 35)

> "E todo aquele que por minha causa deixar irmãos, irmãs, pai, mãe, mulher, filhos, terras ou casa ***receberá o cêntuplo e possuirá a vida eterna”.*** (Mt 19,29) 

Ela em sua caminhada entregou seus sonhos, deixou irmãos, pai, mãe, perdeu sua vida por amor..
 para agora receber o *cêntuplo e "el Paraiso"*.

Que a Irmã Clare, interceda a Deus por nós.

Nos ensinando a viver a ***Alegria Eucarística e a confiar nos Planos/Tempo/Misericórdia de Deus.***

Amém!
            ''')

        imagem_centralizada('images/irma_clare.jfif')
        
    elif opcao == 'Beato Carlo Acutis':
        st.header('Beato Carlo Acutis')
        st.markdown(''' 
            
            *Relatos sobre ele:*

            > "Carlo era um garoto absolutamente normal. Fazia as coisas que todas as crianças de hoje fazem: usava o computador, brincava com os amigos, levava uma vida semelhante à dos seus amigos."
            
            > "A única grande diferença é que havia colocado no centro de seu dia o encontro com Jesus Eucarístico com a Missa e da Adoração que fazia sempre antes ou depois da celebração."

            *Papa Francisco diz no dia de sua beatificação:*

            >Foi beatificado Carlo Acutis, um jovem de quinze anos, enamorado pela Eucaristia. Ele não se acomodou em uma confortável imobilidade, mas acolheu as necessidades de seu tempo, porque nos mais fracos via o rosto de Cristo.

            *A frase mais bela de Beato Carlo:*

            >"Eucaristia minha auto-estrada para o Céu."

            Que nosso querido Beato Carlo Acutis, interceda a Deus por nós! 
            
            ''')
        
        imagem_centralizada('images/beato_carlo_acutis.jpg')

    elif  opcao == 'Santa Teresa D´Avila':
        st.header('Santa Teresa D´Avila')
        st.markdown(''' 

>Quando eu me chegava à comunhão e recordava aquela altíssima Majestade que vira e pensava que era Ele que estava no Santíssimo Sacramento (tanto mais que muitas vezes quer o Senhor que eu O veja na hóstia), os cabelos se me eriçavam na cabeça e parecia que toda me aniquilava. Oh! Senhor meu! Mas se não encobrísseis vossa grandeza, quem ousara chegar tantas vezes a reunir coisa tão suja e miserável com tão grande Majestade? Bendito sejais, Senhor. Louvado sejais pelos anjos e por todas as criaturas, porque assim medis as coisas por nossa fraqueza para que, gozando de tão soberanas mercês, Vosso grande poder não nos assuste e, gente fraca e miserável que somos, não as ousemos gozar.

>Poderia nos acontecer o que, segundo sei ao certo, sucedeu a um lavrador. Encontrou um tesouro, que valia muito mais do que cabia no seu ânimo mesquinho; e vendo-se com aquela riqueza, deu-lhe uma tristeza tão grande que pouco a pouco veio a morrer de pura aflição, por não saber o que faria com o seu achado. Se não o encontrasse todo de uma vez, mas pouco a pouco lho fossem dando e sustentando com ele, viveria mais contente do que sendo pobre, e não lhe custaria a vida.

>Oh! Riqueza dos pobres, quão admiravelmente sabeis sustentar as almas e, sem que vejam tão grandes riquezas, pouco a pouco as ides mostrando! Quando eu vejo uma majestade tão grande dissimulada em coisa tão pouca como é a Hóstia, fico a admirar sabedoria tão imensa e não sei como me dá o Senhor ânimo e esforço bastante para chegar-me a Si; e se Ele, que me fez e ainda faz mercês tão grandes, ânimo não me desse, nem me seria possível dissimular, nem deixar de dizer aos brados tão grandes maravilhas. Pois que sentirá uma miserável como eu, carregada de abominações e que com tão pouco temor de Deus gastou a sua vida, ao se acercar deste Senhor de tão grande majestade, quando Ele quer que minha alma o veja? Uma boca que tantas palavras falou contra aquele mesmo Senhor, como se poderá juntar àquele corpo gloriosíssimo, cheio de pureza e piedade? E mais dói e aflige a alma, por não O haver servido, o amor que mostra aquele rosto de tanta formosura, com tão grande ternura e afabilidade — do que imprime temor a majestade que nEle se vê. Mas que poderia eu sentir nas duas vezes em que vi isso? Que direi?

>Uma vez, chegando-me à comunhão, vi com os olhos da alma dois demônios, mais claramente que com os olhos do corpo; tinham abominável figura. Parece-me que os seus cornos rodeavam a garganta do pobre sacerdote. E vi o meu Senhor, com a majestade em que já falei, na Partícula que eu ia receber, posto naquelas mãos que claramente mostravam ser criminosas e entendi que estava aquela alma em pecado mortal. Que seria, Senhor meu, ver Vossa formosura entre figuras tão abomináveis! Estavam eles como amedrontados e espantados diante de Vós. E de bom grado parece que fugiriam se Vós os deixásseis ir. Deu-me enorme perturbação e não sei como pude comungar; fiquei com grande temor, parecendo-me que, se fora visão de Deus, não permitira Sua Majestade visse eu o mal que estava naquela alma. Disse-me o próprio Senhor que rogasse por ele e que me permitira aquela vista a fim de que eu entendesse a força que têm as palavras da consagração e como não deixa Deus de estar ali, por mau que seja o sacerdote que as diz; e para que eu visse a sua grande bondade pondo-se nas mãos do seu inimigo — tudo para meu bem e bem de todos. Entendi quão mais obrigados que os outros estão os sacerdotes a ser bons, que coisa terrível é tomarem indignamente este Santíssimo Sacramento, e quão senhor é o demônio da alma que está em pecado mortal. Sobejo proveito me fez esta visão e sobejo conhecimento me deu do que devia a Deus. Bendito seja para todo o sempre.

''')
        imagem_centralizada('images/st_teresa_davila.jpg')

    elif  opcao == 'São Pio X':
        st.header('São Pio X')
        st.markdown(''' 
Algumas de suas belissimas frases:

>A devoção à eucaristia é a mais nobre de todas as devoções, porque tem
o próprio Deus por objeto; é a mais salutar porque nos dá o próprio autor
da graça; é a mais suave, pois suave é o Senhor.

>Se os anjos pudessem sentir inveja, nos invejariam porque podemos comungar.

''')
        imagem_centralizada('images/sao_piox.png')