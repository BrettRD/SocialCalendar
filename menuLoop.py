#!/usr/bin/python

# an interactive menu thing to add data to the socailCalendar
# following
# http://charlesleifer.com/blog/dear-diary-an-encrypted-command-line-diary-with-python/
# 

from socialCalendarMinimal import *
from sqlalchemy.orm import sessionmaker

def menu_loop():
    choice = None
    while choice != 'q':
        for key, value in menu.items():
            print('%s) %s' % (key, value.__doc__))
        choice = raw_input('Action: ').lower().strip()
        if choice in menu:
            menu[choice]()

def search_person(query=None):
    while True:
        name = raw_input(' enter a name ').lower().strip()
        if query == None:
            query = session.query(Person)
        results = query.filter(Person.name.like(name+'%')).all()
        if len(results) == 0:
            print("no results")
            if raw_input('try again? [Yn] ') == 'n':
                return None
        elif len(results) == 1:
            print("found only one: ")
            print str(results[0])
            if raw_input('use this? [Yn] ') != 'n':
                return results[0]
        else:
            print("found more than one: ")
            for i in range(0, len(results)):
                print(str(i) + ": " + results[i].name)
            while True:
                choice = raw_input(' try again: a, choose: 0-' + str(len(results)-1) + ", abort: q, ").strip()
                if choice == 'q':
                    return None
                elif choice.isdigit():
                    if int(choice) > len(results):
                        print("out of range")
                    else:
                        return results[int(choice)]
                else:
                    break



def add_person():
    """Add a person"""
    if raw_input('search first? [Yn] ') != 'n':
        associate_person()
    else:
        name = raw_input(' enter a name ').strip()
        newPerson = Person(name=name)
        print str(newPerson)
        if raw_input('Save entry? [Yn] ') != 'n':
            session.add(newPerson)
            #then add a handle for our updater to find this person by
            newAddress = Addresses(person=newPerson, updater=terminalMenu)
            session.add(newAddress)
            session.commit()
            print('Saved successfully.')


def associate_person():
    #limit selections to people with no addresses associating them with this updater
    query = session.query(Person).filter(~Person.addresses.any(Addresses.updater == terminalMenu))
    person = search_person(query)
    if person != None:
        print str(person)
        if raw_input('Associate this person with this updater? [Yn] ') != 'n':
            newAddress = Addresses(person=person, updater=terminalMenu)
            session.add(newAddress)
            session.commit()
            print('Saved successfully.')




def add_Encounter():
    """Add an encounter"""
    print('Who with?')
    #limit selections to people associated with this updater
    query = session.query(Person).filter(Person.addresses.any(Addresses.updater == terminalMenu))
    person = search_person(query)
    if person != None:
        brief = raw_input(' what happened? ')
        newEncounter = Encounter(person=person, updater=terminalMenu, startTime=datetime.now(), brief=brief)
        print str(newEncounter)
        if raw_input('Save entry? [Yn] ') != 'n':
            session.add(newEncounter)
            session.commit()
            print('Saved successfully.')



terminalMenu = None

menu = {
    'p' : add_person,
    'e' : add_Encounter
}

if __name__ == '__main__':

    # hook to a database
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()


    # grab this updater
    terminalMenu = session.query(Updater).filter(Updater.name == "terminalMenu").all()
    if len(terminalMenu) == 0:
        print "this seems to be the first run of this updater. Registering"
        terminalMenu = Updater(name="terminalMenu")
        session.add(terminalMenu)
        session.commit()
    elif len(terminalMenu) > 1:
        print "this updater exists in duplicate, that needs fixing."
        exit()
    else:
        terminalMenu = terminalMenu[0]

    menu_loop()