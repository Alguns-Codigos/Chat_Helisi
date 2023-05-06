from  cores import  *
import pyttsx3

# Define uma função para responder ao usuário com voz
def Responda(texto):
    engine = pyttsx3.init()
    print(amarelo(f"Helisi Respndendo: {texto}"))
    # Fala o texto usando o engine
    engine.say(texto)
    engine.runAndWait()



    from  Helisi import vai_volta
    vai_volta()
