from Protocol import Protocol
import time
from matplotlib import pyplot as plt

class LBPProtocol(Protocol):
	def __init__(self, items):
		super(LBPProtocol, self).__init__(items)

	def on_rule(self):
		"""
		Will turn on or keep a sensor on if 
		that sensor is the only sensor which is
		covering a particular target
		"""

		sensors, targets = self.network
		for sensor in sensors:
			# remove sensor if battery zeor in advance
			if sensor.battery <= 0:
				sensors.remove(sensor)
		for sensor in sensors:
			# remove the sensor from the network if no battery left
			for target in sensor.cover:
				sensors.remove(sensor)
				for ots in sensors:
					# target should be covered by an `on` sensor
					if target in ots.cover and ots.status:
						break
				else:
					sensor.on()
				sensors.append(sensor)

		self.network =  sensors, targets
		print(self.network)

	def off_rule(self):
		"""
		will turn a off or keep a sensor off if there are
		other sensors taking care of the cover of this 
		sensor
		"""

		sensors, targets = self.network
		for sensor in sensors:
			# remove sensor if battery zeor in advance
			if sensor.battery <= 0:
				sensors.remove(sensor)
		for sensor in sensors:
			os_cover = set() # targets covered by other sensors
			for target in sensor.cover:
				sensors.remove(sensor)
				for ots in sensors:
					if target in ots.cover and ots.status:
						os_cover.add(target)
				sensors.append(sensor)
			if os_cover == sensor.cover:
				sensor.off()
		self.network = sensors, targets
		print(self.network)

	def shift(self):
		"""
		decides how to shuffle the sensors in the network
		"""
		self.on_rule()
		self.off_rule()
		print('-'*20)
		for sensor in self.network[0]:
			if sensor.status:
				sensor.battery -= 1
			print(sensor)
			print(sensor.cover)
