from socialCalendarMinimal import *
engine = create_engine('sqlite+pysqlcipher:///:memory:', echo=True)
Base.metadata.create_all(engine)
frank = Person(name='Frank')
from sqlalchemy.orm import sessionmaker
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
session.add(frank)
session.commit()
kino = Encounter(person=frank, startTime=datetime.now())
session.add(kino)
session.commit()
frank.encounters
markt=Encounter(person=frank, startTime=datetime.now(), notes="some text")
session.add(markt)
session.commit()
frank.encounters
franksBirthday=ImportantDates(person=frank, startDate=datetime.now(), brief="Birthday")
session.add(franksBirthday)
session.commit()
frank.dates
markt.person.dates
frank.urgency
