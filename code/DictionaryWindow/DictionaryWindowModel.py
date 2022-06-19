from code.Base.Model import Model

from code.Base import database_settings as DATABASE_SETTINGS

class DictionaryWindowModel(Model):
	def __init__(
		self,
		_database):	
		
		super(
			DictionaryWindowModel,
			self).__init__(
				_database)
	
	
	def fetch_all_rows(self):
		
		self.database.cursor.execute(
			"""
			SELECT * FROM '%s'
				WHERE language_mapping_id = '%s'
			""" % (
				DATABASE_SETTINGS.TABLE_WORD_MAPPING,
				self.id_dictionary))
		
		rows = self.database.cursor.fetchall()
		
		return rows