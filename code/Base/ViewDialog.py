import tkinter
import tkinter.ttk


class ViewDialog(tkinter.Toplevel):
	def __init__(
		self,
		_parent,
		_title = None):
		
		super(
			ViewDialog,
			self).__init__(_parent)
			
		self.parent = _parent
		
		self.title(_title)
		
		self.body = tkinter.Frame(self)
		self.setup_body()
		self.body.pack()
		
		# Oké, Megszakít
		self.buttons = tkinter.Frame(self)
		self.button_ok = None
		self.button_cancel = None
		self.create_ok_cancel_buttons()
		self.buttons.pack()
		
		self.grab_set()
		
		self.geometry("300x300")	
	
	
	def setup_body(self):
		pass
	
	
	def create_ok_cancel_buttons(self):
		
		self.button_ok = tkinter.Button(
			self.buttons,
			text = "Oké")
		self.button_ok.pack(
			side = tkinter.LEFT,
			padx = 5,
			pady = 5)

		self.button_cancel = tkinter.Button(
			self.buttons,
			text = "Megszakít")
		self.button_cancel.pack(
			side = tkinter.LEFT,
			padx = 5,
			pady = 5)
		
		
		