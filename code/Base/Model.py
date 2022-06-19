class Model():
	def __init__(
		self,
		_database):
		
		self.database = _database
		
		
		# Szótár ID
		self.id_dictionary = None
	
	
	def set_active_dictionary(
		self,
		_id_dictionary):
		
		self.id_dictionary = _id_dictionary