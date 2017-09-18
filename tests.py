from socialCalendarMinimal import *
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)
from sqlalchemy.orm import sessionmaker
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

frank = Person(name='Frank')
session.add(frank)
session.commit()

terminalMenu = Updater(name="terminal terminalMenu")
session.add(terminalMenu)
session.commit()

franksAddress=Addresses(person=frank, updater=terminalMenu, handle="Frank's face")
session.add(franksAddress)
session.commit()

frank.addresses
terminalMenu.addresses

kino = Encounter(person=frank, updater=terminalMenu, startTime=datetime.now(), brief="cinema")
session.add(kino)
session.commit()

frank.encounters

markt=Encounter(person=frank, updater=terminalMenu, startTime=datetime.now(), notes="some text")
session.add(markt)
session.commit()

frank.encounters
franksBirthday=ImportantDates(person=frank, startDate=datetime.now(), brief="Birthday")
session.add(franksBirthday)
session.commit()
frank.dates
markt.person.dates
frank.urgency
