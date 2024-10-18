from IN import input

sum = 0
for value in input:
    #reset values for each string analyzed
    foundNumIndices = []
    #for each character in the string
    for char in value:
        #check to see if the character is a digit
        if char.isdigit():
            #if it is a digit, append it to the array of digit indices
            foundNumIndices.append(value.index(char))
            print(foundNumIndices)
            #if there is more than one instance of the digit, check for the position of the others
            startPos = value.index(char)
            while value.count(char) > 1:
                #start from the index of the previously found number
                nextPos = value.find(char, startPos +1)
                #if the number can't be found, break execution
                if nextPos == -1: break
                #append it to the array of number indices
                foundNumIndices.append(nextPos)
                #start from this position next time, exiting if we get a -1 because that means no more instances of the character were found
                startPos = nextPos
    print(f"found digits at indices {foundNumIndices}")
    #sortedIndices = foundNumIndices.sort()
    print(f"sorted indices {foundNumIndices}")
    #create a string from the first and last digit position
    numberAsString = value[foundNumIndices[0]]+ value[foundNumIndices[-1]]
    calibrationNum = int(numberAsString)
    print(f"number is {calibrationNum}")
    sum += calibrationNum
print(sum)