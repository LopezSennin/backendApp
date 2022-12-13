from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/dbApp'
mongo = PyMongo(app)


@app.route('/peluqueria', methods=['POST'])
def create_peluqueria():
    nit = request.json['nit']
    nombre_peluqueria = request.json['nombre_peluqueria']
    nombre_owner = request.json['nombre_owner']
    cedula_owner = request.json['cedula_owner']

    if nit and nombre_peluqueria and nombre_owner and cedula_owner:
        value = mongo.db.peluqueria.insert(
            {'nit': nit, 'nombre_peluqueria': nombre_peluqueria, 'nombre_owner': nombre_owner, 'cedula_owner': cedula_owner}
        )
        response = jsonify({
            'id': str(value),
            'nit': nit,
            'nombre_peluqueria': nombre_peluqueria,
            'nombre_owner': nombre_owner,
            'cedula_owner': cedula_owner
        })
        response.status_code = 201
        return response
    else:
        return not_found()


@app.route('/peluqueria', methods=['GET'])
def get_peluqueria():
    peluquerias = mongo.db.peluqueria.find()
    response = json_util.dumps(peluquerias)
    return Response(response, mimetype='application/json')


@app.route('/peluqueria/<nit>', methods=['GET'])
def get_peluqueria(nit):
    peluqueria = mongo.db.peluqueria.find_one({'nit': int(nit)})
    response = json_util.dumps(peluqueria)
    return Response(response, mimetype="application/json")


@app.route('/peluqueria/<nit>', methods=['PUT'])
def update_peluqueria(nit):
    nombre_peluqueria = request.json['nombre_peluqueria']
    nombre_owner = request.json['nombre_owner']
    cedula_owner = request.json['cedula_owner']



@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'message': 'Resource Not Found: ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True)
