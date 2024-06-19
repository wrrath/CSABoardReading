from typing import List
from src.Line import Line
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


          
def toSigned16(n):
    #return n
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
            valueList: List[str] = []
            old = old.read().split("0D0A")
            
            for line in old:
                # print(f"Line length: {len(line)}")
                if (len(line) == 256):
                    try:
                        newLine = splitToInt16(line,64)
                        lineList.append(newLine)
                        #print(newLine)
                    except:
                        #print(line)
                        continue
            
            for line in lineList:
                new.write('\t'.join(str(x) for x in line) + '\n')

def checkValues(fileName: str): #finds significant value from each line in the file
    with open(fileName, "r") as file:
        outer_count = 0
        count = 0
        tempPacket = []
        allPackets = []
        for line in file:
            tmp_line = line.rsplit()
            tmp_line = np.array(tmp_line,dtype=int)
            for val in tmp_line:
                tempPacket.append(val)
            allPackets.append(tempPacket)
            tempPacket = []
            outer_count +=1    
        with open("outputConsole4.txt", "w") as output:
            for packet in allPackets:
                index: int = np.argmax(packet)
                maxValue: int = packet[index]
                
                output.write(f"{index}\t:\t{maxValue}\r")
                
def fileToArray(file: str) -> List[List[int]]:
    frames = []
    with open(file, "r") as f:
        for line in f:
            frames.append(list(map(int, line.rstrip('\n').split('\t'))))
    return frames

def outputData(file: str):
    frames = fileToArray(file)
    frames = np.array(frames)
    idx = np.array([19,23,22,18,21,17,16,20,
                    27,31,30,26,29,25,24,28,
                    35,39,38,34,37,33,32,36,
                    43,47,46,42,45,41,40,44,
                    51,55,54,50,53,49,48,52,
                    59,63,62,58,61,57,56,60,
                    3, 7, 6, 2, 5, 1, 0, 4,
                    11,15,14,10,13,9, 8, 12])
    
    framesOutput = []
    for frame in frames:
        frame = frame[idx]
        framesOutput.append(frame)
    framesOutput = np.array(framesOutput)

    np.save("NumpyTestOut", framesOutput)
    
def displayData(file: str):
    frames = fileToArray(file)
    
    frames = np.array(frames,dtype=float)
    frames = frames - np.min(frames)
    frames = frames/np.max(frames)
    frames = frames * 255
    frames = np.array(frames,dtype=int)
    
    
    idx = np.array([19,23,22,18,21,17,16,20,
                    27,31,30,26,29,25,24,28,
                    35,39,38,34,37,33,32,36,
                    43,47,46,42,45,41,40,44,
                    51,55,54,50,53,49,48,52,
                    59,63,62,58,61,57,56,60,
                    3, 7, 6, 2, 5, 1, 0, 4,
                    11,15,14,10,13,9, 8, 12])
  
    rows, cols = 8, 8
    

    # Set up the figure and axis
    fig, ax = plt.subplots()
    cax = ax.imshow(np.zeros((rows, cols)), cmap='viridis', vmin=0, vmax=256)



    def update(frame):
        frameDisplay = frames[frame][idx]
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
