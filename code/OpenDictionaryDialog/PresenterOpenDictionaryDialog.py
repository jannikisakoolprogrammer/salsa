import tkinter

from code.Base.PresenterDialog import PresenterDialog


class PresenterOpenDictionaryDialog(PresenterDialog):	
	def __init__(
		self,
		_view,
		_model,
		_parent_presenter,
		_title = None):
		
		super(
			PresenterOpenDictionaryDialog,
			self).__init__(
				_view,
				_model,
				_parent_presenter,
				_title)
		
		self.id_dictionary_chosen = None
	
	
	def populate(self):
		rows = self.model.fetch_all()
		
		# Insert into view listbox.
		self.populate_tk_listbox_dictionaries(rows)
	
	
	def populate_tk_listbox_dictionaries(
		self,
		_rows):
		
		for row in _rows:
			self.view.tk_listbox_dictionaries.insert(
				row[0],
				"%s <-> %s" % (
					row[1],
					row[2]))
					
	def get_input(self):
	
		if len(self.view.tk_listbox_dictionaries.curselection()) > 0:
			self.id_dictionary_chosen = self.view.tk_listbox_dictionaries.curselection()[0]
			
				
	
	
	def validate_input(self):
		return True
	
	
	def apply(self):
	
		ret = super()
	
		self.model.set_active_dictionary(self.id_dictionary_chosen)
		
		return True