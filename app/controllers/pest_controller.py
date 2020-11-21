from models.pest import MongoDB
from bson.json_util import dumps


def save_pest_request(request):
    fields = ['idVineyard', 'type', 'startTime']

    if not all(field in request.keys() for field in fields):
        return {
            "erro": "Preencha os campos obrigatórios!"
        }, 400

    if not request["type"]:
        return {
            "erro": "Informe o tipo de praga!"
        }, 400

    if not request["startTime"]:
        return {
            "erro": "Informe a data de início da constatação da manifestação!"
        }, 400

    db = MongoDB()
    connection_is_alive = db.test_connection()

    if connection_is_alive:
        if(db.insert_one(request)):
            return {"message": "Sucess"}, 200
    db.close_connection()

    return {'error': 'Something gone wrong'}, 500


def get_by_winery(winery_id):
    db = MongoDB()
    connection_is_alive = db.test_connection()

    if connection_is_alive:
        pest = db.get_by_winery_id(winery_id)
        if pest:
            return dumps(pest), 200

    db.close_connection()

    return {'error': 'Something gone wrong'}, 500
