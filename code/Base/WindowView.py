import tkinter
import tkinter.ttk


class WindowView(tkinter.Toplevel):
	def __init__(
		self,
		_parent,
		_title = None,
		_geometry_manager = "pack"):
		
		super(
			WindowView,
			self).__init__(_parent)
			
		self.parent = _parent
		
		self.title(_title)
		
		self.geometry_manager = _geometry_manager
		
		self.body = tkinter.Frame(self)
		self.setup_body()
		
		if self.geometry_manager == "pack":
			self.body.pack()
		else:
			self.body.grid()
		
		self.grab_set()
		
		self.set_geometry()
	
	
	def setup_body(self):
	
		pass
	
	
	def set_geometry(self):
	
		self.geometry("300x300")
		
		
		