from flask import Flask
from extensions import db
from region_routes import bp as region_routes_bp
from tax_param_route import bp as tax_param_route_bp
from tax_route import bp as tax_route_bp


def main():
    app = Flask(__name__)
    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost/postgres"
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(region_routes_bp)
    app.register_blueprint(tax_param_route_bp)
    app.register_blueprint(tax_route_bp)
    app.run()


if __name__ == '__main__':
    main()
