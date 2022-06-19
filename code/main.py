import tkinter
import tkinter.ttk


from code.Base.Database import Database

from code.MainWindow.PresenterMainWindow import PresenterMainWindow
from code.MainWindow.ViewMainWindow import ViewMainWindow
from code.MainWindow.ModelMainWindow import ModelMainWindow



def main():

	model_main_window = ModelMainWindow(Database());	
	presenter_main_window = PresenterMainWindow(model_main_window)
	view_main_window = ViewMainWindow(presenter_main_window);
	
	view_main_window.run()