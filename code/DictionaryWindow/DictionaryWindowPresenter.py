import tkinter

from code.Base.Presenter import Presenter

from code.Base.PresenterDictionaryEntry import PresenterDictionaryEntry
from code.Base.ModelDictionaryEntry import ModelDictionaryEntry
from code.Base.ViewDictionaryEntry import ViewDictionaryEntry


class DictionaryWindowPresenter(Presenter):

	def __init__(self,
		_view,
		_model,
		_parent_presenter = None):
		
		super(
			DictionaryWindowPresenter,
			self).__init__(
				_view,
				_model,
				_parent_presenter)
				
		self.entries = []				
		self.dictionary_entries = []
		self.create_dictionary_entries()
	
	
	def create_dictionary_entries(self):
	
		# Fetch entries from database.
		for row in self.model.fetch_all_rows():
			view = ViewDictionaryEntry(self.view.body)
			model = ModelDictionaryEntry(
				self.model,
				row)
			presenter = PresenterDictionaryEntry(
				view,
				model)
			presenter.update_view()
			
			self.dictionary_entries.append(presenter)		
			
		# Always create one additional entry.
		view = ViewDictionaryEntry(self.view.body)
		model = ModelDictionaryEntry(
			self.model)
		presenter = PresenterDictionaryEntry(
			view,
			model)
		presenter.update_view()
		
		self.dictionary_entries.append(presenter)
	