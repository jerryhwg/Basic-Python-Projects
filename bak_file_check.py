# Python 3.7.2
# Use: check a specific folder to verify whether the files end with a ".txt" file extension
# if they do, print those qualifying file names and their corresponding modified time-stamps
# to the console
# 
# Example of:
# os module import
# listdir() method
# path.join() method
# getmtime() method
# loop

import os

def bak_file_check():
    # specify a folder
    fPath = 'C:\\Temp\\'
	# get all files within a specific directory (C:\Temp\)
    files = list(os.listdir(fPath))
    # iterate through all files in a specified folder
    for fName in files:
        # check whether each file extension is txt
        if fName.endswith(".bak"):
            # get the concatenated file name
        	abPath = os.path.join(fPath,fName)
            # check the file's last update time
        	fDate = os.path.getmtime(abPath)
            # print the result with formatting
        	print("The found backup file is '{}' and its last update time is '{}'.".format(abPath,fDate))
            #os.remove(abPath)

if __name__ == "__main__":
	bak_file_check()