import uuid

from flask import Flask, request
from flask import jsonify

_contacts = [
    {'Id': str(uuid.uuid4()), 'FirstName': "Albert", 'LastName': "Einstein", 'PhoneNumber': "2222-1111"},
    {'Id': str(uuid.uuid4()), 'FirstName': "Mary", 'LastName': "Curie", 'PhoneNumber': "1111-1111"}
]

app = Flask(__name__)


@app.route('/', methods=['POST'])
def create_contact():
    """Creates a contact"""
    try:
        try:
            contact = request.get_json()
        except:
            raise ValueError
        if contact is None:
            raise ValueError

        id = str(uuid.uuid4())
        contact['Id'] = id

        _contacts.append(contact)

        response = app.response_class()
        response.status_code = 201
        response.headers['Location'] = f"/{id}"
        return response
    except ValueError:
        return '', 400


@app.route('/', methods=['GET'])
def get_all_contacts():
    """Gets all contacts"""
    return jsonify(_contacts)


@app.route('/<id>', methods=['GET'])
def get_contact(id):
    """Gets a specific contact"""
    _, contact = find_contact(id)
    if not contact:
        return '', 404

    return jsonify(contact)


@app.route('/<id>', methods=['PUT'])
def update_contact(id):
    """Updates a contact"""
    i, _ = find_contact(id)
    if i == -1:
        return '', 404

    try:
        try:
            contact = request.json
        except:
            raise ValueError
        if contact is None:
            raise ValueError

        _contacts[i] = contact
        return '', 204
    except ValueError:
        return '', 400


@app.route('/<id>', methods=['DELETE'])
def delete_contact(id):
    """Deletes a contact"""
    i, contact = find_contact(id)
    if not contact:
        return '', 404

    del _contacts[i]
    return '', 204


def find_contact(id):
    for i in range(len(_contacts)):
        if _contacts[i]['Id'] == id:
            return i, _contacts[i]
    return -1, None


if __name__ == '__main__':
    # todo: env
    app.debug = True
    app.run(host='0.0.0.0', port=8010)
