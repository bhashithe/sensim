import numpy as np
from collections import namedtuple
from matplotlib import pyplot
from matplotlib import animation
import time

# configurations
rectilinear_plane = 0, 50
num_sensors = 4
num_targets = 10

Position = namedtuple('Position',['x','y'])
sensor_pos = [Position(np.random.randint(low=rectilinear_plane[0], high=rectilinear_plane[1], size=2)) for i in range(num_sensors)]
target_pos = [Position(np.random.randint(low=rectilinear_plane[0], high=rectilinear_plane[1], size=2)) for i in range(num_targets)]


