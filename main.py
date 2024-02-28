import requests
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dataclasses import dataclass
from producer import publish

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db = SQLAlchemy(app)


@dataclass
class Shop(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=False)
    shop_name: str = db.Column(db.String(200))
    shop_address: str = db.Column(db.String(200))

    def __repr__(self):
        return f'<Shop {self.shop_name} {self.shop_address}>'

    def __int__(self, shop_name, shop_address, **kwargs):
        self.shop_name = shop_name
        self.shop_address = shop_address


@dataclass
class Order(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=False)
    shop: str = db.Column(db.Integer)
    address: str = db.Column(db.String(200))

    def __repr__(self):
        return f'<Order {self.shop} {self.address}>'

    def __int__(self, shop, address, **kwargs):
        self.shop = shop
        self.address = address


migrate = Migrate(app, db)


@app.route("/api/v1/shops")
def index():
    shops = Shop.query.all()

    return jsonify(shops)


@app.route("/api/v1/orders/<int:id>/delivery", methods=['POST'])
def delivery_finish(id):
    publish("order_delivery_finished", id)

    return jsonify({'message': 'success'})


if __name__ == '__main__':
    app.app_context().push()
    db.create_all()

    app.run(debug=True, host='0.0.0.0', port=5001)
