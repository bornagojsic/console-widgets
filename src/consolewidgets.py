from errors import *
import inspect


class Box():
	def __init__(self, horizontal_symbol: str = "─", vertical_symbol: str = "│", corners: list = ["┌", "┐", "└", "┘"]):
		super(Box, self).__init__()
		self.horizontal_symbol = horizontal_symbol
		self.vertical_symbol = vertical_symbol
		self.corners = corners
		

class ConsoleWidget():
	def __init__(self, title: str = "", subtitle: str = "",
		body: str = ""):
		self.title = title
		self.subtitle = subtitle
		self.body = body
		
		for attribute, value in self.get_attributes():
			if not type(value) is str:
				raise ParameterTypeError(value, attribute, "string")

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
	def __init__(self, title: str = "", subtitle: str = "", body: str = "", box: Box = Box(), horizontal_margin: int = 0, vertical_margin: int = 0):
		super(ConsoleBox, self).__init__()
		self.title = title
		self.subtitle = subtitle
		self.body = body
		self.box = box
		self.horizontal_margin = horizontal_margin
		self.vertical_margin = vertical_margin

		self.width = max(map(len, [self.title, self.subtitle, self.body])) + 2 * self.horizontal_margin
		self.horizontal_border = self.box.horizontal_symbol * self.width


	def show(self):
		## for i in range(self.border_width):
		print(self.box.corners[0] + self.horizontal_border + self.box.corners[1])

		if self.title:
			title_padding = self.width - len(self.title)
			left_t_padding = " " * ((title_padding // 2) + (title_padding % 2))
			right_t_padding = " " * (title_padding // 2)
			print(self.box.vertical_symbol + left_t_padding + self.title + right_t_padding + self.box.vertical_symbol)
			print("├" + self.horizontal_border + "┤")

		if self.subtitle:
			subtitle_padding = self.width - len(self.subtitle)
			left_s_padding = " " * ((subtitle_padding // 2) + (subtitle_padding % 2))
			right_s_padding = " " * (subtitle_padding // 2)
			print(self.box.vertical_symbol + left_s_padding + self.subtitle + right_s_padding + self.box.vertical_symbol)
			print("├" + self.horizontal_border + "┤")

		if self.body:
			print(self.box.vertical_symbol + self.body + self.box.vertical_symbol)
		print(self.box.corners[2] + self.horizontal_border + self.box.corners[3])


class ConsoleList(ConsoleWidget):
	def __init__(self, title: str = "", subtitle: str = "", items: list = []):
		super(ConsoleList, self).__init__()
		self.title = title
		self.subtitle = subtitle
		self.items = items
		
		for attribute, value in self.get_attributes():
			if attribute != 'items' and not type(value) is str:
				raise ParameterTypeError(value, attribute, "string")

		self.width = max(map(len, map(str, [self.title, self.subtitle] + self.items)))


	def show(self):
		print("─" * self.width)
		for attribute in [self.title, self.subtitle]:
			if attribute:
				print(attribute)
				print("─" * self.width)

		for item_number, item in enumerate(self.items):
			print(f"{item_number + 1}. {item}")
		print("─" * self.width)


class ConsoleSelection(ConsoleList):
	def __init__(self, title: str = "", subtitle: str = "", items: list = []):
		self.title = title
		self.subtitle = subtitle
		self.items = items
		
		for attribute, value in self.get_attributes():
			if attribute != 'items' and not type(value) is str:
				raise ParameterTypeError(value, attribute, "string")

		self.width = max(17 + len(str(len(items))), max(map(len, map(str, [self.title, self.subtitle] + self.items))))

	def select(self):
		super(ConsoleSelection, self).show()

		selection = input(f"Select [1-{len(self.items)}]: ")
		print("─" * self.width)