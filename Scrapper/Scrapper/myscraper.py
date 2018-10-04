# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 05:33:45 2018

@author: Ibrahima
"""
# import des librairies
import urllib2
from bs4 import BeautifulSoup as bfs




lesUrls=[] # tableau qui va contenir toutes les urls de la page
filenames =[] # tableau qui va contenir les noms des fichiers pdf
homepageUrl = "http://www.securite-routiere.gouv.fr"


def scraper_securite_routiere(urlPage):
        
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(urlPage,headers=hdr)
    page1 = urllib2.urlopen(req)
    
    #utilisation de beautifulSoup pour parser la page
    soup = bfs(page1,'html.parser')
    
    indicateurs = soup.find('div',attrs={'class':'cadre_avec_fleches'} )
    
    for i,link in enumerate(indicateurs.findAll('a')):
        
            downloadUrl = homepageUrl + link.get('href')
            
            if downloadUrl.endswith('.pdf'):
                #print downloadUrl
                lesUrls.append(downloadUrl)
                filenames.append(indicateurs.select('a')[i].attrs['href'])
            else :
                # scraping de la 2eme page 
                req2 = urllib2.Request(downloadUrl,headers=hdr)
                page2 = urllib2.urlopen(req2)
                soup2= bfs(page2,'html.parser')
                #print soup2
                for cpt, lien in enumerate(soup2.find_all('a')):
                    if lien.get('href').endswith('pdf'):
                        downloadlink =homepageUrl + lien.get('href')
                        lesUrls.append(downloadlink)
                        filenames.append(downloadlink)
             
                        
    names_urls = zip(filenames, lesUrls)
    
    for name, url in names_urls:
        url = urllib2.quote(url.encode('utf8'), ':/')
        rq = urllib2.Request(url,headers=hdr)
        res = urllib2.urlopen(rq)
        # rfind recupère la dernière occurence d'un char dans une string
        pdf = open(name[name.rfind('/') + 1:], 'wb')
        pdf.write(res.read())
        pdf.close()
    
     
   # ================ TEST ======================= 
# url de la page web a scrapper
pageUrl = "http://www.securite-routiere.gouv.fr/la-securite-routiere/l-observatoire-national-interministeriel-de-la-securite-routiere/accidentalite-routiere/indicateurs-locaux?xtmc=indicateurs&xtcr=8"

scraper_securite_routiere(pageUrl)

