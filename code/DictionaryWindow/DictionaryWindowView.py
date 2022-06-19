import tkinter
import tkinter.ttk

from code.Base.WindowView import WindowView


class DictionaryWindowView(WindowView):
	def __init__(
		self,
		_parent,
		_title = None,
		_geometry_manager = "pack"):
		
		super(
			DictionaryWindowView,
			self).__init__(
				_parent,
				_title,
				_geometry_manager)
		
		self.tk_label_heading = None
		self.tk_label_heading_source_language = None
		self.tk_label_heading_target_language = None
	
	
	def setup_body(self):
	
		self.tk_label_heading = tkinter.Label(
			self.body,
			text = "Szótár",
			font = ("Font", 20))
		self.tk_label_heading.pack()				
		
		# Set up heading for language mapping.
		# Source language - left side
		self.tk_label_heading_source_language = tkinter.Label(
			self.body,
			text = "Forrás nyelv",
			font = (
				"Font",
				16))
		self.tk_label_heading_source_language.grid(
			row = 1,
			column = 0)			
		
		# Target language - right side
		self.tk_label_heading_target_language = tkinter.Label(
			self.body,
			text = "Cél nyelv",
			font = (
				"Font",
				16))
		self.tk_label_heading_target_language.grid(
			row = 1,
			column = 1)
	
	
	def set_geometry(self):
	
		self.geometry("600x600")
		
		
		