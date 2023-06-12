#AVA actualmente funciona conectada a internet y sin interfaz GUI.
#Esta versión contiene funciones básicas
#NOTA: Para que AVA reconozca tu voz, debes tener un micrófono conectado a tu computadora
#y hablar claro.

#Librerías necesarias para que Ava funcione
import speech_recognition as sr
import subprocess as sub
import pyttsx3, pywhatkit, webbrowser,wikipedia,datetime,locale, keyboard, os
from pygame import mixer

name="Ava"
listener= sr.Recognizer()
engine=pyttsx3.init()

voices =engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #0 para voz en español, 1 para voz en inglés
engine.setProperty("rate",145) #Velocidad de la voz de Ava

#Sitios web que se pueden abrir
#Para agregar más sitios web, solo tienes que agregar una coma y poner el nombre del sitio web y la dirección web
sites = {
        'amazon':'https://www.amazon.com.mx',
        'mercadolibre':'https://www.mercadolibre.com.mx',
        'youtube':'https://www.youtube.com',
        'google':'https://www.google.com/?hl=es',
        'tiktok':'https://www.tiktok.com/es?lang=es',
        'facebook':'https://www.facebook.com',
        'whatsapp':'https://web.whatsapp.com',
        'twiter':'https://twitter.com',
        'canva':'https://www.canva.com',
        'github':'https://github.com',
        'instagram':'https://www.instagram.com',
        'plataforma':'https://plataforma.itdurango.edu.mx',
        'gmail':'https://mail.google.com/mail/u/0/#inbox',
        'udemy':'https://www.udemy.com'  
        #Puedes agregar más sitios web aquí, estos son solo algunos ejemplos     
        }
#Programas que se pueden abrir
#Para agregar más programas, solo tienes que agregar una coma y poner el nombre del programa y la ruta del archivo .exe
programs = {
        'chrome':"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        'valorant':"C:\\Riot Games\\Riot Client\\RiotClientServices.exe",
        'excel':"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
        'powerpoint':"C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",
        'word':"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
        #Puedes agregar más programas aquí, estos son solo algunos ejemplos
        }

comandos={'hola','abre','busca','reproduce','dime la fecha','qué hora es','comandos','terminar'}
#Función para que Ava hable
def talk(text):
    engine.say(text)
    engine.runAndWait()

#Función para que Ava escuche
def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            talk("¿Qué puedo hacer por ti?")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc,language="es")#Reconociendo de voz en español
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name,'')         
    except:
        talk('Lo siento, no pude entenderte')
        pass
    return rec

#Funciones de Ava
def run_ava():
    while True:
        rec = listen()
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            a=('Reproduciendo '+music)
            print(a)
            talk(a)
            pywhatkit.playonyt(music)    
        elif 'hola' in rec:     
            a=('Hola, ¿cómo estas?')
            print(a)
            talk(a)
        elif 'abre' in rec:
            #Abre sitios web
            for site in sites:
                if site in rec:
                    webbrowser.open(f'{sites[site]}')
                    talk(f'Abriendo {site}')  
            #Abre programas de la computadora
            for program in programs:
                if program in rec:
                    os.startfile(f'{programs[program]}')
                    talk(f'Abriendo {program}')
        elif 'busca' in rec:
            #Busqueda de contenido en Wikipedia 
            search = rec.replace('busca','')
            wikipedia.set_lang('es')
            wiki = wikipedia.summary(search,1)       
            a=('Buscando')
            b=("Aquí tienes el resultado de "+search)
            print(a)
            talk(a)
            print(b+": "+wiki)
            talk(b+": "+wiki)
        elif 'dime la fecha' in rec:
            locale.setlocale(locale.LC_ALL,'es')
            date = datetime.datetime.now().strftime('%A %#d de %B del %Y')
            talk(f'Hoy es {date}')
        elif 'qué hora es'in rec:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f'Son las {time}')
        elif 'comandos' in rec:
            talk('Estos son los comandos que puedo ejecutar')
            talk(comandos);
        elif 'terminar' in rec:
            talk('Adiós,que tengas un buen día')
            break
            #Comando para terminar la ejecución de AVA
    
if __name__ == '__main__':
    run_ava()