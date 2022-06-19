import os.path

# A fájl útvonalok.
DATABASE_DIRECTORY = "database"

# Az adatbázis neve.
DATABASE_NAME = "ginger.db"

# A fájl útvonal a adatbázishoz.
DATABASE_FILEPATH = os.path.join(
	DATABASE_DIRECTORY,
	DATABASE_NAME)	

# A táblázat a rendszeres beállításoknak.
	
# Az a táblázat a nyelveknek.
TABLE_LANGUAGE_MAPPING = "language_mapping"
TABLE_LANGUAGE_MAPPING_CREATE = """
CREATE TABLE IF NOT EXISTS %s (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	source_language TEXT,
	target_language TEXT,
	created_datetime TEXT)""" % (TABLE_LANGUAGE_MAPPING)

# Az a táblázat a szavaknak.
TABLE_WORD_MAPPING = "word_mapping"
TABLE_WORD_MAPPING_CREATE = """
CREATE TABLE IF NOT EXISTS %s (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	source_word TEXT,
	target_word TEXT,
	created_datetime TEXT,
	modified_datetime TEXT,
	language_mapping_id INTEGER,
	FOREIGN KEY(language_mapping_id) REFERENCES %s(id))""" % (
		TABLE_WORD_MAPPING,
		TABLE_LANGUAGE_MAPPING)
	

