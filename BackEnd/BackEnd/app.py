from flask import Flask, request
from flask_restful import Resource, Api
import psycopg2
import math
import json
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
    first_waypoint_coord = first_waypoint.split(",")
    second_waypoint_coord = second_waypoint.split(",")
    center_waypoint = [(second_waypoint[0]-first_waypoint_coord[0]), (second_waypoint_coord[1]-first_waypoint[1])]
    interval = math.sqrt((second_waypoint[0]-first_waypoint_coord[0])**2+(second_waypoint_coord[1]-first_waypoint[1])**2)

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
            print(json.loads(request.text))
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
            json = request.json['response']
            print(json['route']['shape'])
            if json is None:
                return {"post": []}
            routes = json['route']
            for route in routes:
                waypoints = route['shape']
                moyIndicator = []
                print(waypoints)
                #for index, waypoint in enumerate(waypoints):
                #       if index == len(request.args.get('waypoints'))
                #           break
                #       rqt = create_indicator_request(waypoint,waypoints[index+1])
                #       cursor.execute(rqt)
                #       listAccident = []
                #       for record in cursor:
                #           listAccident.append(record)
                #      moyIndicator.add(mean([accident for accident in listAccident]))
                #route['dangerLevel'] = mean(moyIndicator)
            #json['route'] = route
            #return {"response": json}
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

api.add_resource(ServiceIndicator,'/Indicator')
if __name__ == '__main__':
    app.run()

