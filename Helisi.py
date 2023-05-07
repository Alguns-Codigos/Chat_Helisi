"""instale esses primeiro
python.exe -m pip install --upgrade pip
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio
-------------------------------------
caso n prestar instale esses
pip win install pyaudio
pip install pyttsx3
"""
from  cores import *
from Helisi_Responde import Responda
from Cerebro import *
# Importa o módulo do Python para lidar com reconhecimento de fala
import speech_recognition as sr

import speech_recognition
import os

# Cria uma instância do Recognizer() para reconhecer a fala
rec = sr.Recognizer()


# Define uma função para tratar o texto reconhecido
def Tratamento(texto):

    if "bom dia".lower() in str(texto).lower() :
        print(ciano('-------------------------------- resposta programada'))
        Responda('Olá bom dia como Vai você')

    if "Abra insonia".lower() in str(texto).lower() or "Abra o insônia".lower() in str(texto).lower()  or "Abra ou insônia".lower() in str(texto).lower():
        print(ciano('-------------------------------- executando programa'))
        os.system(r"C:\Users\henri\AppData\Local\insomnia\Insomnia.exe")
        Responda('Abrindo o insônia')

    if "Abra o git".lower() in str(texto).lower() or "Abra github".lower() in str(texto).lower() or "Abra o kit".lower() in str(texto).lower() or "Abra o guia".lower() in str(texto).lower():
        print(ciano('-------------------------------- executando programa'))
        os.system(r"C:\Users\henri\AppData\Local\GitHubDesktop\GitHubDesktop.exe")
        Responda('Abrindo o Github')

    if "pesquise".lower() in str(texto).lower() or "pesquisar".lower() in str(texto).lower() or "o que é".lower() in str(texto).lower():

        from Pesquisa_na_Net import Pesquise
        Pesquise(texto)

    if "quanto é".lower() in str(texto).lower() or "calcula".lower() in str(texto).lower() or " Quanto que".lower() in str(texto).lower() :
        from Calcula_isso import calcular
        calcular(texto)

    else:
        from Pesquisa_na_Net import Pesquise
        Pesquise(texto)




# Define uma função que captura áudio do microfone e reconhece a fala
def vai_volta():

    with sr.Microphone(1) as mic2:
        # Ajusta o reconhecedor de voz para o nível de ruído ambiente
        rec.adjust_for_ambient_noise(mic2)
        print(amarelo("Pode falar que eu te escuto"))
        while True:
            audio = rec.listen(mic2)
            try:
                # Usa o Google para reconhecer a fala em português do Brasil
                texto = rec.recognize_google(audio, language="pt-BR")
                print(verde_negatigo(texto))

                # onde o programa reconhece o seu nome para analizar-------
                # ola Helisi tudo bem com você
                if "Helisi".lower() in str(texto).lower() or "Elisi".lower() in str(texto).lower()  or "Elisa".lower() in str(texto).lower() or "Elise".lower() in str(texto).lower():

                    Tratamento(texto)

                if "parar" in texto.lower():
                    print("Encerrando o programa...")
                    break

                else:
                    print(vermelho('Você nao disse o nome Helisi corretamente!'))

            except speech_recognition.exceptions.UnknownValueError as e:
                print(e)

# Chama a função vai_volta para executar o reconhecimento de fala
vai_volta()
