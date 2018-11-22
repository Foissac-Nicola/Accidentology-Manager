from flask import Flask, request
from flask_restful import Resource, Api
import psycopg2
from numpy import mean

app = Flask(__name__)

connectionString = "dbname=postgres user=postgres host=localhost password=postgres port=5432"

try:
    conn = psycopg2.connect(connectionString)
    cur = conn.cursor()
except:
    print("Connection failed")

app.config['DEBUG'] = True

api = Api(app)


def create_indicator_request(waypoint):
    interval = 10 # valeur à définir
    if request.args.get('type_route') is None:
        return

    rqt = "SELECT indicateur " \
        "FROM " \
        "usager_accidente_par_vehicule as usg AND" \
        "usg  LEFT OUTER JOIN ON type_vehicule ( usg.id_type_vehicule. = type_vehicule.id_typeVehicule) AND" \
        "usg LEFT OUTER JOIN ON type_route ( usg.id_type_route. = type_route.id_typeRoute) AND" \
        "usg LEFT OUTER JOIN ON meteo ( usg.id_meteo. = meteo.id_meteo)" \
        "WHERE" \
        "type_route.type_route = " + request.args.get('type_route')+ \
        "AND longitude < " + (waypoint['x'] - interval)+ \
        "AND longitude > " + (waypoint['x'] + interval)+ \
        "AND latitude < " + (waypoint['y'] - interval)+ \
        "AND latitude > " + (waypoint['y'] + interval)

    if request.args.get('type_vehicule') is not None:
        rqt += "AND type_vehicule.type_vehicule = "+request.args.get('type_vehicule')
    if request.args.get('type_vehicule') is not None:
        rqt += "AND meteo.conditions_meteo = " + request.args.get('meteo')
    if request.args.get('type_vehicule') is not None:
        rqt += "AND usager.categorie_usager = " + request.args.get('meteo')
    return rqt


class ServiceIndicator(Resource):
    def get(self):
        try:
            if request.args.get('id') is None:
                return {"get": []}

          # if (request.args.get('type_vehicule') is None or
          #     request.args.get('type_route') is None or
          #     request.args.get('meteo') is None or
          #     request.args.get('categorie-usager') is None):
          #     return {"get": []}
          #
          #   for waypoint in request.args.get('waypoints'):
          #       rqt = create_indicator_request(waypoint)
          #       cur.execute(rqt)
          #       listAccident = []
          #       for record in cur:
          #           listAccident.append(record)
          #       waypoint['Indicator'] = mean([accident[13] for accident in listAccident])

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

