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
    with open(packetFile, "w") as p:
        with open(fileNameOrig, "r") as f:
            count: int = 0
            tempList: List[Line] = []
            for line in f:
                if(count == 3):
                    tempPacket: Packet = Packet(tempList)
                    

                    p.write('\t'.join(str(x) for x in tempPacket.packetValues()) + '\r')
                    count = 0 
                    tempList.clear()
                    tempPacket.clear()
                else: 
                    tempLine: Line = Line(line.rsplit())
                    tempLine.cleanValues()
                    tempList.append(tempLine)

                    count += 1  
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
def findAvg(fileName: str, avgCutOff: int) -> None:

    fileLength: int = 0
    avg: List[int] = [0] * 128
    with open(fileName, 'r') as file:
        for line in file:
            fileLength += 1
            line: Line = Line(line.rsplit())
            for count, value in enumerate(line.values):
                avg[count] += int(value)
    avg = [x//fileLength for x in avg]
    for count, x in enumerate(avg):
        if(x <= avgCutOff): 
            continue
        else:
            print(f"Index: {count}, Value: {x}")
    

for x in range(1,9):
    for y in range(1,9):    
        print(f"{x}:{y}")
        findAvg(f"CapturedData/SearchData/Packet/Row{x}/R{x}C{y}.txt", 1)
        print()
print("============================")
for y in range(1, 9, 2):
    print(f"R1C{y}")
    findAvg(f"CapturedData/SearchData/Packet/Row1/R1C{y}.txt", 1)
    print()