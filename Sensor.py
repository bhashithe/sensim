class Sensor():
	
	def __init__(self, battery, pos, range=3, status=0):
		self.battery = battery
		self.pos = pos
		self.range = range
		self.status = status
		self.cover = set()

	def __str__(self):
		return 'Sensor: battery: {0}, position: ({1}), range: {2}, status: {3}'.format(self.battery, self.pos, self.range, self.status)

	def adjust_range(self, adjustment):
		"""
		given an adjustment, changes the range of the sensor. Also the range cannot go below 0
		Arguments:
			adjustment: value to change the range, can be a postive or negative value
		"""
		temp = self.range
		if temp+adjustment>0:
			self.range += adjustment
		else:
			self.range = 0

	def distance(self, target):
		"""
		calculates the distance to a target from this sensor
		Arguments:
			target: target object

		returns:
			the distance
		"""

		return abs(self.pos[0] - target.pos[0]) + abs(self.pos[1] - target.pos[1])

	def reachable(self, target_set):
		"""
		finds the reachable targets off a list of targets
		Arguments:
			target_set: a itarable containing targets

		returns: 
			A list of reachable targets
		"""
		
		reachables = []
		for target in target_set:
			if self.distance(target) <= self.range:
				reachables.append(target)

		return reachables

	def on(self):
		"""
		change status to on
		"""
		self.status = 1
		print(self, 'turned on')

	def off(self):
		"""
		change status to off
		"""
		self.status = 0
		print(self, 'turned off')

