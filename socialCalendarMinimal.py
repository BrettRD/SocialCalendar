#!/usr/bin/python
#Author: BrettRD
#
#

import os
import sys

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.types import Text, DateTime, Float, Interval
from datetime import datetime, timedelta
from sqlalchemy import desc
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method



Base = declarative_base()

# a person we intend to catch up with regularly
# this is not intended as an address book.
class Person(Base):
    __tablename__ = 'person_table'
    id = Column(Integer, primary_key=True)
    name =  Column(String(50), nullable=False) #Who
    #preferredContact = Column(Text) #particularly to specify their preferred platform
    
    interval = Column(Interval(native=True), default=timedelta(weeks=1)) #how frequently should be schedule something?
    #this value will almost never be updated by the user.  It'll be tweaked by info from the encounters


    # Urgency: this function is to be the most important and sophisticated one in the framework.
    # It should use a large chunk of the array of encounters and model various things that brains do.
    # Note how we're not taking into account past or future schedules;
    #   actions are the foundations of the past, intentions are only the map to the future.
    # Here is a trivial example.
    @hybrid_property
    def urgency(self):
        return (datetime.now() - self.encounters[0].startTime).total_seconds() / self.interval.total_seconds()
        #slides from zero immediately after an encounter, to one when it's about due, and beyond for overdue.
        #Travellers will have an interesting time defining this.
        #It might be worth allowing it to be calculated outside of this program.

    #update the interval
    # this should probably have a rate setting that can be increased shortly after travelling long distance
    # When you shake up your social life, you want the program to acknowledge the changes, not keep you in a rut.
    # if it's used as the interval directly, the urgency calculation can take advantage of the interval's historic values
    #@hybrid_property
    #def interval(self)
    #    return 

    def __repr__(self):
        return "<Person(name='%s')>"  % (self.name)



#an individual encounter
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
    cutShort = Column(Float) #Did it feel it was cut short? we can reduce the period of this cycle and try again

    def __repr__(self):
        if(self.brief):
            return "<Encounter(name='%s', time='%s', Brief='%s')>" % (self.person.name, self.startTime, self.brief)
        else:
            return "<Encounter(name='%s', time='%s')>" % (self.person.name, self.startTime)

Person.encounters = relationship("Encounter", order_by=desc(Encounter.startTime), back_populates="person")



#Dates important to people (Birthdays, aniversaries, Dinner Parties, Mars transfer windows)
#treating it as a seperate table makes it slightly easier to be alterted for upcoming
#out of scope for early work, but it can stay
class ImportantDates(Base):
    __tablename__ = 'dates_table'
    id = Column(Integer, primary_key=True)
    personId = Column(Integer, ForeignKey('person_table.id'), nullable=False)
    person = relationship("Person", back_populates="dates")
    brief = Column(String(150)) #Do you bring gifts, fireworks or drinks?
    startDate = Column(DateTime, nullable=False)

    #recurrence = Column(Interval, nullable=False)
    #this should probably be implemented as a function pattern, and a call returns the processed dates.
    #dateutil.rrule is almost certainly enough

    def __repr__(self):
        return "<Date(Important to='%s', date='%s', brief='%s')>" % (self.person.name, self.startDate, self.brief)

Person.dates = relationship("ImportantDates", order_by=ImportantDates.startDate, back_populates="person")







