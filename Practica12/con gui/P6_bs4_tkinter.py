from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Progressbar
from bs4 import BeautifulSoup as bs
import requests
import os

def extract(link):
    req = requests.get(link)
    imgfile = open("images/{}".format(link.split("/")[-1]), "wb")
    imgfile.write(req.content)
    imgfile.close()

window = Tk()

window.title("Extraccion de imagenes de la web")

#window.geometry("320x569")

lbl = Label(window, text="Hola!")
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="Este script te ayudara a extraer imagenes de la web")
lbl2.grid(column=0, row=1)
lbl3 = Label(window, text="Escriba el link para empezar a extraer")
lbl3.grid(column=0, row=3)

entryBox = Entry(window, width=50)
entryBox.grid(column=0, row=5)

def buttYes():
    consoleLike = scrolledtext.ScrolledText(window)
    consoleLike.grid(column=0, row=10)
    #bar = Progressbar(window, length=100)
    #bar.grid(column=0, row=8)
    link = entryBox.get()
    req = requests.get(link)
    if req.status_code != 200:
        #print("Conexion rechazada.")
        consoleLike.insert(INSERT, "Conexion rechazada")
        exit()
    else:
        soup = bs(req.content, "html.parser")
        imgsrc = []

        for i in soup.find_all("img"):
            imgsrc.append(i.get("src"))
		
        os.system("mkdir images")
    
        #print("")
        consoleLike.insert(INSERT, "")
        
        #progressNum = 100 / len(imgsrc)
        #n = 1
        
        for i in imgsrc:
            if i.startswith("http") == False:
                imgdownload = link + i
                #print("Descargando imagen: " + imgdownload.split("/")[-1])
                consoleLike.insert(INSERT, "Descargando imagen: " + imgdownload.split("/")[-1] + "\n")
                extract(imgdownload)
            else:
                imgdownload = i
                #print("Descargando imagen: " + imgdownload.split("/")[-1])
                consoleLike.insert(INSERT, "Descargando imagen: " + imgdownload.split("/")[-1] + "\n")
                extract(imgdownload)
            #a = progressNum*n
            #bar["value"] = a
            #n = n + 1
    lbl4 = Label(window, text="Completado")
    lbl4.grid(column=0, row=8)
    
    lbl5 = Label(window, text="Puedes cerrar esta ventana")
    lbl5.grid(column=0, row=12)
    
boton = Button(window, text="Extraer", command=buttYes)
boton.grid(column=0, row=6)

window.mainloop()

