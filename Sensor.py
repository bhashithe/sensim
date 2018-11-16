class Sensor():
	
	def __init__(self, battery, pos, range=3, status=0):
		self.battery = battery
		self.pos = pos
		self.range = range
		self.status = status
		self.cover = set()

	def shufle(self):
		"""
			change the covering set of the sensor
		"""
		pass

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

	def toggle(self):
		"""
		toggles the status of the sensor
		"""
		self.status = not self.status

	def add_to_cover(self, item):
		"""
		add an item to the sensor cover
		Arguments:
			item: item to add to the set, if already added ignored
		"""

		self.cover.add(item)

	def remove_from_cover(self, item):
		"""
		remove an item to the sensor cover
		Arguments:
			item: item to remove from the set, if not in the set ignored
		"""
		
		try:
			self.cover.remove(item)
		except KeyError:
			pass

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
