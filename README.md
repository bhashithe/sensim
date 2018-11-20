# sensim

This is a sensor network simulation framework written in python. This can be used to simulate different protocols on a user defined network of sensors and targets.

## To simulate the protocols

### Creating a protocol

Create a class, following name convention. If the protocol abbreviation is DEEPS then create a file with `DEEPSProtocol.py` and give the class name as `DEEPSProtocol` extending `Protocol` class given here with. Sample implementation is given at the file LBPProtocol. Three abstract functions should be implemented `on_rule`, `off_rule` and `shift`. These will control how the sensors are turned on and off and `shift` will control one schedule instance of turning on and off the sensors.

For now, the simulation is also implemented at the Protocol implementation, but in future this will be moved into a separate file which should be easier for maintaining.

### Important notes

- These scripts assume that all sensors are initially being turned on and then put through the protocol.
- All the items in the network are placed in the rectilinear space to make the calculations easier

## Protocols which are implemented

- [Load Balancing Protocol](https://grid.cs.gsu.edu/~cscazz/postscript/sawn06deeps.pdf), p3
- [DEEPS](https://grid.cs.gsu.edu/~cscazz/postscript/sawn06deeps.pdf), p4

# TODO
- [x] Generalize adding protocols
- [x] Add animating `pyplot` plots to visualize
- [ ] Add functionality to take simulations out of protocols
