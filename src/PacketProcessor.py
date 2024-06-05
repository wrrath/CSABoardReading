from src.Line import Line, Packet
from typing import List, Dict
class PacketProcessor:
    def __init__(self, packet: Packet) -> None:
        self.packet: Packet = packet
        self.line: Line  = packet.lines[0]
        self.line1: Line = packet.lines[1]
        self.line2: Line = packet.lines[2]
        self.line3: Line = packet.lines[3]
    def findMaxValues(self) -> None:
        maxCount: int = 0
        lineIndex: List[List[int]] = [[]]
        for line in self.packet.lines:
            for value in line.values:
                if(int(value) >= 240):
                    maxCount += 1
        print(f'Values >= 240: {maxCount}')