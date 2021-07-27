from errors import *
import inspect


class ConsoleWidget():
	def __init__(self, title: str = "", subtitle: str = "",
		body: str = ""):
		self.title = title
		self.subtitle = subtitle
		self.body = body
		
		for attribute, value in self.get_attributes():
			if not type(value) is str:
				raise ParameterTypeError(value, attribute)

		self.title = self.title.upper()
		self.subtitle = self.subtitle.title()


	def show(self):
		for attribute in [self.title, self.subtitle, self.body]:
			if attribute:
				print(attribute)
				print()


	def get_attributes(self):
		### This code is courtesy of Matt Luongo from StackOverflow
		### https://stackoverflow.com/questions/9058305/getting-attributes-of-a-class

		attributes = inspect.getmembers(self, lambda a:not(inspect.isroutine(a)))
		return [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]


class ConsoleBox(ConsoleWidget):
	def __init__(self, title: str = "", subtitle: str = "", body: str = "", box_symbols: str = "-", horizontal_margin: int = 0, vertical_margin: int = 0):
		super(ConsoleBox, self).__init__()
		self.title = title
		self.subtitle = subtitle
		self.body = body
		self.box_symbols = box_symbols
		self.horizontal_margin = horizontal_margin
		self.vertical_margin = vertical_margin

		self.width = max(map(len, [self.title, self.subtitle, self.body])) + 2 * self.horizontal_margin
		self.horizontal_border = self.box_symbols * self.width


	def show(self):
		## for i in range(self.border_width):
		print(self.horizontal_border)

		for attribute in [self.title, self.subtitle, self.body]:
			if attribute:
				print(attribute)
				print(self.horizontal_border)


class Box():
	def __init__(self, hoerizontal_symbol, vertical_symbol, corners):
		super(Box, self).__init__()
		self.hoerizontal_symbol = hoerizontal_symbol
		self.vertical_symbol = vertical_symbol
		self.corners = corners
		