# sensim

This is a sensor network simulation framework written in python. This can be used to simulate different protocols on a user defined network of sensors and targets.

## To simulate the protocols

### Creating a protocol

Create a class, following name convention. If the protocol abbreviation is DEEPS then create a file with `DEEPSProtocol.py` and give the class name as `DEEPSProtocol` extending `Protocol` class given here with. Sample implementation is given at the file LBPProtocol. Three abstract functions should be implemented `on_rule`, `off_rule` and `shift`. These will control how the sensors are turned on and off and `shift` will control one schedule instance of turning on and off the sensors.

### Testing a protocol

`Simulation` is now a class. To test a simulation, you can instantiate it and then pass the protocol to it. You also can generate a random network using this class.

``` python
from Simulation import Simulation
from MTLBProtocol import MTLBProtocol

sim = Simulation()
network_items = sim.generate_network(4,7, max_battery = 5)
mtlbp = MTLBProtocol(network_items)

times, coverings = sim.simulate(mtlbp, graphs=True)
```


### Important notes

- These scripts assume that all sensors are initially being turned on and then put through the protocol.
- All the items in the network are placed in the rectilinear space to make the calculations easier

## Protocols which are implemented

- [Load Balancing Protocol](https://grid.cs.gsu.edu/~cscazz/postscript/sawn06deeps.pdf), p3
- [DEEPS](https://grid.cs.gsu.edu/~cscazz/postscript/sawn06deeps.pdf), p4
- Moving Target Load Balancing Protocol (MTLBP)

# TODO
- [x] Generalize adding protocols
- [x] Add animating `pyplot` plots to visualize
- [x] Add functionality to take simulations out of protocols
- [ ] Simulation insights plotting
