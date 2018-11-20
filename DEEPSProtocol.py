from Protocol import Protocol
import time
from matplotlib import pyplot as plt

class DEEPSProtocol(Protocol):
	def __init__(self, items):
		super(DEEPSProtocol, self).__init__(items)

	def on_rule(self):
		"""
		Will turn on or keep a sensor on if 
		that sensor is the only sensor which is
		covering a particular target
		"""
		sensors, targets = self.network
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

	def off_rule(self):
		"""
		if not in charge of any targets
		or in charge of targets which are already covered then turn off
		"""
		sensors, targets = self.network
		self.find_managers()
		for sensor in sensors:
			if len(sensor.manage) == 0:
				sensor.off()
			for target in sensor.cover:
				sensors.remove(sensor)
				for ots in sensors:
					if target in ots.cover and ots.status:
						sensor.off()
				sensors.append(sensor)

	def find_managers(self):
		"""
		find the manageres of this network
		"""
		sensors, targets = self.network
		for sensor in sensors:
			for target in sensor.cover:
				#(i)
				if target == self.find_sinks():
					ots_covering_t = []
					for ots in sensors:
						if target in ots.cover and ots.status:
							ots_covering_t.append(ots) #appending the sensor again ?
					#all sensors covering this target, remove the richest sensors and make it the manager
					ots_covering_t.sort(key=lambda x: x.battery, reverse=True)
					manager = ots_covering_t.pop(0)
					manager.manage.add(target)
				#(ii)
				if target == self.find_hills():
					ots_covering_t = []
					for ots in sensors:
						if target in ots.cover and ots.status:
							ots_covering_t.append(ots) #appending the sensror
					ots_covering_t.sort(key=lambda x: x.battery, reverse=True)
					manager = ots_covering_t.pop(0)
					manager.manage.add(target)

	def shift(self):
		"""
		decides how to shuffle the sensors in the network
		"""
		sensors, targets = self.network
		#first remove sensors if they have 0 or less battery
		for sensor in sensors:
			if sensor.battery <= 0:
				sensors.remove(sensor)
		self.network = sensors, targets
		self.on_rule()
		self.off_rule()
		print('-'*20)
		for sensor in self.network[0]:
			if sensor.status:
				sensor.battery -= 1
			print(sensor)
			print(sensor.cover)

	def find_sinks(self):
		"""
		finds the poorest targets in the cover
		"""
		sensors, targets = self.network
		for sensor in sensors:
			for target in sensor.cover:
				target.richness += sensor.battery
		cover = list(sensor.cover)
		cover.sort(key=lambda x: x.richness, reverse=True)
		return cover.pop(0)

	def find_hills(self):
		"""
		finds the richest targets in the cover
		"""
		sensors, targets = self.network
		for sensor in sensors:
			for target in sensor.cover:
				target.richness += sensor.battery
		cover = list(sensor.cover)
		cover.sort(key=lambda x: x.richness, reverse=False)
		return cover.pop(0)
