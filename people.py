from datetime import datetime
from flask import make_response, abort
from config import db
from models import Person, PersonSchema


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


def read_all():
    """
    Responds to a request for /api/people with the complete list of people

    :return:    json string of list of people
    """
    people = Person.query.order_by(Person.lname).all()

    # Serialize
    person_schema = PersonSchema(many=True)
    return person_schema.dump(people).data


def read_one(person_id):
    """
    Responds to a request for /api/people/{person_id}
    with one matching person from people

    :param person_id:   Id of person to find
    :return:        person matching id
    """
    person = Person.query.filter(Person.person_id == person_id).one_or_none()

    if person is not None:
        person_schema = PersonSchema()
        return person_schema.dump(person).data
    else:
        abort(404, f"Person not found for id: {person_id}")


def create(person):
    """
    Creates a new person based on the passed in person data

    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    person_check = (
        Person.query.filter(Person.fname == fname and Person.lname == lname)
        .one_or_none()
    )

    if person_check is None:
        schema = PersonSchema()
        new_person = schema.load(person, session=db.session).data

        db.session.add(new_person)
        db.session.commit()

        data = schema.dump(new_person).data
        return data, 201
    else:
        abort(406, f"Person {fname} {lname} already exists")


def update(person_id, person):
    """
    Updates an existing person in the people structure

    :param person_id:   id of the person to update
    :param person:      person to update
    :return:            updated person structure
    """
    update_person = Person.query.filter(
        Person.person_id == person_id
    ).one_or_none()

    if update_person is not None:
        schema = PersonSchema()
        update = schema.load(person, session=db.session).data

        update.person_id = update_person.person_id
        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_person).data

        return data, 200
    else:
        abort(404, f"Person not found for id: {person_id}")


def delete(person_id):
    """
    Deletes a person in the people structure

    :param person_id:   id of the person to delete
    :return:            200 on successful delete, 404 if not found
    """
    person = Person.query.filter(Person.person_id == person_id).one_or_none()

    if person is not None:
        db.session.delete(person)
        db.session.commit()
        return make_response(f"Person {person_id} deleted", 200)
    else:
        abort(404, f"Person not found for id: {person_id}")
