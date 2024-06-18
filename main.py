from src.Line import Line, Packet
from src.BoardDisplay import BoardDisplay, Square
from src.PacketProcessor import PacketProcessor
from src.indexGetter import indexGetter

from typing import List
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def cleanData(fileNameOrig: str, fileNameCleaned: str):
    with open(fileNameCleaned, "w") as n:
        with open(fileNameOrig, "r") as f:
            for line in f:
                line = line.rstrip('\r\n')
                if (line == ''):
                    continue
                else:
                    n.write(line + '\r')
def stripCommas(fileNameOrig: str, fileNameCleaned: str):
    with open(fileNameCleaned, "w") as n:
        with open(fileNameOrig, "r") as f:
            for line in f:
                line = line.rstrip('\n')
                valueList: List[int] = line.split(',')
                n.write('\t'.join(str(x) for x in valueList) + '\r')
          
          
def splitToInt16(value,length):
    out_list = []
    for i in range(int(length)):
        val = int.from_bytes(bytes.fromhex(value[i*4:i*4+4]), byteorder = "big")   
        
        print(val)     
        val = toSigned16(val)
        out_list.append(val)
    return out_list
        
        
def hexCleaner(fileNameOrig: str, fileNameCleaned: str) -> None:
    with open(fileNameOrig, "r") as old:
        with open(fileNameCleaned, "w") as new:
            lineList = []
            valueList: List[str] = []
            old = old.read().split("0D0A")
            for line in old:
                newLine = splitToInt16(line,64)
                lineList.append(newLine)
                print(newLine)
                try:
                    continue
                except:
                    print(line)
            print(len(lineList))
            
            for line in lineList:
                new.write('\t'.join(str(x) for x in line) + '\n')
                
            # new.write(newerLine)
                #newLine = line.replace('0D0A', "\n")
                # print(newLine)
                # newerLine = splitToInt16(newLine,32)
                # print(newerLine)
                # lineList.append(newerLine)
                
                # for line in lineList:
                #     hex: List[str] = line.rstrip('\n').split(',')
                #     valList: List[int] = []
                #     for val in hex:
                #         if(len(val) > 0):
                #             signed_integer = int(val, 16)
                #         else:
                #             signed_integer = 0
                #         valList.append(signed_integer)
                #     new.write('\t'.join(str(x) for x in valList) + '\n')
                # # new.write(newerLine)
            
               
                
def condensedDataToFile(orginalFile: str, newFile: str) -> None:
    with open(orginalFile, "r") as orgFile:
        with open(newFile, "w") as nFile:
            for line in orgFile:
                tempLine: Line = Line(line.rsplit())
                print(tempLine.dataLine())
                if(tempLine.dataLine()):
                    tempLine.cleanValues()
                    nFile.write('\t'.join(str(x) for x in tempLine.values) + '\r')

def lineToPacket(fileNameOrig: str, packetFile: str): # needs to be fixed, skips a line
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
        
def combineFile(front) -> None:
    files:List[str] = {f"{front}1.txt", f"{front}2.txt", f"{front}3.txt", f"{front}4.txt", f"{front}5.txt" }
    with open(f"{front}All.txt", '+a') as newFile:
        for file in files:
            with open(str(file)) as oldFile:
                newFile.write(oldFile.read())
    
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
        if(x < avgCutOff): 
            continue
        else:
            print(f"Index: {count}, Value: {x}")
            
def printRowCol(file:str) ->None:
    with open(file, "r") as file:
        for line in file:
            tempLine: Line = Line(line.rsplit())
            i: indexGetter = indexGetter(tempLine)
            rowVal: int = i.determineRow()
            colVal: int = i.determineColumn()
            print(f"Row: {rowVal}\tColumn: {colVal}")




def toSigned16(n):
    #return n
    n = n & 0xffff
    return (n ^ 0x8000) - 0x8000



def checkValues():
    wholeBoardFile: str = "CapturedData/WholeBoardTestCleaned.txt"
    otherFile: str = "CapturedData/Cleanedcapture3.txt"
    otherOtherFile: str = "CapturedData/SearchData/Cleaned/Row5/R5C7.txt"
    newFile: str = "CapturedData/WholeCaptureCleaned.txt"
    test: str = "CapturedData/testCaptureCleaned.txt"
    with open(test, "r") as file:
        outer_count = 0
        count = 0
        tempPacket = []
        allPackets = []
        for line in file:
            #tempLine: Line = Line(line.rsplit())
            #tempLine.cleanValues()                          # gets rid of the large values >=220
            tmp_line = line.rsplit()
            tmp_line = np.array(tmp_line,dtype=int)
            for val in tmp_line:
                tempPacket.append(val)
            allPackets.append(tempPacket)
            tempPacket = []
            outer_count +=1
            print(outer_count)
                
        with open("outputConsole4.txt", "w") as output:
            for packet in allPackets:
                index: int = np.argmax(packet)
                maxValue: int = packet[index]
                
                output.write(f"{index}\t:\t{maxValue}\r")
                #print(f"{index}\t:\t{maxValue}:\t{nextValue}:\t{prevValue}")

def normalize(origFile: str, newFile: str):
    with open(origFile, "r") as old:
        with open(newFile, "w") as new:
            for line in old:
                line = line.rstrip('\n').split('\t')
                tempArray = []
                for val in line:
                    val = int(val)
                    if(val < 0):
                        val = 0
                    elif( val > 256):
                        val = 256
                    tempArray.append(val)
                new.write("\t".join(str(x) for x in tempArray) + '\n')

def displayData(file: str):
    with open(file, "r") as f:
        allFile: List[List: int] = []
        for line in f:
            allFile.append(line.rstrip('\n').split('\t'))
        
        # fig, ax = plt.subplots()             # Create a figure containing a single Axes.
        # ax.plot(list(range(len(allFile[0]))), allFile[0])
        plt.imshow(allFile[0])
        plt.show()
        



# hexCleaner("CapturedData/testCapture.txt", "CapturedData/testCaptureCleaned.txt")
# normalize("CapturedData/testCaptureCleaned.txt", "CapturedData/testCaptureNormalized.txt")
# checkValues
# displayData("CapturedData/testCaptureNormalized.txt")

def drawStuff():
    # Prepare data
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)   

    # Initialize figure and axis
    fig, ax = plt.subplots()
    line, = ax.plot(x, y)   

    # Update function
    def update(frame):
        line.set_ydata(np.sin(x + frame / 10))
        return line,    

    # Animation
    ani = FuncAnimation(fig, update, frames=range(100), blit=True)
    # ani = FuncAnimation(figure, funciton, frames, init_func, fargs, save_count, cache_frame_data)
    # Show the animation
    plt.show()
def barcode():
    code = np.array([
        1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1,
        0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0,
        1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1,
        1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1])

    pixel_per_bar = 4
    dpi = 100

    fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
    ax.set_axis_off()
    ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
            interpolation='nearest')
    plt.show()
    
barcode()