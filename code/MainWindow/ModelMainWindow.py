from code.Base.Model import Model

import random
import os.path


class ModelMainWindow(Model):
	def __init__(
		self,
		_database):
		super(
			ModelMainWindow,
			self).__init__(_database)
			
		self.filename = ""	

		self.n_cur_entry = 0
		self.n_len_entries = 0
		
		self.correct_guesses = 0
		self.incorrect_guesses = 0
		
		self.n_printable_chars = 0		
		self.hint_word = None
		self.n_hints = 0
		self.cur_hint = 0
		
		self.n_mistakes = 0
		
		self._printable_chars_positions = []	
			
	
	def validate_file(self,
		_filename):
		"""Validates the file _filename.
		"""
		
		# TODO:  Implement logic.
		
		return True
	
	
	def set_filename(self,
		_filename):
		
		self.filename = _filename
	
	
	def load_vocabulary(self):
		
		self.f = open(
			self.filename,
			encoding = "utf-8")
		
		self.entries = self.f.readlines()
		random.shuffle(self.entries)
		
		self.n_cur_entry = -1
		self.n_len_entries = len(self.entries)
		
		self.correct_guesses = 0
		self.incorrect_guesses = 0
		
		self.n_printable_chars = 0		
		self.hint_word = None
		self.n_hints = 0
		self.cur_hint = 0
		
		self.n_mistakes = 0
		
		self._printable_chars_positions = []
	
	
	def increase_cur_entry(self):
	
		self.n_cur_entry += 1
	
	
	def check_show_results_dialog(self):
		
		if self.n_cur_entry >= self.n_len_entries:
			return True
		else:
			return False

	
	def next_word_pair(self):
	
		if self.n_cur_entry >= self.n_len_entries:
			self.n_cur_entry = 0
			
			self.n_mistakes = 0
			
			# Randomize again
			random.shuffle(self.entries)
		
		chosen_entry = self.entries[self.n_cur_entry]
		
		self.source_word = chosen_entry.split("|")[1].strip()
		self.target_word = chosen_entry.split("|")[0].strip()
		
		self.prepare_hint()
	
	
	def prepare_hint(self):
	
		self.n_printable_chars = 0
		self._printable_chars_positions = []
		cur_pos = 0
		for c in self.target_word:
			if c.isprintable():
				self.n_printable_chars += 1
				self._printable_chars_positions.append(
					cur_pos)
			cur_pos += 1
		

		self.hint_word = ""
		for c in self.target_word:
			if c.isspace():
				self.hint_word += " "
			else:
				self.hint_word += "*"
		
		self.n_hints = self.n_printable_chars + 1 # 1 is show masked word.
		self.cur_hint = 0
	
	
	def reveal_char(self):
		pop_index = random.choice(
			self._printable_chars_positions)

		self._printable_chars_positions.remove(pop_index)
		
		self.hint_word = self.hint_word[:pop_index] + \
			self.target_word[pop_index] + \
			self.hint_word[pop_index + 1:]
	
	
	def get_cur_hint(self):
	
		return self.cur_hint
	
	
	def increment_cur_hint(self):
		
		self.cur_hint += 1
	
	
	def get_n_hints(self):
	
		return self.n_hints
	
	
	def get_hint_word(self):
	
		return self.hint_word
	
	
	def get_n_printable_chars(self):
		
		return self.n_printable_chars
	
	
	def get_number_of_entries(self):
		
		return self.n_len_entries
	
	
	def increment_correct_guesses(self):
		
		self.correct_guesses += 1
	
	
	def increment_incorrect_guesses(self):
		
		self.incorrect_guesses += 1
	
	
	def get_correct_guesses(self):
	
		return self.correct_guesses
	
	
	def get_incorrect_guesses(self):
		
		return self.incorrect_guesses
	
	
	def get_current_word_counter(self):
	
		return self.n_cur_entry
	
	
	def increase_mistakes_counter(self):
	
		self.n_mistakes += 1
		
	def get_mistakes_made(self):
	
		return self.n_mistakes
		
