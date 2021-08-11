from errors import *
import inspect


### IDEAS
## ------------------------------------------------------------------------------------------------
## add a modify_width method which automagically modifies the width of a wigets after using the set method
## add the possibility to add a multi-line body for the widgets and other attributes
## ^ done only for the ConsoleWidget currently
## (+?) change allignment checking from COnsoleBox to another method (kinda done)
## (easy!) add Corners() class for the Box() class so that you don't need to use lists


class Box():
	def __init__(self, type: str = "Default", horizontal_border: str = "─", vertical_border: str = "│", full_intersection: str = "┼",
			left_vertical: str = "├", right_vertical: str = "┤", upper_horizontal: str = "┬", lower_horizontal: str = "┴",
			upper_left: str = "┌", upper_right: str = "┐", lower_left: str = "└", lower_right: str = "┘"):
		super(Box, self).__init__()
		
		## borders
		self.horizontal_border = horizontal_border
		self.vertical_border = vertical_border

		## intersections
		self.full_intersection = full_intersection
		self.left_vertical = left_vertical
		self.right_vertical = right_vertical
		self.upper_horizontal = upper_horizontal
		self.lower_horizontal = lower_horizontal

		## corners
		self.upper_left = upper_left
		self.upper_right = upper_right
		self.lower_right = lower_right
		self.lower_left = lower_left
		

class ConsoleWidget():
	def __init__(self, title: str = "", subtitle: str = "",
		body: str = "", width: int = None):
		self.title = title
		self.subtitle = subtitle
		self.body = body
		
		for attribute, value in self.get_attributes():
			if not type(value) is str:
				raise ParameterTypeError(value, attribute, "string")

		self.title = self.title.upper()
		self.subtitle = self.subtitle.title()

		self.parse_attributes()


	def show(self):
		for attribute in [self.title, self.subtitle, self.body]:
			if any(attribute):
				for line in attribute:
					print(line)
				print()


	def parse_attributes(self):
		## This method parses multi-line attribtes into lists
		for attribute, value in self.get_attributes():
			if type(value) is str:
				parsed_value = value.split('\n')
				setattr(self, attribute, parsed_value)


	def set(self, attr_val: dict = {}):
		if type(attr_val) is not dict:
			raise SetError(attr_val)

		[setattr(self, attribute, value) for attribute, value in attr_val.items()]

		## ! This is a temporary solution to possibly changigng the max width when resetting an attribute

		#if type(self) is ConsoleList():
		#	self.width = max(17 + len(str(len(items))), max(map(len, map(str, [self.title, self.subtitle] + self.items))))



	def get_attributes(self):
		### This code is courtesy of Matt Luongo from StackOverflow
		### https://stackoverflow.com/questions/9058305/getting-attributes-of-a-class

		attributes = inspect.getmembers(self, lambda a:not(inspect.isroutine(a)))
		return [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]


class ConsoleBox(ConsoleWidget):
	def __init__(self, title: str = "", subtitle: str = "", body: str = "", box: Box = Box(), horizontal_margin: int = 0, vertical_margin: int = 0, allignment: str = "CENTER"):
		super(ConsoleBox, self).__init__()
		self.title = title
		self.subtitle = subtitle
		self.body = body
		self.box = box
		self.horizontal_margin = horizontal_margin
		self.vertical_margin = vertical_margin
		self.allignment = allignment

		self.parse_attributes()

		self.width = max(map(len, self.title + self.subtitle + self.body)) + 2 * self.horizontal_margin
		self.horizontal_border = self.box.horizontal_border * self.width


	def return_padding(self, padding):
		## The function returns the left and right paddings
		if self.allignment[0] == "CENTER":
			return (" " * ((padding // 2) + (padding % 2)), " " * (padding // 2))
		if self.allignment[0] == "LEFT":
			return ("", " " * padding)
		if self.allignment[0] == "RIGHT":
			return (" " * padding, "")


	def show(self):
		## for i in range(self.border_width):
		print(self.box.upper_left + self.horizontal_border + self.box.upper_right)

		if any(self.title):
			for title_line in self.title:
				title_padding = self.width - len(title_line)
				
				(left_t_padding, right_t_padding) = self.return_padding(title_padding)

				print(self.box.vertical_border + left_t_padding + title_line + right_t_padding + self.box.vertical_border)
				print(self.box.left_vertical + self.horizontal_border + self.box.right_vertical)

		if any(self.subtitle):
			for sub_line in self.subtitle:
				subtitle_padding = self.width - len(sub_line)
				
				(left_s_padding, right_s_padding) = self.return_padding(subtitle_padding)

				print(self.box.vertical_border + left_s_padding + sub_line + right_s_padding + self.box.vertical_border)
				print(self.box.left_vertical + self.horizontal_border + self.box.right_vertical)

		if any(self.body):
			for body_line in self.body:
				body_padding = self.width - len(body_line)
				
				(left_b_padding, right_b_padding) = self.return_padding(body_padding)

				print(self.box.vertical_border + left_b_padding + body_line + right_b_padding + self.box.vertical_border)
		print(self.box.lower_left + self.horizontal_border + self.box.lower_right)


class ConsoleList(ConsoleWidget):
	def __init__(self, title: str = "", subtitle: str = "", items: list = []):
		super(ConsoleList, self).__init__()
		self.title = title
		self.subtitle = subtitle
		self.items = items
		
		for attribute, value in self.get_attributes():
			if attribute != 'items' and not type(value) is str:
				raise ParameterTypeError(value, attribute, "string")

		self.width = max(map(len, map(str, self.title + self.subtitle + self.items)))


	def show(self):
		print("─" * self.width)
		for attribute in [self.title, self.subtitle]:
			if attribute:
				for lin in attribute:
					print(line)
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
		#print("─" * self.width)

		return selection