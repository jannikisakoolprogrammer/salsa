import tkinter

from code.Base.PresenterDialog import PresenterDialog

from code.NewDictionaryDialog import NewDictionaryDialogConstants \
as NEWDICTIONARYDIALOGCONSTANTS


class PresenterNewDictionaryDialog(PresenterDialog):	
	def __init__(
		self,
		_view,
		_model,
		_parent_presenter,
		_title = None):
		
		super(
			PresenterNewDictionaryDialog,
			self).__init__(
				_view,
				_model,
				_parent_presenter,
				_title)
	
	
	def get_input(self):
	
		self.source_language = self.view.tk_entry_source_language.get()
		self.target_language = self.view.tk_entry_target_language.get()
	
	
	def prepare_input(self):
	
		self.source_language.strip()
		self.target_language.strip()
				
				
	def validate_input(self):
		
		if (len(self.source_language) == 0):
			self.error_message = NEWDICTIONARYDIALOGCONSTANTS.SOURCE_LANGUAGE_NOT_FILLED
			return False
		
		if (len(self.target_language) == 0):
			self.error_message = NEWDICTIONARYDIALOGCONSTANTS.TARGET_LANGUAGE_NOT_FILLED
			return False
			
		return True
		
	
	def check_apply(self):
	
		found = self.model.exists(
			self.source_language,
			self.target_language)
			
		if found == True:
			self.error_message = NEWDICTIONARYDIALOGCONSTANTS.RECORD_ALREADY_EXISTS
			return False
			
		else:
			return True
	
	
	def apply(self):
		
		ret = self.model.insert(
			self.source_language,
			self.target_language)
			
		if ret == False:
			self.error_message = NEWDICTIONARYDIALOGCONSTANTS.FAILED_TO_INSERT_RECORD
		
		return ret