from socialCalendarMinimal import *
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)
from sqlalchemy.orm import sessionmaker
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# enter some people

jenny = Person(name='Jenny')
session.add(jenny)
session.commit()

suzan = Person(name='Suzan')
session.add(suzan)
session.commit

frank = Person(name='Frank')
session.add(frank)
session.commit()

boris = Person(name='Boris')
session.add(frank)
session.commit()

# create some updaters

terminalMenu = Updater(name="terminalMenu")
session.add(terminalMenu)
session.commit()

otherUpdater = Updater(name = "otherthing")
session.add(otherUpdater)
session.commit

# associate the people with updaters

jennysAddress=Addresses(person=jenny, updater=otherUpdater, handle="")
session.add(jennysAddress)
session.commit()

franksAddress=Addresses(person=frank, updater=terminalMenu, handle="Frank's face")
session.add(franksAddress)
session.commit()

borissAddress=Addresses(person=boris, updater=terminalMenu, handle="")
session.add(borissAddress)
session.commit()

borissOtherAddress = Addresses(person=boris, updater=otherUpdater, handle=""
session.add(borissOtherAddress)
session.commit()

# try some simple relation dereferences

frank.addresses
terminalMenu.addresses

#add some encounters

kino = Encounter(person=frank, updater=terminalMenu, startTime=datetime.now(), brief="cinema")
session.add(kino)
session.commit()

markt=Encounter(person=frank, updater=terminalMenu, startTime=datetime.now(), notes="some text")
session.add(markt)
session.commit()

frank.encounters


franksBirthday=ImportantDates(person=frank, startDate=datetime.now(), brief="Birthday")
session.add(franksBirthday)
session.commit()

frank.dates
markt.person.dates

# try the Person hybrid attribute
frank.urgency


# try some queries

# people with terminalMenu as an updater
session.query(Person).filter(Person.addresses.any(Addresses.updater == terminalMenu))
# people without terminalMenu as an updater
session.query(Person).filter(~Person.addresses.any(Addresses.updater == terminalMenu))

