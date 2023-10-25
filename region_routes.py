from flask import Blueprint, request, jsonify, abort, render_template
from extensions import db, Region
bp = Blueprint('region_routes', __name__)


@bp.route("/v1/region/add", methods=['POST'])
def add():
    data = request.get_json()
    id = data['id']
    name = data['name']
    id_exists = Region.query.filter(Region.id == id).first()
    if id_exists:
        abort(400)
    else:
        region = Region(id=id, name=name)
        db.session.add(region)
        db.session.commit()
        message = {'message': 'Region with name added'}
        return jsonify(message), 200


@bp.route("/v1/region/update", methods=['POST'])
def update():
    data = request.get_json()
    id = data['id']
    name = data['name']
    id_exists = Region.query.filter(Region.id == id).first()
    if id_exists:
        id_exists.name = name
        db.session.commit()
        message = {'message': 'Region name updated'}
        return jsonify(message), 200
    else:
        abort(400)


@bp.route("/v1/region/delete", methods=['POST'])
def delete():
    data = request.get_json()
    id = data['id']
    id_exists = Region.query.filter(Region.id == id).first()
    if id_exists:
        db.session.delete(id_exists)
        db.session.commit()
        message = {'message': 'Region with name deleted'}
        return jsonify(message), 200
    else:
        abort(400)


@bp.route("/web/region", methods=['GET'])
def region():
    query = Region.query.all()
    return render_template('region-list.html', query=query)


@bp.route("/web/region/add", methods=['GET'])
def region_add():
    return render_template('region-add.html')


@bp.route("/web/region/update", methods=['GET'])
def region_update():
    return render_template('region-update.html')


@bp.route("/web/region/delete", methods=['GET'])
def region_delete():
    return render_template('region-delete.html')
