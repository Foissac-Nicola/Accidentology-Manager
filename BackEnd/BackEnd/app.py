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


class ServiceIndicator(Resource):
    def get(self):
        try:
            id = request.args.get('id')
            rqt = "select * from test where id="+id
            cur.execute(rqt)
            list = []
            for record in cur:
                list.append(record)
            return {"get": list}
        except:
            print("Request failed")

    def post(self):
        try:
            rqt = "select * from test"
            cur.execute(rqt)
            list = []
            for record in cur:
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

