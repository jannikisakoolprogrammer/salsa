import sqlite3
import datetime

from code.Base import database_settings

class Database(object):
	
	def __init__(self):
	
		# A tárgy az adatbázis kapcsolatnak.
		self.connection = None
		
		# A tárgy a cursornak.
		self.cursor = None
		
		# Itt, az adatbázist és a táblázatot előállítom.
		self.connection = sqlite3.connect(database_settings.DATABASE_FILEPATH)		
		self.init_table_language_mapping()
		self.init_table_word_mapping()
		
		self.cursor = self.connection.cursor()
		
		
	def init_table_language_mapping(self):
		self.connection.execute(database_settings.TABLE_LANGUAGE_MAPPING_CREATE)
	
	
	def init_table_word_mapping(self):
		self.connection.execute(database_settings.TABLE_WORD_MAPPING_CREATE)
		
	
	def default_system_settings_exist(self):
		self.cursor.execute("SELECT * FROM %s" % (database_settings.TABLE_SYSTEM_SETTINGS))		
		return self.cursor.fetchone()