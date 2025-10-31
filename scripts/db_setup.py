from sqlalchemy import create_engine, Column, Integer, String, Float, Date, TIMESTAMP, ForeignKey, MetaData, Table
from datetime import datetime

#  Database connection configuration
# Replace username and password with your PostgreSQL credentials if different
DB_URL = "postgresql://postgres:admin@localhost:5432/livestock_db"

# Create connection engine
engine = create_engine(DB_URL, echo=True)
meta = MetaData()

#  Farm Table
farm = Table(
    'farm', meta,
    Column('farm_id', Integer, primary_key=True),
    Column('location', String),
    Column('owner_name', String)
)

#  Animals Table
animals = Table(
    'animals', meta,
    Column('animal_id', Integer, primary_key=True),
    Column('name', String),
    Column('species', String),
    Column('farm_id', Integer, ForeignKey('farm.farm_id')),
    Column('birth_date', Date)
)

#  Sensors Table
sensors = Table(
    'sensors', meta,
    Column('sensor_id', Integer, primary_key=True),
    Column('type', String),
    Column('unit', String),
    Column('installed_on', Date),
    Column('animal_id', Integer, ForeignKey('animals.animal_id'))
)

#  Sensor Readings Table
sensor_readings = Table(
    'sensor_readings', meta,
    Column('reading_id', Integer, primary_key=True),
    Column('sensor_id', Integer, ForeignKey('sensors.sensor_id')),
    Column('timestamp', TIMESTAMP, default=datetime.now),
    Column('value', Float)
)

#  Alerts Table
alerts = Table(
    'alerts', meta,
    Column('alert_id', Integer, primary_key=True),
    Column('animal_id', Integer, ForeignKey('animals.animal_id')),
    Column('alert_type', String),
    Column('severity', String),
    Column('timestamp', TIMESTAMP, default=datetime.now)
)

#  Create all tables
meta.create_all(engine)
print(" All tables created successfully in livestock_db!")