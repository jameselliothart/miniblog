from datetime import datetime
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with API
PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}


# Create handler to read (GET) people
def read_all():
    """
    Responds to a request for /api/people with the complete list of people

    :return:    json string of list of people
    """
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


def read_one(lname):
    """
    Responds to a request for /api/people/{lname}
    with one matching person from people

    :param lname:   last name of person to find
    :return:        person matching last name
    """
    if lname in PEOPLE:
        person = PEOPLE.get(lname)
    else:
        abort(404, f"Person with last name {lname} not found")

    return person


def create(person):
    """
    Creates a new person based on the passed in person data

    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp()
        }
        return make_response(f"{lname} successfully created", 201)
    else:
        abort(406, f"Person with last name {lname} already exists")


def update(lname, person):
    """
    Updates an existing person in the people structure

    :param lname:   last name of the person to update
    :param person:  person to update
    :return:        updated person structure
    """
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["timestamp"] = get_timestamp()

        return PEOPLE[lname]
    else:
        abort(404, f"Person with last name {lname} not found")


def delete(lname):
    """
    Deletes a person in the people structure

    :param lname:   last name of the person to delete
    :return:        200 on successful delete, 404 if not found
    """
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(f"{lname} successfully deleted", 200)
    else:
        abort(404, f"Person with last name {lname} not found")
