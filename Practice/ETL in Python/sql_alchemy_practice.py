from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker

dbPath = "database_test.db"
engine = create_engine('sqlite:///%s' % dbPath)
metadata = MetaData(engine)
people = Table('People', metadata, Column('id', Integer, primary_key=True), Column('name', String), Column('age', Integer))
Session = sessionmaker(bind=engine)
sessoin = Session()
metadata.create_all(engine)
