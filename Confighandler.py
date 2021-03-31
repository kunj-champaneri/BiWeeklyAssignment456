#Author: Naresh Adh
#Date: 03/15/2021
#Through this program, students will learn to:
#1. validate an input file and contents in it.
#2. Handle file opening in a mode
#2.1. Handle file exceptions, etc.
#3. Search file contents



def parse_file(filename):
    #open the file to read, and implement the logic as required by the assignment-4
    tempFile = open(filename, "r")
    pFile = tempFile.readlines()
    for line in pFile:
        if 'true' in line:
            print(line)
    tempFile.close()

def validate_file(filename):
    #validate if the file is a text file, if it is return true, otherwise return false
      num1 = 0
    num2 = 0
    num3 = 0
    for i in filename:
        if i == ".":
            num1 = num1 + 1
        if i == "t" and num1 != 0:
            num2 = num2 + 1
        if i == "x" and num1 != 0:
            num3 = num3 + 1
    if num1 > 0 and num2 > 1 and num3 > 0:
        return True
    return False

#Main program, do not modify it.
if __name__ == "__main__":
    filename="my_config.txt"
    valid=validate_file(filename)

    #print all the setting values set to ON/true on the configuration file.
    if valid:
        print("File %s is a valid text file. Now printing all the settings set ON" %filename)
        parse_file(filename)
    else:
        print("File %s is NOT a valid text file. Program aborted!" % filename)
