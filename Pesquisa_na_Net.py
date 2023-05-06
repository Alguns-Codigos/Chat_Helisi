
# pip install googlesearch-python
# pip install bs4

from  cores import  *
from Helisi_Responde import Responda
from googlesearch import search
import requests
from bs4 import BeautifulSoup

def Pesquise(texto):
    print(ciano('-------------------------------- Pesquisando na net!'))
    try:
        # Define a pergunta a ser pesquisada
        pergunta = texto

        # Faz uma pesquisa no Google e extrai o primeiro resultado
        resultado = next(search(pergunta, num_results=1))

        # Faz uma requisição para o resultado obtido
        response = requests.get(resultado)

        # Extrai o conteúdo da página usando a biblioteca Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontra a resposta na página (assumindo que está em uma tag <p>)
        resposta = soup.find('p').text

        # Imprime a resposta
        print(resposta)
        Responda(texto + resposta)
        # Imprime os links

        for result in search(pergunta, num_results=1):
            print(result)


    except AttributeError:
        Responda('Erro ao conctar')