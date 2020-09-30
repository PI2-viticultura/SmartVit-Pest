from models.pest import MongoDB

def save_pest_request(request):
    fields = ['id_vinicola', 'tipo', 'inicio']

    if not all(field in request.keys() for field in fields):
        return {
            "erro": "Preencha os campos obrigatórios!"
        }, 400

    if not request["tipo"]:
        return {
            "erro": "Informe o tipo de praga!"
        }, 400

    if not request["inicio"]:
        return {
            "erro": "Informe a data de início da constatação da manifestação!"
        }, 400

    db = MongoDB()
    connection_is_alive = db.test_connection()
    
    if connection_is_alive:
        if(db.insert_one(request)):
            return {"message": "Sucess"}, 200
    db.close_connection()

    return {'error': 'Something gone wronfdslkjflksdjg'}, 500