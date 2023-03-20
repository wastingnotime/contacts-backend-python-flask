import os
import uuid

from dotenv import load_dotenv
from flask import Flask, request
from flask import jsonify
from pony.orm import *

# configuration --------------
load_dotenv()
db_location = os.getenv("DB_LOCATION")
flask_debug = os.getenv("FLASK_DEBUG")


# database --------------
if flask_debug:
    set_sql_debug(True)

db = Database()


class Contact(db.Entity):
    id = PrimaryKey(str)
    firstName = Required(str)
    lastName = Required(str)
    phoneNumber = Required(str)


db.bind(provider='sqlite', filename=db_location, create_db=True)
db.generate_mapping(create_tables=True)

# api --------------
app = Flask(__name__)


@app.route('/contacts', methods=['POST'])
@db_session
def create_contact():
    """Creates a contact"""
    try:
        try:
            contact_payload = request.get_json()
        except:
            raise ValueError
        if contact_payload is None:
            raise ValueError

        id = str(uuid.uuid4())

        Contact(id=id, firstName=contact_payload['firstName'], lastName=contact_payload['lastName'],
                phoneNumber=contact_payload['phoneNumber'])

        response = app.response_class()
        response.status_code = 201
        response.headers['Location'] = f"/{id}"
        return response
    except ValueError:
        return '', 400


@app.route('/contacts', methods=['GET'])
@db_session
def get_all_contacts():
    """Gets all contacts"""
    contacts_payload = []

    contacts = select(c for c in Contact)
    for c in contacts:
        contacts_payload.append(c.to_dict())

    return jsonify(contacts_payload)


@app.route('/contacts/<id>', methods=['GET'])
@db_session
def get_contact(id):
    """Gets a specific contact"""
    try:
        contact = Contact[id]
    except ObjectNotFound:
        return '', 404

    return jsonify(contact.to_dict())


@app.route('/contacts/<id>', methods=['PUT'])
@db_session
def update_contact(id):
    """Updates a contact"""
    try:
        contact = Contact[id]
    except ObjectNotFound:
        return '', 404

    try:
        try:
            contact_payload = request.json
        except:
            raise ValueError
        if contact_payload is None:
            raise ValueError

        contact.firstName = contact_payload['firstName']
        contact.lastName = contact_payload['lastName']
        contact.phoneNumber = contact_payload['phoneNumber']

        return '', 204
    except ValueError:
        return '', 400


@app.route('/contacts/<id>', methods=['DELETE'])
@db_session
def delete_contact(id):
    """Deletes a contact"""
    try:
        contact = Contact[id]
    except ObjectNotFound:
        return '', 404

    contact.delete()

    return '', 204


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8010)
