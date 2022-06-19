import tkinter
import tkinter.ttk
import tkinter.filedialog

from code.MainWindow import ConstantsMainWindow
from code.MainWindow.IViewMainWindow import IViewMainWindow
from constants import core
from constants import labels_en as labels


class ViewMainWindow(
	tkinter.Frame,
	IViewMainWindow):
	
	def __init__(
		self,
		_presenter):
		
		master = tkinter.Tk()
		
		super().__init__(master)
		
		# Init instance members used throughout the entire class with a default
		# value.
		self.master = None	
		
		# Frames
		self.tkinter_frame = None
		
		# Master
		self.master = master
		self.master.title(
			core.CHAR_SPACE.join((
				core.TEXT_TOOL_TITLE,
				core.TEXT_TOOL_VERSION)))
				
		self.style = tkinter.ttk.Style()
		
		# Ablakok
		self.tk_frame_create()
		
		# Pack all controls.
		#self.grid(
		#	row = 0,
		#	column = 0)
		self.pack()
		
		self.presenter = _presenter
		self.presenter.set_view(self)
		
		# Let the presenter init this view.
		# self.presenter.init_view()			
			
		self.bind_events()

	
	def tk_frame_create(self):
		self.tk_frame = tkinter.ttk.Frame(
			self)
		self.tk_frame.grid(
			row = 0,
			column = 0,
			sticky = "nsew")
			
		# Menu
		self.tk_menu = tkinter.Menu(self.master)
		
		# Filemenu
		self.tk_menu_file = tkinter.Menu(
			self.tk_menu,
			tearoff = 0)			
		self.tk_menu.add_cascade(
			label = labels.FILE,
			menu = self.tk_menu_file)
			
		# File menu options
		self.tk_menu_file.add_command(
			label = labels.OPEN,
			command = self.tk_menu_file_open_clicked)
			
		self.tk_menu_file.add_command(
			label = labels.EXIT,
			command = self.tk_menu_file_exit_clicked)
			
		self.master.config(menu = self.tk_menu)

			
			
		# Gyömbér
		self.tk_label_heading = tkinter.ttk.Label(
			self.tk_frame,
			text = core.TEXT_TOOL_TITLE,
			font = (
				core.FONT_DEFAULT,
				core.FONT_SIZE_HEADING))
		self.tk_label_heading.grid(
			row = 0,
			column = 0,
			columnspan = 9)
		
		# Subheading
		self.style.configure(
			"G.TLabel",
			foreground = "grey")
		self.tk_label_subheading = tkinter.ttk.Label(
			self.tk_frame,
			text = core.TEXT_TOOL_DESCRIPTION,
			font = (
				core.FONT_DEFAULT,
				core.FONT_SIZE_SUBHEADING),
			style = "G.TLabel")
		self.tk_label_subheading.grid(
			row = 1,
			column = 0,
			columnspan = 9,
			sticky = "n")
		
		# Show number of entries
		self.tk_label_number_of_entries = tkinter.ttk.Label(
			self.tk_frame)
		self.tk_label_number_of_entries.config(
			font = (
				core.FONT_DEFAULT,
				core.FONT_SIZE_DEFAULT))
		self.tk_label_number_of_entries.grid(
			row = 2,
			columnspan = 9,
			column = 0)
		
		# Show done entries.
		self.tk_label_current = tkinter.ttk.Label(
			self.tk_frame)
		self.tk_label_current.config(
			font = (
				core.FONT_DEFAULT,
				core.FONT_SIZE_DEFAULT))
		self.tk_label_current.grid(
			row = 3,
			columnspan = 9,
			column = 0)		
		
		# Show amount of mistakes made.
		self.tk_label_number_of_mistakes = tkinter.ttk.Label(
			self.tk_frame)
		self.tk_label_number_of_mistakes.config(
			font = (
				core.FONT_DEFAULT,
				core.FONT_SIZE_DEFAULT))
		self.tk_label_number_of_mistakes.grid(
			row = 4,
			columnspan = 9,
			column = 0)			
		
		# Word to guess
		self.tk_label_word_to_guess = tkinter.ttk.Label(
			self.tk_frame)
		self.tk_label_word_to_guess.config(
			font = (
				core.FONT_MONOSPACE,
				core.FONT_SIZE_GUESS),
			wraplength=core.WRAPLENGTH)
		self.tk_label_word_to_guess.grid(
			row = 5,
			column = 0,
			columnspan = 9)	
		
		
		# User input
		self.tk_entry_user_input = tkinter.ttk.Entry(
			self.tk_frame)
		self.tk_entry_user_input.config(
			font = (
				core.FONT_MONOSPACE,
				core.FONT_SIZE_GUESS),
			justify = core.STANDARD_JUSTIFY)
		self.tk_entry_user_input.grid(
			row = 6,
			column = 0,
			columnspan = 9,
			sticky="we")
		
		
		# Check
		self.tk_button_check = tkinter.ttk.Button(
			self.tk_frame,
			text = labels.CHECK)
		self.tk_button_check.grid(
			row = 7,
			column = 0,
			columnspan = 9,
			sticky="we")
			
					
		# Hint
		self.tk_label_hint = tkinter.ttk.Label(
			self.tk_frame)
		self.tk_label_hint.config(
			font = (
				core.FONT_MONOSPACE,
				core.FONT_SIZE_GUESS),
			anchor = tkinter.CENTER)
		self.tk_label_hint.grid(
			row = 8,
			column = 0,
			columnspan = 9,
			sticky = "we")				
	
		
		# Hint button
		self.tk_button_hint = tkinter.ttk.Button(
			self.tk_frame,
			text = labels.HINT)
		self.tk_button_hint.grid(
			row = 9,
			column = 0,
			columnspan = 9,
			sticky="we")
		
		
		# Buttons for hungarian only letters
		self.style.configure(
			"Font.TButton",
			font = (
				core.FONT_MONOSPACE,
				core.FONT_SIZE_LETTER_BUTTONS),
			width = 4)
				
		self.tk_button_1 = tkinter.ttk.Button(
			self.tk_frame,
			text = "ñ",
			style="Font.TButton")
		self.tk_button_1.grid(
			row = 10,
			column = 0,
			sticky="we")
		
		self.tk_button_2 = tkinter.ttk.Button(
			self.tk_frame,
			text = "á",
			style="Font.TButton")
		self.tk_button_2.grid(
			row = 10,
			column = 1,
			sticky="we")

		self.tk_button_3 = tkinter.ttk.Button(
			self.tk_frame,
			text = "é",
			style="Font.TButton")
		self.tk_button_3.grid(
			row = 10,
			column = 2,
			sticky="we")
		
		self.tk_button_4 = tkinter.ttk.Button(
			self.tk_frame,
			text = "í",
			style="Font.TButton")
		self.tk_button_4.grid(
			row = 10,
			column = 3,
			sticky="we")
		
		self.tk_button_5 = tkinter.ttk.Button(
			self.tk_frame,
			text = "ó",
			style="Font.TButton")
		self.tk_button_5.grid(
			row = 10,
			column = 4,
			sticky="we")	
		
		self.tk_button_6 = tkinter.ttk.Button(
			self.tk_frame,
			text = "ú",
			style="Font.TButton")
		self.tk_button_6.grid(
			row = 10,
			column = 5,
			sticky="we")
			
			
	def configure_columns(self):
	
		self.tk_frame.grid_columnconfigure(0, weight = 0)
		
		
	def configure_rows(self):	
		self.grid_rowconfigure(0, weight = 1)	
		self.grid_rowconfigure(1, weight = 2)

	
	def set_number_of_entries(
		self,
		_number_of_entries):
		
		self.tk_label_number_of_entries.config(
			text = labels.NUMBER_OF_ENTRIES % (_number_of_entries))
	
	
	def set_current(
		self,
		_current):
		
		self.tk_label_current.config(
			text = labels.ENTRIES_DONE % (_current))
	
	
	def set_mistakes(
		self,
		_mistakes):
		
		self.tk_label_number_of_mistakes.config(
			text = labels.MISTAKES % (_mistakes))
	
	
	def set_word_to_guess(
		self,
		_word_to_guess):
		
		self.tk_label_word_to_guess.config(
			text = _word_to_guess)
			
	
	def enable_hint_button(self):
	
		self.tk_button_hint.config(
			state = tkinter.NORMAL)
	
	
	def set_hint_blank(self):
	
		self.tk_label_hint.config(
			text = "")	
	
	
	def get_user_input(self):
	
		text = self.tk_entry_user_input.get()
		self.tk_entry_user_input.delete(
			0, len(text))
		return text
		
		
	def set_user_input(
		self,
		_user_input):
	
		self.tk_entry_user_input.insert(
			-1,
			_user_input)
	
	
	def set_hint(
		self,
		_hint):
		
		self.tk_label_hint.config(
			text = _hint)
	
	
	def disable_hint_button(self):
	
		self.tk_button_hint.config(
			state = tkinter.DISABLED)
		
		
	def tk_button_check_clicked(
		self,
		_event):
		
		self.presenter.check(_event)
	
	
	def tk_button_hint_clicked(
		self,
		_event = None):
	
		self.presenter.hint(_event)
	
	
	def tk_button_letter_clicked(
		self,
		_event):
		
		self.presenter.add_special_letter(_event)
		
		
	def entry_user_input_get_cursor_index(self):
	
		return self.tk_entry_user_input.index(tkinter.INSERT)
	
	
	def entry_user_input_set_cursor_index(
		self,
		_index):
		
		self.tk_entry_user_input.icursor(
			_index)
			
	def entry_user_input_set_focus(
		self):
		
		self.after(1, lambda: self.tk_entry_user_input.focus_set())
			
			
	def reset_user_input(self):
	
		self.tk_entry_user_input.delete(0, tkinter.END)
		self.tk_entry_user_input.insert(0, "")


	def tk_menu_file_open_clicked(self):
		self.presenter.file_open()
		

	def open_filedialog(self):
		self.filename = tkinter.filedialog.askopenfilename()
	
	
	def get_filename(self):
		return self.filename
	
	
	def tk_menu_file_exit_clicked(self):
		self.presenter.program_exit()
	
	
	def run(self):
	
		self.mainloop()
	
	
	def bind_events(self):
	
		self.tk_button_check.bind(
			"<Button-1>",
			self.tk_button_check_clicked)
			
		self.tk_button_hint.bind(
			"<Button-1>",
			self.tk_button_hint_clicked)
			
		self.tk_button_hint.bind(
			"<F1>",
			self.tk_button_hint_clicked)
			
		self.tk_entry_user_input.bind(
			"<Return>",
			self.tk_button_check_clicked)
			
		self.tk_entry_user_input.bind(
			"<F1>",
			self.tk_button_hint_clicked)
			
		self.bind(
			"<F1>",
			self.tk_button_hint_clicked)
			
		self.tk_button_1.bind(
			"<Button-1>",
			self.tk_button_letter_clicked)
			
		self.tk_button_2.bind(
			"<Button-1>",
			self.tk_button_letter_clicked)

		self.tk_button_3.bind(
			"<Button-1>",
			self.tk_button_letter_clicked)
			
		self.tk_button_4.bind(
			"<Button-1>",
			self.tk_button_letter_clicked)	
			
		self.tk_button_5.bind(
			"<Button-1>",
			self.tk_button_letter_clicked)
			
		self.tk_button_6.bind(
			"<Button-1>",
			self.tk_button_letter_clicked)	