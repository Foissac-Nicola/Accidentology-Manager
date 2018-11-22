from flask import Flask, request
from flask_restful import Resource, Api
import psycopg2

app = Flask(__name__)

connectionString = "dbname=postgres user=postgres host=localhost password=postgres port=5432"

try:
    conn = psycopg2.connect(connectionString)
    cur = conn.cursor()
except:
    print("Connection failed")

app.config['DEBUG'] = True

api = Api(app)


def create_indicator_requete():
    type_vehicule = request.args.get('type_vehicule')
    type_route = request.args.get('type_route')
    meteo = request.args.get('meteo')
    cat_usager = request.args.get('cat_usager')

    rqt = "SELECT indicateur " \
        "FROM " \
        "usager_accidente_par_vehicule as usg AND" \
        "usg  LEFT OUTER JOIN ON type_vehicule ( usg.id_type_vehicule. = type_vehicule.id_typeVehicule) AND" \
        "usg LEFT OUTER JOIN ON type_route ( usg.id_type_route. = type_route.id_typeRoute) AND" \
        "usg LEFT OUTER JOIN ON meteo ( usg.id_meteo. = meteo.id_meteo) AND" \
        "WHERE" \
        "type_vehicule.type_vehicule = "+type_vehicule + \
        "type_route.type_route = " + type_route + \
        "meteo.conditions_meteo = " + meteo + \
        "usager.categorie_usager = " + cat_usager
    return rqt


class ServiceIndicator(Resource):
    def get(self):
        try:
            if request.args.get('id') is None:
                return {"get": []}

#           if (request.args.get('type_vehicule') is None or
#               request.args.get('type_route') is None or
#               request.args.get('meteo') is None or
#               request.args.get('categorie-usager') is None):
#               return {"get": []}

#           rqt = create_indicator_requete()

            id = request.args.get('id')
            rqt = "select * from test where id=" + id
            cur.execute(rqt)
            list = []
            for record in cur:
                list.append(record)
            return {"get": list}
        except:
            print("Request failed")

    def post(self):
        return {"post": list}

    def delete(self):
        return {"delete": "example"}

    def put(self):
        return {"put": "example"}


api.add_resource(ServiceIndicator,'/Indicator')
if __name__ == '__main__':
    app.run()

