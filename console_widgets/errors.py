class ParameterTypeError(Exception):
	"""Exception raised for errors in the input parameter.

	Attributes:
		parameter -- input parameter which caused the error
		message -- explanation of the error
	"""

	def __init__(self, parameter, parameter_name, parameter_type, message="The parameter can only be of type {}!"):
		self.parameter = parameter
		self.message = message.replace("parameter", parameter_name).replace("{}", parameter_type)
		self.parameter_name = parameter_name
		super().__init__(self.message)

	def __str__(self):
		return f'{self.parameter} is of type {type(self.parameter).__name__}. -> {self.message}'


class SetError(Exception):
	"""Exception raised for errors in the type of the argument to the set method of any ConsoleWidget.

	Attributes:
		parameter -- input parameter which caused the error
	"""

	def __init__(self, parameter, message="The argument of the set method can only be of type dict!"):
		self.parameter = parameter
		self.message = message
		super().__init__(self.message)

	def __str__(self):
		return f'{self.parameter} is of type {type(self.parameter).__name__}. -> {self.message}'


class ParseError(Exception):
	"""Exception raised for errors in the type of the argument to the parse_text function.

	Attributes:
		text -- input text which caused the error
	"""

	def __init__(self, text, message="The argument of the parse_text function can only be of type str!"):
		self.text = text
		self.message = message
		super().__init__(self.message)

	def __str__(self):
		return f'{self.text} is of type {type(self.text).__name__}. -> {self.message}'