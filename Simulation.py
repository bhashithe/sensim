from Sensor import Sensor
from Target import Target
from LBPProtocol import LBPProtocol
import time
from matplotlib import pyplot as plt
from matplotlib import lines as mlines

network_items = [(0,0,4),(3,3,2),(4,1,3),(1,3),(3,0), (5,3)] 

test_protocol = LBPProtocol(network_items)

def simulate(protocol, graphs=True):
    if graphs:
        fig = plt.figure()
        axis = fig.add_subplot(1,1,1)
        fig.show()

    network = protocol.network

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
        time.sleep(2)

    if graphs:
        plt.show()

if __name__ == '__main__':
    simulate(test_protocol)
