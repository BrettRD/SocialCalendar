#Social Calendar Notes

An elemental Thing for managing encounters with people.
Because I'm terrible at getting out on my own.

Requires:
	*Fully Offline and Encrypted* oh god the privacy implications
	Concept of a person.
	Concept of an encounter.
	Details sufficient to estimate how urgent it is that another encounter happen.

Would Be Nice:
	a reference to what generated the encounter so that automatic sources can be managed.
	A transactional structure that allows multiple (offline) clients to add to the database to facilitate multiple autonomous agents




Definitions:
	Person:
		Name (String)
		Notable Dates (Epoch, Recurrence)
		Brief description
		Notes and topics of conversation
		//Name (Phonetic)
		//Name (Handle)
		//Gender (String)
		//Face recognition pattern for robots
		//RF cues
		//Voice Noise Pattern also for robots
		//Interests (can be gleaned from encounters)
		//NotableFiles
		//Platforms
		//AcquaintedWith (network Graph, link (string))


	Encounter:
		Person (Just One)
		TimeStart
		TimeEnd
		//Concurrent With (Encounters) // look up times
		InteractionQuality (Can be Negative for smalltalk)
		CutShort
		TooSoon
		Location (String array) //allows autocomplete to fill GPS and fetch names from alt sources
		Tags
		Description (Large String) (Can be a filename)



Straight up JSON has enough fidelity to deal with this, some of these lookups will flatly refuse to scale though.

Like non-rel databases, JSON would allow sharding on a multi-disk multicore.

The concept of an Encounter doesn't model long-term online conversations well. Maybe many Encounters of low quality as a brief back and forth. Would require quality to accumulate, and negative Quality with high CutShort would indicate smalltalk

Build a bunch of layers so that the DB architecture can be chosen later
Start with SQLlite, maybe migrate to MariaDB
Build an interface (Maybe like TaskWarrior)

