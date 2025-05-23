from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated "database"
items = []
next_id = 1

# Create
@app.route('/items', methods=['POST'])
def create_item():
    global next_id
    data = request.json
    item = {'id': next_id, 'name': data.get('name')}
    items.append(item)
    next_id += 1
    return jsonify(item), 201

# Read All
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Read One
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

# Update
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    for item in items:
        if item['id'] == item_id:
            item['name'] = data.get('name', item['name'])
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

# Delete
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'})

if __name__ == '__main__':
    app.run(debug=True)
