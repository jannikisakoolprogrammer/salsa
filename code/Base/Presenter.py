import tkinter


class Presenter(object):

	def __init__(self,
		_model,
		_parent_presenter = None):
		
		self.view = None
		self.model = _model
		self.parent_presenter = _parent_presenter
	
	
	def view_update_controls(self):
		pass