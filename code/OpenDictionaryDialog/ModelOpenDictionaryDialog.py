import tkinter

import datetime

from code.Base.Model import Model
from code.Base import database_settings as DATABASE_SETTINGS

class ModelOpenDictionaryDialog(Model):
	def __init__(
		self,
		_database):
		super(
			ModelOpenDictionaryDialog,
			self).__init__(_database)
	
	
	def fetch_all(self):
	
		self.database.cursor.execute(
			"""
			SELECT * FROM '%s'
			""" % (
				DATABASE_SETTINGS.TABLE_LANGUAGE_MAPPING))
		
		return self.database.cursor.fetchall()