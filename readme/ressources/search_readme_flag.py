#-*- coding: utf-8 -*-
from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup
import getch
import random
import json
import time

url_base='http://192.168.0.13:8080/.hidden/'
readme_url=[]
count_readme=0

def parse_url(url):
    global count_readme
    body=urlopen(url)
    soup = BeautifulSoup(body, features="html.parser")
    for a in soup.find_all('a'):
        if a.get('href') == "README":
            readme_url.append(url+"README")
            #print(url+"README")
            count_readme+=1
        
        elif a.get('href') != "../":
            parse_url(url+a.get('href'))

parse_url(url_base)
#print("Il y a " + str(count_readme) + " readme dans ce .hidden")

for dionysos in readme_url:
    body=urlopen(dionysos)
    soup = str(BeautifulSoup(body, features="html.parser"))
    if "Toujours pas tu vas craquer non ?\n" != soup and "Non ce n'est toujours pas bon ...\n" != soup and soup != "Tu veux de l'aide ? Moi aussi !  \n" and soup.find("Demande ") == -1:
        print(soup)
