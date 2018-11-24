import numpy as np

class Target():
	def __init__(self, pos):
		self.pos = pos
		self.richness = 0
	
	def __repr__(self):
		return 'Target: position {0}'.format(self.pos)

	def __str__(self):
		return 'Target: position {0}'.format(self.pos)

	def move(self, new_pos):
		"""A
		targets move to new location
		Arguments:
			new_pos: new position of the targe
		"""

		self.pos = new_pos
	
	def random(self):
		"""
		new random pos object
		"""
		return tuple((np.random.rand(), np.random.rand()))
