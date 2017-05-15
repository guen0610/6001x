def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    print("str1: ", str1)
    print("str2: ", str2)
    raw_input("Press key continue")
    # Your code here
    if len(str1) != len(str2):
	print(1)
        return False
    if str == '':
	print(2)
        return True
    if len(str1) == 1:
	print(3)
        return True
    if len(str1) == 2:
        print(4)
        return str1[0] == str2[1] and str[1] == str2[0]
    if str1[0] != str2[-1]:
	print(5)
        return False
    else:
        return semordnilap(str1[1:-1],str2[1:-1])
