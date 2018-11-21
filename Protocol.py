"""
Base class for implementing protocols
Abstract methods:
	- on_rule()
	- off_rule()
	- shift()
"""

from abc import ABC, abstractmethod
from Sensor import Sensor
from Target import Target

class Protocol(ABC):
	def __init__(self, items):
		"""
		Parameters:
			items: a list of tuples with details of the position of each item in the network
			       e.g. [(2,1,6), (4,1), ...] first element is a sensor with battery 6 and position (2,1)
						 and second item is a target with position (4,1)
			
		"""
		self.network = self.from_items(items)

	@abstractmethod
	def on_rule(self):
		"""
		defines how to turn sensors on of a network, will update network tuple
		"""
		pass

	@abstractmethod
	def off_rule(self):
		"""
		defines how a sensor is turned off, this also will update the network tuple
		"""
		pass

	@abstractmethod
	def shift(self):
			"""
			control how the shift schedules are implemented
			"""
			pass
        
	def from_items(self, items):
		"""
		creates a network with self.items initializing Sensor and Target objects
		Parameters:
			items: items list with sensor, target locations and sensor battery amounts
		"""
		sensors = []
		targets = []
		for item in items:
			if len(item)>2:
				sensors.append(Sensor(item[2], (item[0], item[1])))
			else:
				targets.append(Target(item))

		return self.create_network(sensors, targets)

	def create_network(self, sensors, targets):
		for sensor in sensors:
			sensor.on()
			sensor.cover = set(sensor.reachable(targets))
		return sensors, targets
