from Protocol import Protocol
import time
from matplotlib import pyplot as plt
import operator

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
				if target == self.find_sinks(sensor):
					ots_covering_t = []
					for ots in sensors:
						if target in ots.cover:
							ots_covering_t.append(ots) #appending the sensor again ?
					#all sensors covering this target, get the richest sensors and make it the manager for this target
					manager = max(ots_covering_t, key=operator.attrgetter('battery'))
					manager.manage.add(target)
				#(ii)
				if target == self.find_hills(sensor):
					ots_covering_t = []
					for ots in sensors:
						if target in ots.cover:
							ots_covering_t.append(ots) #appending the sensror
					manager = max(ots_covering_t, key=operator.attrgetter('battery'))
					manager.manage.add(target)

	def shift(self):
		"""
		decides how to shuffle the sensors in the network
		"""
		sensors, targets = self.network
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

	def find_sinks(self, sensor):
		"""
		finds the poorest targets in the cover of a given sensor
		"""
		osensors, otargets = self.network
		#forget previous richness values
		self.reset_richness()
		for target in sensor.cover:
			for osensor in osensors:
				if target in osensor.cover:
					target.richness += osensor.battery
		return min(sensor.cover, key=operator.attrgetter('richness'))

	def find_hills(self, sensor):
		"""
		finds the richest targets in the cover
		"""
		osensors, otargets = self.network
		#forget previous richness values
		self.reset_richness()
		for target in sensor.cover:
			for osensor in osensors:
				if target in osensor.cover:
					target.richness += osensor.battery
		return max(sensor.cover, key=operator.attrgetter('richness'))

	def reset_richness(self):
		"""
		resets richness for a new reshufle
		"""
		sensors, targets = self.network
		for target in targets:
			target.richness = 0
		self.network = sensors, targets
