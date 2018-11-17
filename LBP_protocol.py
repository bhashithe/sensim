import time
import numpy as np
from matplotlib import pyplot
from matplotlib import animation
from Sensor import Sensor
from Target import Target

network_items = [(0,0,4), (3,0), (4,1,3), (5,3), (3,3,2), (1,3)]

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
	sensors, targets = network
	for sensor in sensors:
		for target in sensor.cover:
			sensors.remove(sensor)
			for ots in sensors:
				if target in ots.cover:
					break
			else:
				sensor.on()

			sensors.append(sensor)

def off_rule(network):
	sensors, targets = network
	for sensor in sensors:
		os_cover = set() # targets covered by other sensors
		for target in sensor.cover:
			sensors.remove(sensor)
			for ots in sensors:
				if target in ots.cover:
					os_cover.add(target)

			sensors.append(sensor)
		if os_cover == sensor.cover:
			sensor.off()

def shift(network):
	on_rule(network)
	off_rule(network)

	for sensor in network[0]:
		if sensor.status:
			sensor.battery -= 1
