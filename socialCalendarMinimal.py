#!/usr/bin/python

import os
import sys

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.types import Text, DateTime, Float
from datetime import datetime


Base = declarative_base()

class Person(Base):
    __tablename__ = 'person_table'
    id = Column(Integer, primary_key=True)
    name =  Column(String(50))
    def __repr__(self):
        return "<Person(name='%s')>"  % (self.name)


class Encounter(Base):
    __tablename__ = 'encounter_table'
    id = Column(Integer, primary_key=True)
    #Who was it with?    
    personId = Column(Integer, ForeignKey('person_table.id'), nullable=False)
    person = relationship("Person", back_populates="encounters")
    #encode groups as concurrent encounters.

    brief = Column(String(150)) #a brief description for display
    notes = Column(Text) #Full notes like venues, ambiance, musings, topics of conversation, tags etc.
    startTime = Column(DateTime, nullable=False)
    endTime = Column(DateTime, nullable=True)
    meaningful = Column(Float) #how satisfying or fulfilling was it
    tooSoon = Column(Float) #did it feel it was too soon? we can back off the frequency
    cutShort = Column(Float) #Did it feel it was cut short? we can reduce the period of this cycle


    def __repr__(self):
        if(self.person):
            return "<Encounter(name='%s', time='%s')>" % (self.person.name, self.startTime)
        else:
            return "<Encounter(name='None', time='%s')>" % (self.startTime)

Person.encounters = relationship("Encounter", order_by=Encounter.startTime, back_populates="person")


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
#engine = create_engine('sqlite:///socialCalendar_test.db')
#engine = create_engine('sqlite:///:memory:', echo=True)

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
#Base.metadata.create_all(engine)

#frank = Person(name='Frank')