from mongoengine import *
import datetime
connect('trips')

class CustomDate(EmbeddedDocument):
    date = DateTimeField(default=datetime.datetime.utcnow)
    meta = {'allow_inheritance': True}

class Car(EmbeddedDocument):
    plate = StringField(required=True, max_length=6)

class Location(EmbeddedDocument):
    location_type = StringField(required=True, max_length=None)
    coordinates = ListField(field=DecimalField(), max_length=None, required=True)
    meta = {'allow_inheritance': True}

class CurrentInformation(EmbeddedDocument):
    status = StringField(required=True, max_length=6)
    updated_at = EmbeddedDocumentField(CustomDate)
    driver_location = EmbeddedDocumentField(Location)
    meta = {'allow_inheritance': True}

class Driver(EmbeddedDocument):
    first_name = StringField(required=True, max_length=200)
    last_name = StringField(required=True, max_length=200)
    car = EmbeddedDocumentField(Car)

class Passenger(EmbeddedDocument):
    first_name = StringField(required=True, max_length=200)
    last_name = StringField(required=True, max_length=200)

class StartTrip(EmbeddedDocument):
    pickup_location = EmbeddedDocumentField(Location)
    start_date = EmbeddedDocumentField(CustomDate)
    pickup_address = StringField(required=True, max_length=None)

class EndTrip(EmbeddedDocument):
    pickup_location = EmbeddedDocumentField(Location)
    end_date = EmbeddedDocumentField(CustomDate)
    pickup_address = StringField(required=True, max_length=None)

class TripInformation(EmbeddedDocument):
    start = EmbeddedDocumentField(StartTrip)
    end = EmbeddedDocumentField(EndTrip)
    price = DecimalField(required=True, min_value=0, precision=1)
    passenger = EmbeddedDocumentField(Passenger)
    driver = EmbeddedDocumentField(Driver)
    check_code = StringField(required=True, max_length=None)
    created_at = EmbeddedDocumentField(CustomDate)
    current_information = EmbeddedDocumentField(CurrentInformation)

class Trips(EmbeddedDocumentField):
    trips = EmbeddedDocumentField(TripInformation)

class City(EmbeddedDocumentField):
    name = StringField(required=True, max_length=200)
    trips = EmbeddedDocumentField(Trips)

class Country(Document):
    country = StringField(required=True, max_length=200)
    city = EmbeddedDocumentField(City)