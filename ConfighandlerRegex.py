#Author: Naresh Adh
#Date: 03/26/2021
#Through this program, students will learn to:
    #1. validate an input file and contents in it using regular expression.
    #2. Handle file opening in a mode
    #2.1. Handle file exceptions, etc.
    #3. Search file contents
    #4. Use tools to check is a regular expression is 'evil'

#function-1
def classify_settings(filename):
    # implement function-1 as instructed
    j=0
    k=0
    i=0
    seton = []
    setoff = []
    setdef = []
    tempFile = open(filename, "r")
    pFile = tempFile.readlines()
    for line in pFile:
        option = line.split(":")
        if 'true' in line:
            seton.append(option[0])
            j = j+1
        elif 'false' in line:
            line.split(":")
            setoff.append(option[0])
            k = k+1
        elif 'default' in line:
            line.split(":")
            setdef.append(option[0])
            i = i+1
    tempFile.close()
    return seton, setoff, setdef
    pass


#function-2
def print_settings(setonlist, setofflist, setdefaultlist) :
    n = 0
    #implement function-2 as instructed
    print("1) Set on keywords: \n\n")
    for value in setonlist:
        print("\t" + str((n+1)) + ") " + value)
        n += 1
    n = 0
    print("2) Set off keywords: \n\n")
    for value in setofflist:
        print("\t" + str((n+1)) + ") " + value)
        n += 1
    n = 0
    print("3) Set default keywords: \n\n")
    for value in setdefaultlist:
        print("\t" + str((n+1)) + ") " + value)
        n += 1

    pass

#Main program, do not modify it.
if __name__ == "__main__":
    filename="my_config.txt"
    setonlist, setofflist, setdefaultlist=classify_settings(filename)
    #call function to print items in the lists.
    if setonlist or setofflist or setdefaultlist:
        print_settings(setonlist, setofflist, setdefaultlist)
    else:
        print("No settings found on the file.")
