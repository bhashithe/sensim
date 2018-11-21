# sensim

This is a sensor network simulation framework written in python. This can be used to simulate different protocols on a user defined network of sensors and targets.

## To simulate the protocols

### Creating a protocol

Create a class, following name convention. If the protocol abbreviation is DEEPS then create a file with `DEEPSProtocol.py` and give the class name as `DEEPSProtocol` extending `Protocol` class given here with. Sample implementation is given at the file LBPProtocol. Three abstract functions should be implemented `on_rule`, `off_rule` and `shift`. These will control how the sensors are turned on and off and `shift` will control one schedule instance of turning on and off the sensors.

### Testing a protocol

You can do this with the `Simulation.py` script provided. Change the protocol object `test_protocol = LBPProtocol(network_items)` to what ever protocol from the implemented list of protocols. To initialize this protocol we have used a python list `network_items`. This list has tuples as items, if the tuple have 3 items then this is a `Sensor` with first two items being `x, y` position in the environment and then 3rd item will be the battery of the sensor. If there are only two items in this tuple this mean this is a `Target` and its position is given the two values.

Now the `simulate()` function returns a tuple where first index is the time steps the network was up. The 2nd index has the number of targets covered in respective time step

### Important notes

- These scripts assume that all sensors are initially being turned on and then put through the protocol.
- All the items in the network are placed in the rectilinear space to make the calculations easier

## Protocols which are implemented

- [Load Balancing Protocol](https://grid.cs.gsu.edu/~cscazz/postscript/sawn06deeps.pdf), p3
- [DEEPS](https://grid.cs.gsu.edu/~cscazz/postscript/sawn06deeps.pdf), p4

# TODO
- [x] Generalize adding protocols
- [x] Add animating `pyplot` plots to visualize
- [x] Add functionality to take simulations out of protocols
- [ ] Simulation insights plotting
