# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 14:50:10 2018

@author: malik
"""

from bs4 import BeautifulSoup
import os
import csv
import requests
import urllib

url = "https://www.data.gouv.fr/fr/datasets/base-de-donnees-accidents-corporels-de-la-circulation/"

requete = requests.get(url)
content = requete.content


soup = BeautifulSoup(content,'html.parser')

resources = soup.find_all("article",{"class":"resource-card"})
for resource in resources:
    url = resource.find("a",{"class":"btn-primary"}).attrs['href']
    name = resource.find("h4",{"class":"ellipsis"}).get_text()
    print("Enregistrement en cours de "+name)
    data = requests.get(url).content
    urllib.request.urlretrieve(url,"data/"+name)
    print("Enregistrement terminé ")
