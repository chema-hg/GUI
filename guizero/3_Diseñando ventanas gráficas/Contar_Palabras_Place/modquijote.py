import requests
import html2text
import re

def descargar_pagina(url):
    '''
    Lee una pagina web y la convierte en texto plano
    '''
    try:
        page = requests.get(url)
        if page.status_code != 200:
            return "Algo ha salido mal"
        content = html2text.html2text(page.text)
        return content
    except Exception:
        print("error")
    
def contar_palabras (texto) :
    '''
    Calcula la frecuencia de aparicion de cada palabra en un texto y genera una
    lista de pares (palabra, frecuencia) ordenada de mayor a menor frecuencia.
    '''
    frec={}
    texto = re.sub('[^\w\s]+', '', texto) # eliminamos signos de puntuación
    for w in texto.lower().split():
        if len(w)>4: # Para quitar las palabras muy cortas como preposiciones etc
            frec[w]=frec.get(w, 0)+1
    # Ordenamos el diccionario según los valores, no por las claves.
    frec_sorted = sorted(frec.items(), key=lambda x: x [1] , reverse=True)   
    return frec_sorted
       
