import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    nombre = Column(String(100))
    apellido = Column(String(100))
    fecha_creacion = Column(DateTime, nullable=False)
    
    favoritos = relationship('Favorite', backref='user')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    clima = Column(String(100))
    terreno = Column(String(100))
    poblacion = Column(Integer)
    diametro = Column(Integer)
    periodo_orbital = Column(Integer)
    periodo_rotacion = Column(Integer)

    favoritos = relationship('Favorite', foreign_keys='Favorite.planet_id', backref='planet')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    altura = Column(Integer)
    peso = Column(Integer)
    genero = Column(String(20))
    especie = Column(String(100))

    favoritos = relationship('Favorite', foreign_keys='Favorite.character_id', backref='character')

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    modelo = Column(String(100))
    color = Column(String(100))
    pasajeros = Column(Integer)
    capacidad_carga = Column(String(50))

    favoritos = relationship('Favorite', foreign_keys='Favorite.vehicle_id', backref='vehicle')

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
