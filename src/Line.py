import copy
from typing import List, Dict
class Line:
    def __init__(self, values:List[int]) -> None:
        self.values: List[int] = values
        
    def printValues(self) -> None:
        print(*self.values, sep = ", ")
        
    def cleanValues(self) -> None:
        cleanValues:list = []
        for value in self.values:
            value = int(value)
            if (value >= 200):
                value = 0
            cleanValues.append(value)
        self.values = cleanValues

    def clear(self) -> None:
        self.values = []

    def dataLine(self) -> bool:
        for value in self.values:
            if (int(value) < 200 and int(value) > 4 and len(self.values) == 32):
                return True
        return False
    def maxValue(self) -> dict:
        maxValue: int = 0
        indexValue: int = 0
        for count, value in enumerate(self.values):
            if (int(value) > maxValue):
                maxValue = int(value)
                indexValue = count
        output = {"Index": indexValue, "Value": maxValue}
        return output
        