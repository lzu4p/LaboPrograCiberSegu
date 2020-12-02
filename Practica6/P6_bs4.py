#!/usr/bin/env python

from bs4 import BeautifulSoup as bs
import requests
import os

def extract(link, n):
	print("Descargando imagen: images({}).jpg".format(n))
	req = requests.get(link)
	imgfile = open("images/images{}.jpg".format(n), "wb")
	imgfile.close()
	print("Listo\n")

link = "https://www.minecraft.net"
req = requests.get(link)
print(req)
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

    for i in imgsrc:
        if i.startswith("http") == False:
            imgdownload = link + i
            print(imgdownload)
            extract(imgdownload, n)
        else:
            imgdownload = i
            print(imgdownload)
            extract(imgdownload, n)
        n = n + 1
