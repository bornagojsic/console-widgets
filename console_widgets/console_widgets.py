from errors import *
from themes import *
import inspect
from collections import OrderedDict


def write_roman(num):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([a for a in roman_num(num)])


### IDEAS
## ------------------------------------------------------------------------------------------------
## add a modify_width method which automagically modifies the width of a wigets after using the set method
## add the possibility to add a multi-line body for the widgets and other attributes
## ^ done only for the ConsoleWidget currently
## (+?) change allignment checking from COnsoleBox to another method (kinda done)
## (easy!) add Corners() class for the Box() class so that you don't need to use lists

## !!!!!!!!!!!!!!!!!
## (!!!important!!!) check the parsing of items in ConsoleList
## !!!!!!!!!!!!!!!!!

## add box and list themes


def parse_text(text):
	if type(text) is str:
		parsed_text = text.split('\n')
		return parsed_text
	raise ParseError(text)
		

class ConsoleWidget():
	def __init__(self, title: str = "", subtitle: str = "",
		body: str = "", width: int = None):
		self.title = parse_text(title.upper())
		self.subtitle = parse_text(subtitle.title())
		self.body = parse_text(body)
		

	def show(self):
		for attribute in [self.title, self.subtitle, self.body]:
			if any(attribute):
				for line in attribute:
					print(line)
				print()


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
	def __init__(self, title: str = "", subtitle: str = "", body: str = "", theme: str = "default", horizontal_margin: int = 0, vertical_margin: int = 0, allignment: str = "CENTER"):
		super(ConsoleBox, self).__init__()
		global box_themes
		self.title = parse_text(title)
		self.subtitle = parse_text(subtitle)
		self.body = parse_text(body)
		self.horizontal_margin = horizontal_margin
		self.vertical_margin = vertical_margin
		self.allignment = allignment

		self.set_theme(theme)

		self.width = max(map(len, self.title + self.subtitle + self.body)) + 2 * self.horizontal_margin


	def set_theme(self, theme):
		self.box = theme

		if not self.box in box_themes:
			self.box = "default"

		self.set(box_themes[self.box])


	def return_padding(self, padding):
		## The function returns the left and right paddings
		if self.allignment == "CENTER":
			return (" " * ((padding // 2) + (padding % 2)), " " * (padding // 2))
		if self.allignment == "LEFT":
			return ("", " " * padding)
		if self.allignment == "RIGHT":
			return (" " * padding, "")


	def show(self):
		## for i in range(self.border_width):
		print(self.upper_left + self.upper_border * self.width + self.upper_right)

		if any(self.title):
			for title_line in self.title:
				title_padding = self.width - len(title_line)
				
				(left_t_padding, right_t_padding) = self.return_padding(title_padding)

				print(self.left_border + left_t_padding + title_line + right_t_padding + self.right_border)
				print(self.left_vertical + self.horizontal_line * self.width + self.right_vertical)

		if any(self.subtitle):
			for sub_line in self.subtitle:
				subtitle_padding = self.width - len(sub_line)
				
				(left_s_padding, right_s_padding) = self.return_padding(subtitle_padding)

				print(self.left_border + left_s_padding + sub_line + right_s_padding + self.right_border)
				print(self.left_vertical + self.horizontal_line * self.width + self.right_vertical)

		if any(self.body):
			for body_line in self.body:
				body_padding = self.width - len(body_line)
				
				(left_b_padding, right_b_padding) = self.return_padding(body_padding)

				print(self.left_border + left_b_padding + body_line + right_b_padding + self.right_border)
		print(self.lower_left + self.lower_border * self.width + self.lower_right)


class ConsoleList(ConsoleWidget):
	def __init__(self, title: str = "", subtitle: str = "", items: list = [], list_type: str = "default"):
		super(ConsoleList, self).__init__()
		self.title = parse_text(title)
		self.subtitle = parse_text(subtitle)
		self.items = [parse_text(item) for item in items]

		self.list_type = list_type

		self.width = max(map(len, map(str, self.title + self.subtitle + self.items)))


	def show(self):
		print("─" * self.width)
		for attribute in [self.title, self.subtitle]:
			if attribute:
				for line in attribute:
					print(line)
				print("─" * self.width)

		for item_number, item in enumerate(self.items):
			if item:
				print(f"{item_number + 1}. {item[0]}")
				for line in item[1:]:
					print(line)
		print("─" * self.width)


class ConsoleSelection(ConsoleList):
	def __init__(self, title: str = "", subtitle: str = "", items: list = []):
		self.title = title
		self.subtitle = subtitle
		self.items = items

		self.width = max(17 + len(str(len(items))), max(map(len, map(str, [self.title, self.subtitle] + self.items))))

	def select(self):
		super(ConsoleSelection, self).show()

		selection = input(f"Select [1-{len(self.items)}]: ")
		#print("─" * self.width)

		return selection