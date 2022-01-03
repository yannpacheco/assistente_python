import pyttsx3
import speech_recognition as sr
import datetime
import time
import wikipedia as wiki
import pywhatkit
import pyautogui as py
from wikipedia.wikipedia import random
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from google_translate_py import Translator
import random
import time

owm = OWM('889441e6cf7d29d6ec2ed1548fa24d70')
mgr = owm.weather_manager()

audio = sr.Recognizer()

maquina = pyttsx3.init()

piadas = [
    'O que o pato disse para a pata?',
     'Vem Quá!', 
    'Porque o menino estava falando no telefone deitado?',
     'Para não cair a ligação',
    'Qual é a fórmula da água benta?',
     'H Deus Ó!',
    'Qual a cidade brasileira que não tem táxi?',
     'Uberlândia.',
    'O que o tijolo falou para o outro?',
     'Há um ciumento entre nós.',
    'Porque o jacaré tirou o filho da escola?', 
    'Porque ele réptil de ano.',
    'Qual o café que está sempre estressado?',
    'O caputinho',
    'Por que a mulher do Hulk se divorciou dele?',
    'Porque ela queria um homem mais maduro.',
    'Você sabe qual é o contrário de volátil?',
    'Vem cá sobrinho',
    'Se o cachorro tivesse religião, qual seria?',
    'Cão-domblé',
    'O que o tomate foi fazer no banco?',
    'Foi tirar extrato.',
    'Por que a Coca-Cola e a Fanta se dão muito bem?',
    'Porque se a Fanta quebra, a Coca, Cola!',
     ]


def executar_comando():
    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language="pt-BR")
            comando = comando.lower()
            if 'tina' in comando:
                comando = comando.replace('tina', '')
                #maquina.say(comando)
                #maquina.runAndWait()
                

    except:
        print('Microfone não está funcionando...')
    
    return comando



def comando_voz_usuario():
    
    comando = executar_comando()
    
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say(f'Agora são {hora}')
        maquina.runAndWait()

    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wiki.set_lang('pt')
        resultado = wiki.summary(procurar, 3)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()

    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando musica...')
        maquina.runAndWait()

    elif 'tempo' in comando:
        cidade = 'Contagem'
        w = mgr.weather_at_place(f'{cidade},BR').weather # localização
        temperatura = w.temperature('celsius')['temp'] # temperatura atual de hoje
        chuva = w.rain # previsão de chuva hoje
        # status = w.status // status do céu

        if chuva == {}:
            r_chuva = 'não há previsão de chuva para hoje!'
        else:
            r_chuva = 'há previsão de chuva hoje!'

        maquina.say(f'A temperatura atual em {cidade} é de {int(temperatura)} graus celsius e {r_chuva}') # termo final //
        maquina.runAndWait()

    elif 'traduza' in comando:
        text = comando.replace('traduza', '')
        traducao = Translator().translate(f"{text}", "pt", "en")
        print(traducao)
        maquina.say(f"traduzinho {text}")
        time.sleep(1)
        maquina.say(traducao)
        maquina.runAndWait()

    elif 'pesquisar por' in comando:
        busca = comando.replace('pesquisar por', '')
        pywhatkit.search(busca)
        maquina.say(f'pesquisando por {busca}')
        maquina.runAndWait()

    elif 'dia' in comando:
        data = datetime.datetime.now()
        maquina.say(f"hoje é {data.day} do {data.month} de {data.year}")
        maquina.runAndWait() 

    elif 'piada' in comando:
        i = random.randrange(0, len(piadas), 2)
        maquina.say(piadas[i])
        print(piadas[i])
        time.sleep(2)
        maquina.say(piadas[i+1])
        print(piadas[i+1])
        maquina.runAndWait()

   
    
    
        

comando_voz_usuario()











