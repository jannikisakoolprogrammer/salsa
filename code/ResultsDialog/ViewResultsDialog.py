import tkinter

from code.Base.ViewDialog import ViewDialog

from code.ResultsDialog import ConstantsResultsDialog as CONSTANTSRESULTSDIALOG


class ViewResultsDialog(ViewDialog):
	def __init__(
		self,
		_parent,
		_title = None):
		
		super(
			ViewResultsDialog,
			self).__init__(
				_parent,
				_title)
	
	
	def setup_body(self):
		# self.body
		
		# Válasszon egy szótárt.
		self.tk_label_choose_dictionary = tkinter.Label(
			self.body,
			text = CONSTANTSRESULTSDIALOG.CHOOSE_A_DICTIONARY)
		self.tk_label_choose_dictionary.pack()
		
		# Szótárak
		self.tk_listbox_dictionaries = tkinter.Listbox(
			self.body)
		self.tk_listbox_dictionaries.pack()	