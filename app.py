from SpaceNetwork.SpaceNetwork.classes import RelayPacket
from space_network_lib import *
from classes import Satellite, NotSatellite, transmission_attempt, RelayPacket

# Create earth
earth = NotSatellite("Earth", 0)

# Create satellites
sat1 = Satellite("Sat1", 100)
sat2 = Satellite("Sat2", 200)
sat3 = Satellite("Sat3", 300)
sat4 = Satellite("Sat4", 400)

# A message from the Earth to sat4
p_final = Packet("Hello from Earth!!!", sat3, sat4)
p_earth_to_sat3 = RelayPacket(p_final, sat2, sat3)
p_earth_to_sat2 = RelayPacket(p_earth_to_sat3, sat1, sat2)
p_earth_to_sat1 = RelayPacket(p_earth_to_sat2, earth, sat1)

try:
    transmission_attempt(p_earth_to_sat1)
except:
    print("Transmission failed")
