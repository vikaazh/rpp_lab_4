from flask import Blueprint, request, jsonify, abort, render_template
from extensions import db, Region, Car_tax_param
bp = Blueprint('tax_route', __name__)


@bp.route("/v1/car/tax/calc", methods=['POST'])
def calc():
    data = request.get_json()
    city_id = data['city_id']
    hp_car = data['hp_car']
    production_year_car = data['production_year_car']
    id_exists = Car_tax_param.query.filter(Car_tax_param.city_id == city_id and Car_tax_param.from_hp_car <= hp_car and Car_tax_param.to_hp_car >= hp_car and Car_tax_param.from_production_year_car <= production_year_car and Car_tax_param.to_production_year_car >= production_year_car).first()
    if id_exists:
        rate = id_exists.rate
        message = {'tax': rate*int(hp_car)}
        return jsonify(message), 200
    else:
        abort(400)


@bp.route("/", methods=['GET'])
def index():
    return render_template('index.html')
