import abc
from code.Base.IView import IView


class IViewMainWindow(
	IView,
	abc.ABC):
	
	@abc.abstractmethod
	def set_number_of_entries(
		self,
		_number_of_entries):
		
		pass
	
	
	@abc.abstractmethod
	def set_current(
		self,
		_current):
		
		pass
		

	@abc.abstractmethod
	def set_mistakes(
		self,
		_current):
		
		pass		
	
	
	@abc.abstractmethod
	def set_word_to_guess(
		self,
		_word_to_guess):
		
		pass
	
	
	@abc.abstractmethod
	def get_user_input(self):
	
		pass
	
	
	@abc.abstractmethod
	def set_user_input(
		self,
		_user_input):
		
		pass
	
	
	@abc.abstractmethod
	def set_hint(
		self,
		_hint):
		
		pass
	
	
	@abc.abstractmethod
	def disable_hint_button(self):
	
		pass
		
	
	@abc.abstractmethod	
	def tk_button_check_clicked(
		self,
		_event):
		
		pass
	
	
	@abc.abstractmethod
	def tk_button_hint_clicked(
		self,
		_event = None):
	
		pass
	
	
	@abc.abstractmethod
	def tk_button_letter_clicked(
		self,
		_event):
		
		pass
	
	
	@abc.abstractmethod
	def entry_user_input_get_cursor_index(self):
	
		pass
		
		
	@abc.abstractmethod
	def entry_user_input_set_cursor_index(
		self,
		_index):
		
		pass
		
		
	@abc.abstractmethod
	def reset_user_input(self):
	
		pass
	
	
	@abc.abstractmethod
	def entry_user_input_set_focus(
		self):
		
		pass