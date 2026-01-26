from space_network_lib import *
from classes import Satellite, NotSatellite, transmission_attempt, RelayPacket


earth = NotSatellite("Earth", 0)

sat1 = Satellite("Sat1", 100)
sat2 = Satellite("Sat2", 200)

p_final = Packet("Hello from Earth!!", sat1, sat2)
p_earth_to_sat1 = RelayPacket(p_final, earth, sat1)

try:
    transmission_attempt(p_earth_to_sat1)
except:
    print("Transmission failed")
