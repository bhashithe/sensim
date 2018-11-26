# SenSim

This is a sensor network simulation framework written in python. This can be used to simulate different protocols on a user defined network of sensors and targets.

## Environment

To handle some implementation obstacles, we had to define an environment where we constrain a 'test area'. This is because when randomly generating the sensors and targets they are generated using `numpy.random.rand()` which generates a number between [0-1]. And you have to select a range which will ultimately cover all targets. Therefore the default range of all the sensors has been set to `0.5` which solves this problem partially.

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

### Compare created protocols

You can compare two protocol objects on how they behave on their environment. This is supported by `Simulation.compare(p1,p2)`. Currently this implementation is not capable of running graphical simulations but it will give the computed outputs for times of the network cover.

``` python
from MTDEEPSProtocol import MTDEEPSProtocol
from MTLBProtocol import MTLBProtocol

sim = Simulation()
network_items = sim.generate_network(4,7, max_battery = 5)
p1 = MTLBProtocol(network_items)
p2 = MTDEEPSProtocol(network_items)

times, p1_coverings, p2_coverings = sim.compare(p1, p2)
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
- [x] LBP battery issue
- [ ] Range 20/15
