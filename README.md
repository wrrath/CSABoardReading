This program allows you to input a file, and get an output of what the data collected shows as well as saving the data into a .npy file

Directions for use:

1. Capture the data using Realterm
    1. Open the port the CSA is connected to.
    2. Click the Capture tab.
    3. Select the folder you want to save to (Change from the default C:/temp.txt)
    4. Click the checkbox for HEX (if your data is unreadable from .txt, check that you clicked this box)
2. Import the file into CaptureData folder for this program
3. Select the file path for your file, and the name of the file after it is cleaned when running hexCleaner function
4. displayData shows an animation from the data
4. outputData outputs the data into a numpy array to whatever the fileName you select.  (Leave blank for .npy)