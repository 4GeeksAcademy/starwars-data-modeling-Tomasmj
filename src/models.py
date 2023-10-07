import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False) #nullable no puede estar vacio
    mass = Column(Integer, nullable=False) #nullable no puede estar vacio
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    homeworld  = Column(String(250), nullable=False)
   


    
class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False) #nullable no puede estar vacio
    diameter = Column(Integer, nullable=False) #nullable no puede estar vacio
    gravity = Column(Integer, nullable=False) #nullable no puede estar vacio
    oribital_period = Column(Integer, nullable=False) #nullable no puede estar vacio
    population = Column(Integer, nullable=False) 
    terrain = Column(String(250), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id')) # nombre de la tabla
    character = relationship(Character) #nombre de la clase
    
    

class Starship(Base):
    __tablename__ = 'starship'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    manufacturer = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    passenger = Column(Integer, nullable=False)
    character_id = Column(Integer, ForeignKey('character.id')) # nombre de la tabla
    character = relationship(Character) #nombre de la clase
    




class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id')) # nombre de la tabla
    character = relationship(Character) #nombre de la clase
    planet_id = Column(Integer, ForeignKey('planet.id')) # nombre de la tabla
    planet = relationship(Planet) #nombre de la clase
    starship_id = Column(Integer, ForeignKey('starship.id')) # nombre de la tabla
    starship = relationship(Starship) #nombre de la clase
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
