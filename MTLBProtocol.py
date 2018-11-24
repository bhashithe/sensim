from LBPProtocol import LBPProtocol

class MTLBProtocol(LBPProtocol):
	"""
	Moving target LBP is an extension of LBP itself. 
	"""
	def __init__(self, items):
		super(MTLBProtocol, self).__init__(items)

	def shift(self):
		"""
		Communicate the network and see whether the positions have been changed
		Meaning that, the reachable targets of a sensor(cover ultimately) can be changed
		For each shift, the cover should be recalculated
		"""
		sensors, targets = self.network
		for target in targets:
			print(target.random())
			#target.move(target.random())
		for sensor in sensors:
			sensor.cover = set(sensor.reachable(targets))
		self.network = sensors, targets

		self.off_rule()
		self.on_rule()
		print('-'*20)
		for sensor in self.network[0]:
			if sensor.status:
				sensor.battery -= 1
			print(sensor)
			print(sensor.cover)
