from errors import *


class ConsoleWidget():
	def __init__(self, title: str = None, subtitle: str = None,
		body: str = None):
		self.title = title
		self.subtitle = subtitle
		self.body = body

		if not type(self.title) is string:
			raise TitleTypeError(self.title)

	
	def show(self):
		if self.title:
			print(self.title.upper())
			print()

		if self.subtitle:
			print(self.subtitle.title())
			print()

		if self.body:
			print(self.body)
			print()


class ConsoleBox(ConsoleWidget):
	def __init__(self, title, subtitle, body, box_symbol, horizontal_margin, vertical_margin):
		super(ConsoleBox, self).__init__()
		self.title = title
		self.subtitle = subtitle
		self.body = body
		self.box_symbol = box_symbol
		self.horizontal_margin = horizontal_margin
		self.vertical_margin = vertical_margin
		