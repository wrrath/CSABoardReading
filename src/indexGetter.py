from typing import List, Dict
from src.Line import Line
class indexGetter:
    def __init__(self, line: Line) -> None:
        self.line = line
    def oddColumn(self) -> bool:
        searchIndex = [8,0,2,10,4,12,14,6]

        for packet in self.packets:
            tempList: List[int] = packet.packetValues()
        
        return False
    def evenColumn(self) -> bool:

        return False
    def determineRow(self):
        index = self.line.maxValue().get("Index") #ssssssssssssssssssssssssssssssssssssssssssss
        print(f"Index: {index}")
    def determineColumn(self):
        return