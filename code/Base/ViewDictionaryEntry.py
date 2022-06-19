import tkinter
import tkinter.ttk


class ViewDictionaryEntry(object):
	def __init__(
		self,
		_body):
		
		self.frame = _body
		
		self.id = None
		self.word_source_language = None
		self.word_target_language = None
		self.tags = None
		
		self.tk_entry_word_source_language = tkinter.Entry(
			self.frame)
			
		self.tk_entry_word_source_language.pack(
			side = tkinter.LEFT)
			
		self.tk_entry_word_target_language = tkinter.Entry(
			self.frame)
		
		self.tk_entry_word_target_language.pack(
			side = tkinter.LEFT)
		
		self.tk_button_delete = tkinter.Button(
			self.frame,
			text = "X")
		self.tk_button_delete.pack(
			side = tkinter.LEFT)
			
			