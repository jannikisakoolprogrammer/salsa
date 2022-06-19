import abc

class IView(abc.ABC):
	
	@abc.abstractmethod
	def run(self):
	
		pass
		
		
	@abc.abstractmethod
	def bind_events(self):
	
		pass		