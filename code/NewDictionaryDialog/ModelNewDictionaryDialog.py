import tkinter

import datetime

from code.Base.Model import Model
from code.Base import database_settings as DATABASE_SETTINGS

class ModelNewDictionaryDialog(Model):
	def __init__(
		self,
		_database):
		super(
			ModelNewDictionaryDialog,
			self).__init__(_database)
	
	
	def exists(
		self,
		_source_language,
		_target_language):
		
		ret = self.exists_validate_input(
			_source_language,
			_target_language)
		
		if ret == False:
			return ret
			
		self.database.cursor.execute(
			"""
			SELECT * FROM '%s'
				WHERE source_language = '%s'
				  AND target_language = '%s'
			""" % (
				DATABASE_SETTINGS.TABLE_LANGUAGE_MAPPING,
				_source_language,
				_target_language))
		
		row = self.database.cursor.fetchone()
		
		if row == None:
			return False
		else:
			return True
	
	
	def exists_validate_input(
		self,
		_source_language,
		_target_language):
		
		if len(_source_language) == 0:
			return False
		
		if len(_target_language) == 0:
			return False
		
		return True

	
	def insert(
		self,
		_source_language,
		_target_language):
		
		ret = self.insert_validate_input(
			_source_language,
			_target_language)
		
		if ret == False:
			return ret
			
		dt_isoformat = datetime.datetime.now().isoformat()			
			
		self.database.cursor.execute(
			"""
			INSERT INTO '%s' (
				source_language,
				target_language,
				created_datetime)
			VALUES (
				'%s',
				'%s',
				'%s')
			""" % (
				DATABASE_SETTINGS.TABLE_LANGUAGE_MAPPING,
				_source_language,
				_target_language,
				dt_isoformat))
		
		self.database.connection.commit()
		
		self.set_active_dictionary(self.database.cursor.lastrowid)		
		
		return True
	
	
	def insert_validate_input(
		self,
		_source_language,
		_target_language):
		
		if len(_source_language) == 0:
			return False
		
		if len(_target_language) == 0:
			return False
			
		return True		
			
		
			
			
			