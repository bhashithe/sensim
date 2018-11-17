# sensim

This is a sensor network simulation framework written in python. This can be used to simulate different protocols on a user defined network of sensors and targets.

### To simulate the protocols

``` python
network = shift(network)
```

Here `network` is a `set` created by preferably `from_items()` function which will create a set of sensors and targets using a list as following

``` python
network_items = [(0,0,4), (3,0), (4,1,3), (5,3), (2,1,2), (1,3), (4,5,2)]
```

### Important notes

These scripts assume that all sensors are initially being turned on and then put through the protocol.

# TODO
- [ ] Generalize adding protocols
- [x] Add animating `pyplot` plots to visualize
