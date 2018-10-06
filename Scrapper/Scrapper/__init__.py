from Scrapper.scrapper import Scrapper
from Scrapper.scrapper import scrap_open_data_lr
from Scrapper.scrapper import scrap_data_gouv
from Scrapper.scrapper import scrap_score_test

if __name__ == "__main__":

    scrap_score_test(None)

    scrap = Scrapper()
    scrap.set_data_dir("./")

    urls = ["https://opendata.larochelle.fr/dataset/reseau-de-transport-cyclable-voie-bus",
            "https://opendata.larochelle.fr/dataset/stationnement-place-des-deux-roues-motorises",
            "https://opendata.larochelle.fr/dataset/occupation-du-domaine-public-travaux-sur-la-voirie"]

    scrap.get_links(urls, scrap_open_data_lr)
    scrap.get_link("https://www.data.gouv.fr/fr/datasets/base-de-donnees-accidents-corporels-de-la-circulation/",
                   scrap_data_gouv)



    scrap.download_data()
