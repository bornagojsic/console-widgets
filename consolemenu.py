class ConsoleMenu():
	def __init__(self, title="Title", subtitle="Subtitle", options=[], width=150, height=100):
		self.title = title
		self.subtitle = subtitle
		self.options = options
		self.width = width
		self.height = height
	
	def show(self):
		print(self.title)
		print(self.width)
		print(self.height)
