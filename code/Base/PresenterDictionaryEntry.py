import tkinter
import tkinter.ttk

from code.Base.Presenter import Presenter


class PresenterDictionaryEntry(Presenter):
	def __init__(
		self,
		_view,
		_model,
		_parent_presenter = None):
		
		super(
			PresenterDictionaryEntry,
			self).__init__(
				_view,
				_model,
				_parent_presenter)
		
		self.view.tk_entry_word_source_language.bind(
			"<Key>",
			self.model_set_word_source)
			
		self.view.tk_entry_word_target_language.bind(
			"<Key>",
			self.model_set_word_target)			
	
	
	def update_view(
		self,
		_event = None):
	
		self.model_get()
		self.view_set()
		
		print("update")
	
	
	def update_model(self):
		
		self.view_get()
		self.model_set()

	
	def view_set(self):
	
		pass
		
	
	
	def model_get(self):
	
		pass
	
	
	def view_get(self):
	
		pass
		
	
	def model_set(self):
	
		pass
	
	def run(self):
	
		pass # Base class functionality overridden.
	
	
	def model_set_word_source(self):
		
		self.model.word_source = self.view.tk_entry_word_source_language.get()
		self.model.save()
	
	
	def model_set_word_target(self):
		
		self.model.word_target = self.view.tk_entry_word_target_language.get()
		self.model.save()