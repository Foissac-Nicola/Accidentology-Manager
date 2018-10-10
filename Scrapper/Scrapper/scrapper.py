# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 14:50:10 2018

@author: malik
@author: nfoissac
@author: alexandre
"""


from requests import get as get_url
import urllib
from bs4 import BeautifulSoup as beautiful_soup
import dryscrape




class Scrapper:

    def __init__(self) -> None:
        self.__urls = []
        self.__dataDir = "."
        super().__init__()

    def append_url(self, url):
        if isinstance(url, str):
            self.__urls.append(url)
        return self

    def append_urls(self, urls):
        if isinstance(urls, list):
            self.__urls.extend(urls)
        return self

    def set_data_dir(self, path):
        if isinstance(path, str):
            self.__dataDir = path

    def get_links(self, urls, scrap_func):
        if isinstance(urls, list):
            for url in urls:
                self.get_link(url, scrap_func)

    def get_link(self, url, scrap_func):
        if isinstance(url, str):
            request = get_url(url)
            content = request.content
            self.__urls.extend(scrap_func(content))

    def download_data(self):
        for url in self.__urls:
            print(self.__dataDir+url[1])
            urllib.request.urlretrieve(url[0], str(url[1]))



def scrap_data_gouv(content):
    result = []
    soup = beautiful_soup(content, 'html.parser')
    tags = soup.find("section",{"class":"content"}).find_all("article",{"class":"resource-card"})
    for tag in tags:
        balises = tag.find_all("a",{"class":"btn-primary"})
        for balise in balises:
            if balise.get_text() == "Télécharger":
                url = balise.attrs['href']
                name = tag.find("h4",{"class":"ellipsis"}).get_text().translate(str.maketrans({'\"': '','\'': ''}))
                if url.split(".")[-1] == '':
                    name = name+".csv"
            result.append([url, name])
    return result


def scrap_open_data_lr(content):
    result = []
    soup = beautiful_soup(content, 'html.parser')
    tags = soup.find_all("a", {"class": "icon-kml"})
    for tag in tags :
        if tag != None:
            url =  tag.get('href')
            name = url.split("/")[-2]+"-"+url.split("/")[-1]+".kml"
            result.append([url,name])
    return result






def scrap_score_test(content):
    session = dryscrape.Session()
    session.set_attribute('local_storage_enabled')
    session.visit("http://www.scoresante.org/sindicateurs.html")
    response = session.body()
    b = session.at_xpath('//*[@id="treeArbreNoeudst4"]')
    b.click()
    b = session.at_xpath('//*[@id="treeArbreNoeudst13"]')
    b.click()
    b = session.at_xpath('//*[@id="treeArbreNoeudst18"]')
    b.click()
    b = session.at_xpath('//*[@id="treeArbreNoeudst21"]')
    b.click()
    b = session.at_xpath('//*[@id="treeArbreNoeudst22"]')
    b.click()
    b = session.at_xpath('//*[@id="SP_EXPO"]')
    b.click()
    b = session.at_xpath('//*[@id="ctl00_CPH1_ucArbreNoeuds_ucNoeudInfos_RB_SELECT_PARAM"]')
    b.click()
    # get departament option
    b = session.at_xpath('//*[@id="ctl00_CPH1_ucArbreNoeuds_ucNoeudInfos_ddlCriteresGeoExport"]')
    # find good option
    children = b.children()
    for child in children:
        if child['value'] == "DEP17" :
            child.select_option()
            pass

    # select export date 1
    b = session.at_xpath('//*[@id="ctl00_CPH1_ucArbreNoeuds_ucNoeudInfos_ddl_date1_export"]')
    b.children()[0].select_option()

    # select export date 2
    b = session.at_xpath('//*[@id="ctl00_CPH1_ucArbreNoeuds_ucNoeudInfos_ddl_date2_export"]')
    b.children()[-1].select_option()


    b = session.at_xpath('//*[@id="ctl00_CPH1_ucArbreNoeuds_ucNoeudInfos_ibn_Export_Csv"]')

    b.left_click()

    print(b)

    file = open("test.csv", "w")
    file.write(session.source())
    file.close()