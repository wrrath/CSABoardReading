from typing import List
import math

class Square:
    def __init__(self, on) -> None:
        self.on = int(on)
        
    def setOnValue(self, on) -> None:
       self.on = on 


class BoardDisplay:
    def __init__(self, squares: List[Square]) -> None:
        self.squares = squares
        self.createArray(64)
        
    def createArray(self, size):
        for square in range(size):
            self.newSquare(False)
            
    def printArray(self) -> None:
        count: int = 0
        for square in self.squares:
            sqrtOfSizeSquares: int = int(math.sqrt(len(self.squares)))
            if (count == sqrtOfSizeSquares):
                print()
                count = 0
            if (count == 0 ):
                print('|', end='')
            print (square.on, end='|')
            count +=1
        print(end='\r')
        
    def newSquare(self, on) -> None:
        self.squares.append(Square(on))
    def setColumn(self, on:bool, column:int) -> None:
        for x in range(column, len(self.squares), 8):
            self.squares[x].setOnValue(on)
            
            
    def setRow(self, on) -> None:
        self.squares = self.squares[0:2]
