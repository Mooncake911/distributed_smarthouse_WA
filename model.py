from sqlalchemy import Boolean, Column, Integer, Identity, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from base import engine

# Создание базового класса для определения моделей
Base = declarative_base()


class Table1(Base):
    __tablename__ = "peripherals"
    id = Column(Integer)
    uni_id = Column(Integer, Identity(start=1), primary_key=True)
    name = Column(Text)
    attribute_name = Column(Text, ForeignKey("attributes.name"))
    attribute_rel = relationship("Table2")


class Table2(Base):
    __tablename__ = "attributes"
    name = Column(Text, primary_key=True)
    variable = Column(Boolean)
    var_type = Column(Text)
    upper_limit = Column(Text)
    lower_limit = Column(Text)
    is_input = Column(Boolean)
    is_output = Column(Boolean)


# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

table_dict = {"peripherals": Table1, "attributes": Table2}
