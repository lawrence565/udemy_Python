from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect

dbPath = "database_test.db"
engine = create_engine('sqlite:///%s' % dbPath)
metadata = MetaData(engine)

Base = declarative_base()

class People(Base):
    __tablename__ = "people" # 這個 Attribute 需要
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    age = Column('age', Integer)

Session = sessionmaker(bind=engine)
session = Session()
metadata.create_all(engine)

# new1 = People(name="Jason", age=26)
# new2 = People(name="Edward", age=19)
# new3 = People(name="Eileen", age=28)
# new4 = People(name="John", age=30)

# # session.add(new1)
# # session.add(new2)
# # session.add(new3)
# # session.add(new4)

# session.commit()

# for row in session.query(People).all():
#     print(row.id, row.name, row.age)

# for row in session.query(People).filter_by(name="Lawrence"):
#     print(row.id, row.name, row.age)

inspector = inspect(engine)
print(inspector.get_table_names())

session.close()