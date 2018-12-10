from flask import Flask, request
from flask_restful import Resource, Api
import psycopg2
import math
from numpy import mean

app = Flask(__name__)

connectionString = "dbname=postgres user=postgres host=localhost password=postgres port=5432"

try:
    conn = psycopg2.connect(connectionString)
    cursor = conn.cursor()
except:
    print("Connection failed")

app.config['DEBUG'] = True

api = Api(app)

# rqt a modifier/utiliser plustard
# rqt = "SELECT indicateur " \
#         "FROM " \
#         "usager_accidente_par_vehicule as usg AND" \
#         "usg  LEFT OUTER JOIN ON type_vehicule ( usg.id_type_vehicule. = type_vehicule.id_typeVehicule) AND" \
#         "usg LEFT OUTER JOIN ON type_route ( usg.id_type_route. = type_route.id_typeRoute) AND" \
#         "usg LEFT OUTER JOIN ON meteo ( usg.id_meteo. = meteo.id_meteo)" \
#         "WHERE" \
#         "type_route.type_route = " + request.args.get('type_route')+ \
#         "AND usg.longitude < " + (waypoint['lon'] - interval)+ \
#         "AND usg.longitude > " + (waypoint['lon'] + interval)+ \
#         "AND usg.latitude < " + (waypoint['lat'] - interval)+ \
#         "AND usg.latitude > " + (waypoint['lat'] + interval)


def create_indicator_request(first_waypoint,second_waypoint):
    center_waypoint = {'lon': (second_waypoint['lon']-first_waypoint['lon']), 'lat': (second_waypoint['lat']-first_waypoint['lat'])}
    interval = math.sqrt((second_waypoint['lon']-first_waypoint['lon'])**2+(second_waypoint['lat']-first_waypoint['lat'])**2)

    rqt = "SELECT indicateur " \
        "FROM " \
        "usager_accidente_par_vehicule as usg" \
        "WHERE" \
        "type_route.type_route = " + request.args.get('type_route')+ \
        "AND usg.longitude < " + (center_waypoint['x'] - interval)+ \
        "AND usg.longitude > " + (center_waypoint['x'] + interval)
    return rqt


class ServiceIndicator(Resource):
    def get(self):
        try:
            print(len(request.args))
            if request.args.get('id') is None:
                return {"gett": []}
            data = request.args
            route = []
          #   for index, waypoint in enumerate(request.args.get('waypoints')):
          #       if index == len(request.args.get('waypoints'))
          #       rqt = create_indicator_request(waypoint,request.args.get('waypoints'))[index])
          #       cursor.execute(rqt)
          #       listAccident = []
          #       for record in cursor:
          #           listAccident.append(record)
          #       route.add(mean([accident for accident in listAccident]))
          #
            id = request.args.get('id')
            rqt = "select * from test where id=" + id
            cursor.execute(rqt)
            list = []
            for record in cursor:
                list.append(record)
            return {"get": list}
        except:
            print("Request failed")

    def post(self):
        try:
            print(len(request.args))
            if request.args.get('id') is None:
                return {"postt": []}
            data = request.args
            route = []
            #   for index, waypoint in enumerate(request.args.get('waypoints')):
            #       if index == len(request.args.get('waypoints'))
            #       rqt = create_indicator_request(waypoint,request.args.get('waypoints'))[index])
            #       cursor.execute(rqt)
            #       listAccident = []
            #       for record in cursor:
            #           listAccident.append(record)
            #       route.add(mean([accident for accident in listAccident]))
            #
            id = request.args.get('id')
            rqt = "select * from test where id=" + id
            cursor.execute(rqt)
            list = []
            for record in cursor:
                list.append(record)
            return {"post": list}
        except:
            print("Request failed")

    def delete(self):
        return {"delete": "example"}

    def put(self):
        return {"put": "example"}

class Test(Resource):
    def post(self):
        try:
            bidule = request.get_json()

            for f in bidule["response"]["route"]:
                value = random.randint(0, 2)
                f["dangerLevel"] = str(value)
                print(f["dangerLevel"])

            return bidule
        except:
            print("Request failed")


api.add_resource(ServiceIndicator,'/Indicator')
api.add_resource(Test,'/test')
if __name__ == '__main__':
    app.run()

