from space_network_lib import *
import time


class Satellite(SpaceEntity):

    def receive_signal(self, packet: Packet):
        # Chacking if it's an instance
        if isinstance(packet, RelayPacket):
            # Unwrapping the message
            inner_packet = packet.data
            print(f"[{self.name}] - Unwrapping and forwarding to {inner_packet.receiver}.")
            # Sending to the receiver
            transmission_attempt(inner_packet)
        else:
            print(f"Final destination reached: {packet.data}")


class RelayPacket(Packet):
    def __init__(self, packet_to_relay, sender, proxy):
        super().__init__(data=packet_to_relay, sender=sender, receiver=proxy)
        self.sender = sender

    def __repr__(self):
        return f"RelayPacket (Relaying [{self.data}] to {self.receiver} from {self.sender})"


class NotSatellite(SpaceEntity):
    def receive_signal(self, packet: Packet):
        pass


def transmission_attempt(packet):
    spaceship = SpaceNetwork(level=4)
    while True:
        try:
            spaceship.send(packet)
            break
        except TemporalInterferenceError:
            print("Interference, waiting two seconds...")
            print("1...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
        except DataCorruptedError:
            print("Data corrupted, retrying...")
        except LinkTerminatedError:
            print("Link lost")
            raise "BrokenConnectionError"
        except OutOfRangeError:
            print("Target out of range.")
            raise "BrokenConnectionError"