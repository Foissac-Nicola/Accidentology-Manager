from flask import Flask, request
from flask_restful import Resource, Api
import psycopg2
import math
import json
from numpy import mean

app = Flask(__name__)

connectionString = "dbname=accidentology_light user=postgres host=localhost password=postgres port=5432"

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
    first_waypoint_coord = [round(float(x),7) for x in first_waypoint.split(",")]
    second_waypoint_coord = [round(float(x),7) for x in second_waypoint.split(",")]
    center_waypoint = [round((second_waypoint_coord[0]+first_waypoint_coord[0])/2,7), round((second_waypoint_coord[1]+first_waypoint_coord[1])/2,7)]
    rayon = round(math.sqrt((center_waypoint[0]-first_waypoint_coord[0])**2)+((center_waypoint[1]-first_waypoint_coord[1])**2),7)
    rqt = ("SELECT avg(indicateur) " 
        "FROM " 
        "accident " 
        "WHERE "
        +str(rayon)+" > |/((accident.lon-("+str(center_waypoint[1])+"))^2+(+accident.lat-("+str(center_waypoint[0])+"))^2)")
    return rqt


class ServiceIndicator(Resource):
    def get(self):
        try:
            json = request.json['response']
            if json is None:
                return {"post": []}
            waypoint_interval = 100
            routes = json['route']

            for route in routes:
                waypoints = route['shape']
                moyIndicator = []
                for index, waypoint in enumerate(waypoints):
                    if index > len(waypoints)-waypoint_interval:
                        break

                    if index%waypoint_interval == 0:
                        rqt = create_indicator_request(waypoint,waypoints[index+waypoint_interval])
                        cursor.execute(rqt)
                        for record in cursor:
                            if record[0]:
                                moyIndicator.append(record[0])

                route['dangerLevel'] = mean(moyIndicator)

            json['route'] = route

            return {"response": json}
        except:
            print("Request failed")

    def post(self):
        try:
            json = request.json['response']
            if json is None:
                return {"post": []}
            waypoint_interval = 100
            routes = json['route']

            for route in request.json['response']['route']:
                waypoints = route['shape']
                moyIndicator = []
                cpt = 0
                for index, waypoint in enumerate(waypoints):
                    if index > len(waypoints)-waypoint_interval:
                        break

                    if index%waypoint_interval == 0:
                        cpt = cpt+1
                        print(cpt)
                        rqt = create_indicator_request(waypoint,waypoints[index+waypoint_interval])
                        cursor.execute(rqt)
                        for record in cursor:
                            if record[0]:
                                moyIndicator.append(record[0])

                route['dangerLevel'] = mean(moyIndicator)

            json['route'] = route

            return {"response": json}
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
