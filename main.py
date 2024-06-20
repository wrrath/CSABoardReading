from typing import List
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


          
def toSigned16(n):
    n = n & 0xffff
    return (n ^ 0x8000) - 0x8000

def splitToInt16(value,length):
    out_list = []
    for i in range(int(length)):
        val = int.from_bytes(bytes.fromhex(value[i*4:i*4+4]), byteorder = "big")   
        
         
        val = toSigned16(val)
        out_list.append(val)
    return out_list
        
        
def hexCleaner(fileNameOrig: str, fileNameCleaned: str) -> None:
    with open(fileNameOrig, "r") as old:
        with open(fileNameCleaned, "w") as new:
            lineList = []
            old = old.read().split("0D0A")
            
            for line in old:
                if (len(line) == 256):
                    newLine = splitToInt16(line,64)
                    lineList.append(newLine)
                else:
                    print("Line is too short")
            for line in lineList:
                new.write('\t'.join(str(x) for x in line) + '\n')

def checkValues(fileName: str): #finds significant value from each line in the file
    with open(fileName, "r") as file:
        tempPacket = []
        allPackets = []
        for line in file:
            tmp_line = line.rsplit()
            tmp_line = np.array(tmp_line,dtype=int)
            for val in tmp_line:
                tempPacket.append(val)
            allPackets.append(tempPacket)
            tempPacket = []   
        with open("outputConsole4.txt", "w") as output:
            for packet in allPackets:
                index: int = np.argmax(packet)
                maxValue: int = packet[index]
                
                output.write(f"{index}\t:\t{maxValue}\r")
                
def txtFileToArray(file: str) -> List[List[int]]:
    frames = []
    with open(file, "r") as f:
        for line in f:
            frames.append(list(map(int, line.rstrip('\n').split('\t'))))
    return frames

def setIndex(originalArray):
    # if you are reading idx, read the first value as an inverted xy grid.  
    # The first value, 19, is the bottom left of the board, 12 is the top right.
    idx = np.array([19,27,35,43,51,59,3,11,
                    23,31,39,47,55,63,7,15,
                    22,30,38,46,54,62,6,14,
                    18,26,34,42,50,58,2,10,
                    21,29,37,45,53,61,5,13,
                    17,25,33,41,49,57,1, 9,
                    16,24,32,40,48,56,0, 8,
                    20,28,36,44,52,60,4,12])
    return originalArray[idx]
def outputData(file: str):
    frames = txtFileToArray(file)
    frames = np.array(frames)
    framesOutput = []
    for frame in frames:
        frame = setIndex(frame)
        framesOutput.append(frame)
    framesOutput = np.array(framesOutput)

    np.save("NumpyTestOut", framesOutput)
    
def displayData(file: str):
    frames = txtFileToArray(file)
    
    frames = np.array(frames,dtype=float)
    frames = frames - np.min(frames)
    frames = frames/np.max(frames)
    frames = frames * 255
    frames = np.array(frames,dtype=int)
    
    rows, cols = 8, 8
    
    # Set up the figure and axis
    fig, ax = plt.subplots()
    cax = ax.imshow(np.zeros((rows, cols)), cmap='viridis', vmin=0, vmax=256, origin="lower")

    def update(frame):
        frameDisplay = setIndex(frames[frame])
        data_2d = np.array(frameDisplay).reshape((rows, cols))
        cax.set_array(data_2d)
        return cax,

    # Create an animation
    ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=30, blit=True)

    # Display the animation
    plt.show()


hexCleaner("CapturedData/testCapture.txt", "CapturedData/testCaptureCleaned.txt")
outputData("CapturedData/testCaptureCleaned.txt")
displayData("CapturedData/testCaptureCleaned.txt")
