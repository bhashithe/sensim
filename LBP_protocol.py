import time
import numpy as np
from matplotlib import pyplot
from matplotlib import animation
from Sensor import Sensor
from Target import Target

network_items = [(0,0,4), (3,0), (4,1,3), (5,3), (2,1,2), (1,3), (4,5,2)]

def from_items(items):
	sensors = []
	targets = []
	for item in items:
		if len(item)>2:
			sensors.append(Sensor(item[2], (item[0], item[1])))
		else:
			targets.append(Target(item))

	return create_network(sensors, targets)

def create_network(sensors, targets):
	for sensor in sensors:
		sensor.cover = set(sensor.reachable(targets))
	return sensors, targets

def on_rule(network):
	"""
	Will turn on or keep a sensor on if 
	that sensor is the only sensor which is
	covering a particular target

	Arguments:
		network: a tuple in the form of (sensors, targets)
	"""
	sensors, targets = network

	for sensor in sensors:
		# remove the sensor from the network if no battery left
		if sensor.battery <= 0:
			sensors.remove(sensor)
			continue

		for target in sensor.cover:
			sensors.remove(sensor)
			for ots in sensors:
				# target should be covered by an `on` sensor
				if target in ots.cover and ots.status:
					break
			else:
				sensor.on()

			sensors.append(sensor)
	return sensors, targets


def off_rule(network):
	"""
	will turn a off or keep a sensor off if there are
	other sensors taking care of the cover of this 
	sensor

	Arguments:
		network: a tuple in the form of (sensors, targets)
	"""

	sensors, targets = network
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
	return sensors, targets

def shift(network):
	network = on_rule(network)
	network = off_rule(network)

	for sensor in network[0]:
		if sensor.status:
			sensor.battery -= 1
		print(sensor)
		print(sensor.cover)

	return network
