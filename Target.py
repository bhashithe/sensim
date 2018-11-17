class Target():
	def __init__(self, pos):
		self.pos = pos

	def move(self, new_pos):
		"""
		targets move to new location
		Arguments:
			new_pos: new position of the targe
		"""

		self.pos = new_pos
