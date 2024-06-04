from flask_restful import Resource
from flask import request, jsonify
from urllib.parse import parse_qs


lista_objetos_almacen = [
    {
        'id':1,
        'nombre':'Lapiz',
        'cantidad': 4
    },
    {
        'id':2,
        'nombre':'Pluma',
        'cantidad': 5
    },
    {
        'id':3,
        'nombre':'Goma',
        'cantidad': 10
    },
    {
        'id':4,
        'nombre':'Plumon',
        'cantidad': 9
    }
]

class HelloWorld(Resource):
    def get(self):
        return { "message":"Hola mundo", "status":200 }
    

class Almacen(Resource):

    def get(self):
        parametro_id = request.args.get('id')
        parametro_nombre = request.args.get('nombre')
        if parametro_id != None:
            for objeto in lista_objetos_almacen:
                if objeto.get('id') == int(parametro_id):
                    return {'Objeto': objeto, 'status': 200}
            return{'Mensaje': 'Objeto no encontrado', 'status':200}
    
        if parametro_nombre:
            for objeto in lista_objetos_almacen:
                if objeto.get('nombre') == parametro_nombre:
                    return {'Objeto': objeto, 'status':200}
            return {'Mensaje': 'Objeto no encontrado', 'status':404}


        return{'Objetos': lista_objetos_almacen, 'status':200}
    def post(self):

        data = request.get_json()
        lista_objetos_almacen.appen(data)
        return {'Receiced': True, 'status':200, 'info': data}

class APIRoutes():
    def init_routes(self, api):
        api.add_resource(HelloWorld, '/')
        api.add_resource(Almacen, '/objetos_almacen')