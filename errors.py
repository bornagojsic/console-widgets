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
