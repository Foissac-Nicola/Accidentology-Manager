from Scrapper.scrapper import Scrapper

if __name__ == "__main__":

        scrap = Scrapper()
        scrap.set_data_dir("./")

        urls = ["https://opendata.larochelle.fr/dataset/reseau-de-transport-cyclable-voie-bus",
                "https://opendata.larochelle.fr/dataset/stationnement-place-des-deux-roues-motorises",
                "https://opendata.larochelle.fr/dataset/occupation-du-domaine-public-travaux-sur-la-voirie"]

        scrap.get_links(urls , scrap_open_data_lr)
        scrap.download_data()