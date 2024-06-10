from src.Line import Line, Packet
from src.BoardDisplay import BoardDisplay, Square
from src.PacketProcessor import PacketProcessor
from typing import List

def cleanData(fileNameOrig: str, fileNameCleaned: str):
    with open(fileNameCleaned, "w") as n:
        with open(fileNameOrig, "r") as f:
            for line in f:
                line = line.rstrip('\r\n')
                if (line == ''):
                    continue
                else:
                    n.write(line + '\r')
def lineToPacket(fileNameOrig: str, packetFile: str):
    with open(fileNameOrig) as f:
        with open(packetFile) as p:
            for line in f:
                
    return
def checkForAnyValues(totalData):
    indexList: List[List[dict]] = []
    for count, packet in enumerate(totalData):
        if(count > 0):
            prevList = totalData[count-1].packetValues()
            currList = packet.packetValues()
            tempList: List[dict] = []
            for x in range(len(packet.packetValues())):
                info: dict = {}
                if(prevList[x] == currList[x] and count < 2):
                    info = {"index" : x, "value" : prevList[x]}
                    tempList.append(info)
                elif(prevList[x] == currList[x]):
                    for list in indexList:
                        for d in list:
                            if(x == d.get("index") and prevList[x] == d.get("value")):
                                print("exists")
                                print(d)
                                d.update({"exists:": 1})
                            else: 
                                d.update({"exists:": 0})
            for list in indexList:
                for d in list:
                    if(d.get("exists") == "1"):
                        print(d)
    print(indexList)
    
def fileOperator(readFile: str):  
    totalData: List[Packet] = []
    with open(readFile, "r") as file:
        packet:Packet = Packet([])
        count: int = 0
        for line in file:
            if (count == 4):
                temp = packet.copy()
                totalData.append(temp)
                packet.clear()
                count = 0
            list = line.rsplit()
            lineObj = Line(list)
            lineObj.cleanValues()
            packet.addLine(lineObj)
            count += 1
            
    for packet in totalData:
        values: List[int] = packet.packetValues()
        for value in range(0, len(values), 2):
            print(values[value], end=',')
        print()
        
        # if(packet.packetValues()[14] >0):
        #     print("column 1", end=':')
        # # elif():
        # # elif():
        # # elif():
        # # elif():
        # # elif():
        # # elif():
        # # elif():
        # # if(packet.packetValues()[] > 0)
        print()
        
    # Saving output to text file
    
    # n = open("CapturedData/row1Column1Data/R1C1D1.txt", "w")
    w = open("CapturedData/row1Column1Data/R1C1D1.txt", "w")
    for packet in totalData:
        w.write('\t'.join(str(x) for x in packet.packetValues()) + '\r')
        for line in packet.lines:
            p = 0
            # n.write('\t'.join(str(x) for x in line.values) + '\r')
    # n.close()
    w.close()
    
    
    # board: BoardDisplay = BoardDisplay([])
    # board.setColumn(1,0)
    # board.printArray()
    # print(totalData[0].packetValues())
    # p: PacketProcessor = PacketProcessor(totalData[0])
    # p.findMaxValues()
    
    # checkForAnyValues(totalData)
    
    
    # totalData[15].printPacket()
    # print()
    # totalData[16].printPacket()
    # print()
    # totalData[17].printPacket()
    # for x in range(len(totalData)):
    #     first: int = totalData[x].lines[3].values[8]
    #     second: int = totalData[x].lines[3].values[9]
    #     print(first, end=" : ")
    #     print(second)
    #     if (first == second == 255):
    #         print()
    
    
def combineFile(front) -> None:
    files:List[str] = {f"{front}1.txt", f"{front}2.txt", f"{front}3.txt", f"{front}4.txt", f"{front}5.txt" }
    with open(f"{front}All.txt", '+a') as newFile:
        for file in files:
            with open(str(file)) as oldFile:
                newFile.write(oldFile.read())
    

    
    
    

            
                
# cleanData("CapturedData/row1Column1Data/column1Row1Data5.txt", "CapturedData/row1Column1Data/column1Row1Data5DataCleaned.txt")
# fileOperator("CapturedData/row1Column1Data/column1Row1Data1DataCleaned.txt")
def findAvg():
    front: str = "CapturedData/row1Column1Data/R1C1D"

    totalData: List[Line] = []
    with open(f"{front}All.txt", 'r') as newFile:
        for line in newFile:
            list = line.rsplit()
            lineObj = Line(list)
            totalData.append(lineObj)
    avg: List[int] = [0] * 128
    for line in totalData:
        list = line.values
        for count, value in enumerate(list):
            avg[count] = avg[count] + int(value)
            if (int(value) > 1):
                # print(value, end=',')
                continue
        print()
    avg = [x//1808 for x in avg]
    print(avg)
    
for x in range(1,9):
    for y in range(1,9):    
        lineToPacket(f"CapturedData/SearchData/Cleaned/Row{x}/R{x}C{y}.txt", f"CapturedData/SearchData/Packet/Row{x}/R{x}C{y}.txt")
        print(f"{x}:{y}")