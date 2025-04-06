# models.py
from sqlalchemy import Column, Integer, String, create_engine, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db.database import Base, engine
#import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True )
    hashed_password = Column(String)


class Monosillabs(Base):
    __tablename__ = "monosillabs"

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    order = Column(Integer)
    monousers = relationship("MonoUser", backref="monosillabs")

class MonoUser(Base):
    __tablename__ = "mono_user"

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    icon = Column(String)
    owner_id = Column(Integer, ForeignKey('monosillabs.order'))

Base.metadata.create_all(bind=engine)