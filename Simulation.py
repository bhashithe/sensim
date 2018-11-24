from Sensor import Sensor
from Target import Target
import time
from matplotlib import pyplot as plt
from matplotlib import lines as mlines
import numpy as np
from Sensor import Sensor
from Target import Target

class Simulation():
	def __init__(self, protocol=None, graphs=True):
		self.protocol = protocol

	def dummy(self):
		return Target((5,5))

	def generate_network(self, num_sensors, num_targets, max_battery=10):
		"""
		generate a network item list using the given numbers of sensors targets and max battery
		Arguments:
			num_sensors: number of sensors
			num_targets: number of targets
			max_battery: maximum batter of generated item list
		"""
		sensors = []
		targets = []
		for i in range(num_sensors):
			b = np.random.randint(1, max_battery)
			pos = np.random.rand(2)
			sensors.append((pos[0], pos[1], b))

		for i in range(num_targets):
			pos = np.random.rand(2)
			targets.append((pos[0], pos[1]))

		return sensors + targets

	def simulate(self, protocol, graphs=True):
		"""
		simulate a protocol
		Arguments:
			protocol: the `Protocol` object
			graphs: True/False, if needed interactive graph to be plotted

		Returns:
			t: the time of cover
			covering_targets: number of targets covered in each time
		"""
		if graphs:
			fig = plt.figure()
			axis = fig.add_subplot(1,1,1)
			fig.show()

		network = protocol.network
		#variable to keep the time
		count = 0 
		t = []
		covering_targets = []
		while len(network[0]):
			protocol.shift()
			sensors, targets = protocol.network
			sensor_x = []
			sensor_y = []
			target_x = []
			target_y = []
			for sensor in sensors:
				sensor_x.append(sensor.pos[0])
				sensor_y.append(sensor.pos[1])
			for target in targets:
				target_x.append(target.pos[0])
				target_y.append(target.pos[1])
			if graphs:
				axis.clear()
				axis.scatter(sensor_x, sensor_y, marker='s', color='green')
				axis.scatter(target_x, target_y, marker='o', color='red')
				for sensor in sensors:
					if sensor.status:
						for target in sensor.cover:
							axis.plot([sensor.pos[0], target.pos[0]], [sensor.pos[1], target.pos[1]], linewidth=1, linestyle='-')
							fig.canvas.draw()
							time.sleep(1)
			count+=1
			t.append(count)
			cover = set()
			for sensor in sensors:
				if sensor.status:
					for target in sensor.cover:
						cover.add(target)
			covering_targets.append(len(cover))
		if graphs:
			plt.show()
		return t, covering_targets
