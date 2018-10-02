# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 14:50:10 2018

@author: malik
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import urllib
import os
import time

if "data" not in os.listdir("."):
    os.mkdir("data")
    
def data_gouv():
    if "data-gouv" not in os.listdir("./data"):
        os.mkdir("data/data-gouv")
    
    url = "https://www.data.gouv.fr/fr/datasets/base-de-donnees-accidents-corporels-de-la-circulation/"
    
    requete = requests.get(url)
    content = requete.content
        
    soup = BeautifulSoup(content,'html.parser')
    
    resources = soup.find_all("article",{"class":"resource-card"})
    start_total_time = time.time()
    for resource in resources:
        url = resource.find("a",{"class":"btn-primary"}).attrs['href']
        name = resource.find("h4",{"class":"ellipsis"}).get_text()
        print("Enregistrement en cours de \'"+name+"\'")
        tic = time.time()
        urllib.request.urlretrieve(url,"data/data-gouv"+name)
        toc = time.time()
        print("Enregistrement terminé : ",toc - tic, " sec")
    end_total_time = time.time()
    print('data-gouv : Total time ', end_total_time - start_total_time, 'sec')
    
def opendata_lr():
    if "opendata-lr" not in os.listdir("./data"):
        os.mkdir("data/opendata-lr")
        
    base_url = "https://opendata.larochelle.fr/dataset/"
    urls = ["reseau-de-transport-cyclable-voie-bus",
            "stationnement-place-des-deux-roues-motorises",
            "occupation-du-domaine-public-travaux-sur-la-voirie"]

    start_total_time = time.time()
    for name in urls:
        url = base_url+name
        
        requete = requests.get(url)
        content = requete.content
             
        soup = BeautifulSoup(content,'html.parser')
        resource = soup.find("a",{"class":"icon-kml"}).attrs['href']
        print("Enregistrement en cours de \'"+name+"\'")
        tic = time.time()
        urllib.request.urlretrieve(resource,"data/opendata-lr/"+name+".kml")
        toc = time.time()
        print("Enregistrement terminé : ",toc - tic, " sec")    
    end_total_time = time.time()
    print('opendata-lr : Total time ', end_total_time - start_total_time, 'sec')
    
def scoresante():
#    if "scoresante" not in os.listdir("./data"):
#        os.mkdir("data/scoresante")
#        
#    url = "http://www.scoresante.org/sindicateurs_2015.html"
#        
#    driver = webdriver.PhantomeJS()
#    driver.get(my_url)
#    p_element = driver.find_element_by_id(id_='intro-text')
#    
#    resources = soup.find_all("article",{"class":"resource-card"})
#    start_total_time = time.time()
#    for resource in resources:
#        url = resource.find("a",{"class":"btn-primary"}).attrs['href']
#        name = resource.find("h4",{"class":"ellipsis"}).get_text()
#        print("Enregistrement en cours de \'"+name+"\'")
#        tic = time.time()
#        urllib.request.urlretrieve(url,"data/scoresante"+name)
#        toc = time.time()
#        print("Enregistrement terminé : ",toc - tic, " sec")
#    end_total_time = time.time()
#    print('scoresante : Total time ', end_total_time - start_total_time, 'sec')
    
#data_gouv()
#opendata_lr()
#scoresante()
    pass