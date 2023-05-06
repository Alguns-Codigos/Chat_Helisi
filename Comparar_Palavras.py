
import re
import unicodedata
def limpa_texto(texto):
    texto_sem_acentos = ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    texto_sem_especiais = re.sub(r'[^\w\s-]', '', texto_sem_acentos)
    texto_limpo = texto_sem_especiais.strip().lower()
    texto_limpo = re.sub(r'[\s]+', ' ', texto_limpo) # AQUI VOCÊ COLOCA OQUE QUISER ENTRE OS ESPAÇOS
    texto_limpo = re.sub(r'[-]+', ' ', texto_limpo) # AQUI VOCÊ COLOCA OQUE QUISER ENTRE OS ESPAÇOS
    return texto_limpo

Lista_Nome = ['helisi','elisi',"helisa","elis","elisa","elica","elise",]

def Nome_Bot(txt):
    T = limpa_texto(str(txt))
    for i in Lista_Nome:
        if str(i).lower() in str(T).lower():
            #return str(T).lower().replace(str(i).lower(),'')
         return  True

        else:
            return False
print(Nome_Bot('Helisi Maradona'))


# vonversação programada -------------------------------------------------------------

Lista_Nome = ['helisi','elisi',"helisa","elis","elisa","elica","elise",]