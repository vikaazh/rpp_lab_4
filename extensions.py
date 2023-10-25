from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Region(db.Model):
   __tablename__ = 'region'
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.VARCHAR(), nullable=False)
   car_tax_param = db.relationship('Car_tax_param', cascade='all', backref='region')
   area_tax_param = db.relationship('Area_tax_param', cascade='all', backref='region')


class Car_tax_param(db.Model):
   __tablename__ = 'car_tax_param'
   id = db.Column(db.Integer, primary_key=True)
   city_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)
   from_hp_car = db.Column(db.Integer, nullable=False)
   to_hp_car = db.Column(db.Integer, nullable=False)
   from_production_year_car = db.Column(db.Integer, nullable=False)
   to_production_year_car = db.Column(db.Integer, nullable=False)
   rate = db.Column(db.Numeric(10,2), nullable=False)


class Area_tax_param(db.Model):
   __tablename__ = 'area_tax_param'
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   city_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)
   rate = db.Column(db.Numeric(10,2), nullable=False)