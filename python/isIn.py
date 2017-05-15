def isIn(char, aStr):
    print("String: ", aStr)
    print("first: ", aStr[0])
    print("last: ", aStr[-1])
    print("middle: ", str(aStr[len(aStr)/2]))
    raw_input("Press any key to continue")
    if aStr == "":
	return False
    if char < aStr[0] or char > aStr[-1]:
	return False
    if aStr[len(aStr)/2] == char:
	return True
    elif aStr[len(aStr)/2] > char:
	return isIn(char, aStr[0:len(aStr)/2 - 1])
    else:
	return isIn(char, aStr[len(aStr)/2 + 1:len(aStr)])
