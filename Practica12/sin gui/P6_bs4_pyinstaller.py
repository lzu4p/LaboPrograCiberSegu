from bs4 import BeautifulSoup as bs
import requests
import os

def extract(link, n):
    req = requests.get(link)
    imgfile = open("images/{}".format(imgdownload.split("/")[-1]), "wb")
    imgfile.write(req.content)
    imgfile.close()
    return print("Listo\n")

hola = """
Hola, este script te ayudara a extraer imagenes de
una pagina web

Escriba el link para empezar a extraer
"""
print(hola)
link = input(">")
req = requests.get(link)
if req.status_code != 200:
    print("Conexion rechazada.")
    exit()
else:
    soup = bs(req.content, "html.parser")
    imgsrc = []

    for i in soup.find_all("img"):
        imgsrc.append(i.get("src"))
		
    os.system("mkdir images")
    n = 1
    
    print("")
    
    for i in imgsrc:
        if i.startswith("http") == False:
            imgdownload = link + i
            print("Descargando imagen: " + imgdownload.split("/")[-1])
            extract(imgdownload, n)
        else:
            imgdownload = i
            print("Descargando imagen: " + imgdownload.split("/")[-1])
            extract(imgdownload, n)
        n = n + 1

input("press any key to continue...                     xd")
