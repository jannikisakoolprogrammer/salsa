import tkinter
import tkinter.ttk

from code.Base.Model import Model
from code.Base import database_settings as DATABASE_SETTINGS


class ModelDictionaryEntry(Model):


	def __init__(
		self,
		_database,
		_row = None):
		
		super(
			ModelDictionaryEntry,
			self).__init__(
				_database)
		
		self.row = _row
		
		self.word_source = None
		self.word_target = None
		
	
	
	def save(self):
	
	#	ret = self.insert_validate_input(
	#		_source_language,
	#		_target_language)
		
	#	if ret == False:
	#		return ret
			
		dt_isoformat = datetime.datetime.now().isoformat()			
			
		self.database.cursor.execute(
			"""
			INSERT INTO '%s' (
				source_word,
				target_word,
				created_datetime,
				modified_datetime,
				)
			VALUES (
				'%s',
				'%s',
				'%s',
				'%s',
				'%s')
			""" % (
				DATABASE_SETTINGS.TABLE_WORD_MAPPING,
				self.word_source,
				self.word_target,
				dt_isoformat,
				dt_isoformat,
				self.id_dictionary))
		
		self.database.connection.commit()	
		
		return True