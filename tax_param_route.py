from flask import Blueprint, request, jsonify, abort, render_template
from extensions import db, Region, Car_tax_param
bp = Blueprint('tax_param_route', __name__)


@bp.route("/v1/car/tax-param/add", methods=['POST'])
def add():
    data = request.get_json()
    id = data['id']
    city_id = data['city_id']
    from_hp_car = data['from_hp_car']
    to_hp_car = data['to_hp_car']
    from_production_year_car = data['from_production_year_car']
    to_production_year_car = data['to_production_year_car']
    rate = data['rate']
    city_id_exists = Region.query.filter(Region.id == city_id).first()
    if city_id_exists:
        id_exists = Car_tax_param.query.filter(Car_tax_param.id == id).first()
        if id_exists:
            abort(400)
        else:
            car_tax_param = Car_tax_param(id=id, city_id=city_id, from_hp_car=from_hp_car, to_hp_car=to_hp_car, from_production_year_car=from_production_year_car, to_production_year_car=to_production_year_car, rate=rate)
            db.session.add(car_tax_param)
            db.session.commit()
            message = {'message': 'Car tax param added'}
            return jsonify(message), 200
    else:
        abort(400)


@bp.route("/v1/car/tax-param/update", methods=['POST'])
def update():
    data = request.get_json()
    id = data['id']
    city_id = data['city_id']
    from_hp_car = data['from_hp_car']
    to_hp_car = data['to_hp_car']
    from_production_year_car = data['from_production_year_car']
    to_production_year_car = data['to_production_year_car']
    rate = data['rate']
    city_id_exists = Region.query.filter(Region.id == city_id).first()
    if city_id_exists:
        id_exists = Car_tax_param.query.filter(Car_tax_param.id == id).first()
        if id_exists:
            id_exists.from_hp_car = from_hp_car
            id_exists.to_hp_car = to_hp_car
            id_exists.from_production_year_car = from_production_year_car
            id_exists.to_production_year_car = to_production_year_car
            id_exists.rate = rate
            db.session.commit()
            message = {'message': 'Car tax param updated'}
            return jsonify(message), 200
    abort(400)


@bp.route("/v1/car/tax-param/delete", methods=['POST'])
def delete():
    data = request.get_json()
    id = data['id']
    city_id = data['city_id']
    city_id_exists = Region.query.filter(Region.id == city_id).first()
    if city_id_exists:
        id_exists = Car_tax_param.query.filter(Car_tax_param.id == id).first()
        if id_exists:
            db.session.delete(id_exists)
            db.session.commit()
            message = {'message': 'Car tax param deleted'}
            return jsonify(message), 200
    abort(400)


@bp.route("/v1/car/tax-param/get/all", methods=['GET'])
def get_all():
    query = Car_tax_param.query.all()
    info = {}
    for car_tax_param in query:
        info[car_tax_param.id] = {"city_id": car_tax_param.city_id, "from_hp_car": car_tax_param.from_hp_car, "to_hp_car": car_tax_param.to_hp_car, "from_production_year_car": car_tax_param.from_production_year_car, "to_production_year_car": car_tax_param.to_production_year_car, "rate": car_tax_param.rate}
    message = {'info': info}
    return jsonify(message), 200


@bp.route("/web/tax-param", methods=['GET'])
def tax_param():
    query = Car_tax_param.query.all()
    return render_template('tax-param-list.html', query=query)


@bp.route("/web/tax-param/add", methods=['GET'])
def tax_param_add():
    return render_template('tax-param-add.html')


@bp.route("/web/tax-param/update", methods=['GET'])
def tax_param_update():
    return render_template('tax-param-update.html')


@bp.route("/web/tax-param/delete", methods=['GET'])
def tax_param_delete():
    return render_template('tax-param-delete.html')