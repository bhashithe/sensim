from DEEPSProtocol import DEEPSProtocol
import time
from matplotlib import pyplot as plt
import operator

class MTDEEPSProtocol(DEEPSProtocol):
	def __init__(self, items):
		super(MTDEEPSProtocol, self).__init__(items)

	def shift(self):
		"""
		decides how to shuffle the sensors in the network
		"""
		sensors, targets = self.network
		for target in targets:
			target.move(target.random())
		#find reachable again, since targets are moving now
		for sensor in sensors:
			sensor.cover = set(sensor.reachable(targets))
		#find the managers of all sensors
		self.find_managers()
		#first remove sensors if they have 0 or less battery
		for sensor in sensors:
			if sensor.battery <= 0:
				sensors.remove(sensor)
		self.network = sensors, targets
		self.off_rule()
		self.on_rule()
		print('-'*30)
		for sensor in self.network[0]:
			if sensor.status:
				sensor.battery -= 1
			print(sensor)
			print(sensor.cover)

