from space_network_lib import *
from classes import Satellite, SpaceNetwork

spaceship = SpaceNetwork(level=1)

sat1 = Satellite("Sat1", 100)
sat2 = Satellite("Sat2", 200)

message = Packet("Hi there...", sat1, sat2)

SpaceNetwork.send(spaceship, message)
