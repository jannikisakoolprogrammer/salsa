import tkinter
import tkinter.ttk

from code.Base.Presenter import Presenter

	
from constants import labels_en as labels


from code.ResultsDialog.PresenterResultsDialog import PresenterResultsDialog
from code.ResultsDialog.ViewResultsDialog import ViewResultsDialog
from code.ResultsDialog.ModelResultsDialog import ModelResultsDialog


class PresenterMainWindow(Presenter):

	def __init__(
		self,
		_model):
		
		super(
			PresenterMainWindow,
			self).__init__(_model)	
	
	
	def set_view(
		self,
		_view):
		
		self.view = _view
	
	
	def init_view(self):
	
		# Show number of entries of words
		self.view.set_number_of_entries(
			self.model.get_number_of_entries())	
	
		# Load next word pair.
		self.load_next_word_pair()	
		
		# Show current word counter
		self.view_update_current_word_counter()
		
		# Show mistakes made.
		self.view_update_mistakes_counter()
		
		# Set word to guess in view.
		self.view.set_word_to_guess(
			self.model.source_word)
		
		# Enable hint button.
		self.view.enable_hint_button()
		
		# Make hint blank.
		self.view.set_hint_blank()


	def add_special_letter(
		self,
		_event):
		
		"""Adds special letter to the text input field where the cursor is
		located.
		"""
		
		# Get pos of cursor.
		cursor_pos = self.view.entry_user_input_get_cursor_index()
		
		# User input
		self.view.set_user_input("")
		user_input = self.view.get_user_input()
		
		# Char to add.
		char = _event.widget["text"].lower()
		
		# Build input.
		new_user_input = user_input[:cursor_pos] + char + user_input[cursor_pos:]
		
		# Set user input in view.
		self.view.set_user_input(new_user_input)

		# Increase cursor position by one.
		self.view.entry_user_input_set_cursor_index(
			cursor_pos + 1)
			
		#Give focus to the entry box again.
		self.view.entry_user_input_set_focus()
		
	
	def view_update_current_word_counter(self):
	
		self.view.set_current(self.model.get_current_word_counter())
	
	
	def view_update_mistakes_counter(self):
	
		self.view.set_mistakes(
			self.model.get_mistakes_made())

	
	def load_next_word_pair(self):
	
		self.model.increase_cur_entry()
		#if self.model.check_show_results_dialog() == True:
		
		#viewResultsDialog = ViewResultsDialog(self.view)
		#modelResultsDialog = ModelResultsDialog(self.model.database)
		#presenterResultsDialog = PresenterResultsDialog(
		#	viewResultsDialog,
		#	modelResultsDialog,
		#	self)
			
		self.model.next_word_pair()

	
	def check(self, _e = None):
	
		user_input = self.view.get_user_input()
		
		if user_input.lower() == self.model.target_word.lower():
			
			# Reset entry field.
			self.view.reset_user_input()
		
			self.load_next_word_pair()
			
			# Show current word counter
			self.view_update_current_word_counter()		
			
			# Set word to guess in view.
			self.view.set_word_to_guess(
				self.model.source_word)			
			
			# Enable hint button.
			self.view.enable_hint_button()
			
			# Make hint blank.
			self.view.set_hint_blank()
			
			# Reset mistakes counter.
			self.view_update_mistakes_counter()
		
		else:
			# Set old user input again.
			self.view.set_user_input(user_input)
			# Increase mistakes counter.
			self.model.increase_mistakes_counter()
			
			# Show the user the amount of mistakes made.
			self.view.set_mistakes(
				self.model.get_mistakes_made())
	
	
	def hint(self, _E = None):
		# Hint 1: Convert printable chars to underscores
		# Other hints:  Turn one underscore into the printable char.
		# Do this until the word is displayed.
		
		# Check if any more hints can be made:
		if self.model.get_cur_hint() >= self.model.get_n_hints():	
			# No more hints possible.
			return
		else:
			if self.model.get_cur_hint() == 0:
				# Show masked word first.
				self.view.set_hint(self.model.get_hint_word())
			else:
				# Reveal one printable char.
				self.model.reveal_char()
				self.view.set_hint(self.model.get_hint_word())
				
			self.model.increment_cur_hint()
			
			if self.model.get_cur_hint() >= self.model.get_n_hints():
			
				# Deactivate Hint button.
				self.view.disable_hint_button()
				
	
	def file_open(self):
		"""Opens a file from which to read vocabulary.
		"""
	
		self.view.open_filedialog()
		
		filename = self.view.get_filename()
		result = self.model.validate_file(filename)
		
		if result == False:
			self.view.show_error_file()
			
		else:
			self.model.set_filename(filename)
			self.model.load_vocabulary()
			self.init_view()
	
	
	def program_exit(self):
		"""Exists the program.
		"""
		
		self.view.master.destroy()