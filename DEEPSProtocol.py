from Protocol import Protocol
import time
from matplotlib import pyplot as plt

class DEEPSProtocol(Protocol):
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

	def off_rul(self):
		"""
		if not in charge of other targets which are already covered then turn off
		"""
		pass
