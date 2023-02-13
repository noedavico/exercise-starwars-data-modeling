import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    _tablename_ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    fecha_suscripcion =  Column(String(250), nullable=False)
    apellido =  Column(String(250), nullable=False)
    email =  Column(String(250), nullable=False)
    favoritos = relationship('Favoritos',backref='usuario', lazy=True)

class Personajes(Base):
    _tablename_ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    altura = Column(String(250), nullable=False)
    genero =  Column(String(250), nullable=False)
    peso =  Column(String(250), nullable=False)
    favoritos = relationship('Favoritos',backref='personajes', lazy=True)
    
class Planetas(Base):
    _tablename_ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    diametro = Column(String(250), nullable=False)
    periodo_orbital =  Column(String(250), nullable=False)
    poblacion =  Column(String(250), nullable=False)
    favoritos = relationship('Favoritos',backref='planetas', lazy=True)

class Favoritos(Base):
    _tablename_ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id =Column(Integer, ForeignKey('usuario.id'))
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    personajes_id = Column(Integer, ForeignKey('personajes.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')