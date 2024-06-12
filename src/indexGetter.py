from typing import List
from src.Line import Packet
class indexGetter:
    def __init__(self, packetValues: List[Packet]) -> None:
        self.packets = packetValues
    def oddColumn(self) -> bool:
        for packet in self.packets:
            packet.packetValues()
        return False
    def evenColumn(self) -> bool:

        return False
    def determineColumn(self):
        return