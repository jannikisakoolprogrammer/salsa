import tkinter
from tkinter import messagebox

from code.Base.Presenter import Presenter


class PresenterDialog(Presenter):
	def __init__(
		self,
		_view,
		_model,
		_parent_presenter,
		_title = None):
		
		super(
			PresenterDialog,
			self).__init__(
				_model,
				_parent_presenter)
				
		self.view = _view
		
		# Előállítom az eventhandlereket.
		# Oké
		self.view.button_ok.bind(
			"<Button-1>",
			self.ok_clicked)
		
		# Megszakít
		self.view.button_cancel.bind(
			"<Button-1>",
			self.cancel_clicked)
		
		self.error_message = ""
				
		self.return_value = None
		self.received_return_value = None
		
		self.populate()		
		
		
	def populate(self):
		pass		
		
	
	def run(self):
		self.view.wait_window(self.view)

	
	def ok_clicked(
		self,
		_event = None):
		
		self.get_input()		
		self.prepare_input()
		
		if ((self.validate_input() == True)
		and (self.check_apply() == True)
		and (self.apply() == True)):
			self.view.withdraw()
			self.cancel_clicked()	
			
			self.set_return_value(True)
			
		else:
			tkinter.messagebox.showerror(
				"Error",
				self.error_message,				
				parent = self.view)
				
			self.set_return_value(False)
		
	
	def get_input(self):
		pass
	
	
	def prepare_input(self):
		pass
	
	
	def validate_input(self):
		return Trueö
	
	
	def check_apply(self):
		return True # Override this for db interactions.
	
	
	def apply(self):
		return True # Override this for db interactions.
	
	
	def cancel_clicked(
		self,
		_event = None):
		self.view.parent.focus_set()
		self.view.destroy()
		
		self.set_return_value(False)
		
	
	def set_return_value(
		self,
		_return_value):
		
		self.return_value = _return_value
	
	
	def get_return_value(self):
		
		return self.return_value