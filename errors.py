class TitleTypeError(Exception):
	"""Exception raised for errors in the input title.

	Attributes:
		title -- input title which caused the error
		message -- explanation of the error
	"""

	def __init__(self, title, message="Title can only be of type string!"):
		self.title = title
		self.message = message
		super().__init__(self.message)

	def __str__(self):
		return f'{self.title} -> {self.message}'
