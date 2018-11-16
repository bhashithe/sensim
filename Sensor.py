class Sensor():
	
	def __init__(self, battery, pos, range=3, status=0):
		self.battery = battery
		self.pos = pos
		self.range = range
		self.status = status
		self.cover = set()

	def shufle():
		"""
			change the covering set of the sensor
		"""
		pass

	def adjust_range(adjustment):
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

	def toggle():
		"""
		toggles the status of the sensor
		"""
		self.status = not self.status

	def add_to_cover(item):
		"""
		add an item to the sensor cover
		Arguments:
			item: item to add to the set, if already added ignored
		"""

		self.cover.add(item)

	def remove_from_cover(item):
		"""
		remove an item to the sensor cover
		Arguments:
			item: item to remove from the set, if not in the set ignored
		"""
		
		try:
			self.cover.remove(item)
		except KeyError:
			pass
