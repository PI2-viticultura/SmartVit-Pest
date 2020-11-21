from flask import Blueprint, request
from flask_cors import CORS
import controllers.pest_controller as controller

app = Blueprint('pest', __name__)
CORS(app)


@app.route("/pest", methods=["POST"])
def pest():
    return controller.save_pest_request(request.json)


@app.route("/pest_by_winery/<string:winery_id>", methods=["GET"])
def pest_by_user(winery_id):
    return controller.get_by_winery(winery_id)
