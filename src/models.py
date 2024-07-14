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
    
    favoritos_planetas = relationship('FavoritePlanet', backref='user')
    favoritos_personajes = relationship('FavoriteCharacter', backref='user')
    favoritos_vehiculos = relationship('FavoriteVehicle', backref='user')
    
    seguidores = relationship(
        'Follow', 
        foreign_keys='Follow.followed_id',
        backref='followee'
    )
    seguidos = relationship(
        'Follow', 
        foreign_keys='Follow.follower_id',
        backref='follower'
    )

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

    favoritos = relationship('FavoritePlanet', backref='planet')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    altura = Column(Integer)
    peso = Column(Integer)
    genero = Column(String(20))
    especie = Column(String(100))

    favoritos = relationship('FavoriteCharacter', backref='character')

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    modelo = Column(String(100))
    color = Column(String(100))
    pasajeros = Column(Integer)
    capacidad_carga = Column(String(50))

    favoritos = relationship('FavoriteVehicle', backref='vehicle')

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)

class FavoriteVehicle(Base):
    __tablename__ = 'favorite_vehicle'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=False)

class Follow(Base):
    __tablename__ = 'follow'
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    followed_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
