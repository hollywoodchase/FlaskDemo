from flask import Blueprint, request, jsonify
from app import db
from app.models import Item

main = Blueprint('main', __name__)

@main.route('/add_item', methods=['POST'])
def add_item():
    data = request.json
    new_item = Item(name=data['name'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item added", "item": new_item.to_dict()}), 201

@main.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])
