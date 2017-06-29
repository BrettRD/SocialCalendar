# Social Calendar

An elemental Thing for managing encounters with people, Because I'm terrible at getting out on my own.

#### Requirements:
* *Fully Offline and Encrypted* oh god the privacy implications
* Concept of a person.
* Concept of an encounter.
* Details sufficient to estimate how urgent it is that another encounter happen soon.

#### Would Be Nice:
* a reference to what generated the encounter so that automatic sources can be managed.
* A transactional structure that allows multiple (offline) clients to add to the database to facilitate multiple autonomous agents (replaying other agent's transactions into the local database to synchronise)


#### Definitions:
* Person:
  * Name (String)
  * Notable Dates (Epoch, Recurrence)
  * Brief description
  * Notes and topics of conversation
  * Platforms / how to contact
  * AcquaintedWith (network Graph, link (string))


* Encounter
  * Person (Just One)
  * TimeStart
  * TimeEnd
  * Concurrent With (Encounters) Or just look up times
  * InteractionQuality (Can be Negative for smalltalk)
  * CutShort  (used to adjust the next prompt period)
  * TooSoon  (used to adjust the automatic prompt schedule)
  * Location (String array) //allows autocomplete to fill GPS and fetch names from alt sources
  * Description (Large String) (Can be a filename)



The concept of an Encounter doesn't model long-term online conversations well. Maybe many satisfying Encounters of low quality can indicate attention paid to a brief back and forth. It would require interaction-quality to accumulate.  which would suggest that negative quality values can be used to indicate smalltalk

Many of the data types used have way more fidelity than they need, this is deliberate. Human interaction is fuzzy, and measurement is hard. The majority of the data that goes into this database is intended to be qualitative only. Uncertainty bounds and un-modelled data makes splitting hairs meaningless. This isn't supposed to accurately archive or direct a perfect personal narrative, it's meant to prompt a more exciting story.

I'm using sqlAlchemy so that the result is somewhat agnostic to the underlying database.  I fully expect people to search the database content with tools written in Perl so adding flexibility with strings is a major goal.


