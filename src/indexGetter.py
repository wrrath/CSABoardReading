from typing import List, Dict
from src.Line import Line
class indexGetter:
    def __init__(self, line: Line) -> None:
        self.line: Line = line
        self.index: int = self.line.maxValue().get("Index")
        self.max: int = self.line.maxValue().get("Value")
    def determineRow(self) -> int:
        row: int = -1
        if (self.index == 8 or self.index == 24):
            row = 1
        elif(self.index == 0 or self.index == 16):
            row = 2
        elif(self.index == 2 or self.index == 18):
            row = 3
        elif(self.index == 10 or self.index == 26):
            row = 4
        elif(self.index == 4 or self.index == 20):
            row = 5
        elif(self.index == 12 or self.index == 28):
            row = 6
        elif(self.index == 14 or self.index == 30):
            row = 7
        elif(self.index == 6 or self.index ==22):
            row = 8
        return row
    def determineColumn(self):
        column: int = -1
        if(self.index <= 14):
            column = 1
        elif(self.index > 14):
            column = 2
        return column