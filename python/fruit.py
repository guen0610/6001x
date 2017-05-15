def nfruits(init, pattern):
   """
   init: A non-empty dictionary containing type of fruit and its quantity initially with Python when he leaves home (length < 10)
   pattern: A string pattern of the fruits eaten by Python on his journey as observed by Cobra. 

   Python is an MIT student who loves fruits. He carries different types of fruits (represented by capital letters) daily from his house to the MIT campus to eat on the way. But the way he eats fruits is unique. After each fruit he eats (except the last one which he eats just on reaching the campus), he takes a 30 second break in which he buys 1 fruit of each type other than the one he just had. Cobra, his close friend, one day decided to keep a check on Python. He followed him on his way to MIT campus and noted down the type of fruit he ate in the form of a string pattern (Eg.: 'AABBBBCA'). Can you help Cobra determine the maximum quantity out of the different types of fruits that is present with Python when he has reached the campus?
   """
   assert (type(init) == dict and type(pattern) == str), "Argument not match"
   assert (len(init) < 10),"Init must less than 10"
   for c in pattern:
	for k in init.keys():
	    if c in init.keys(): 
 	    	if k == c:
		    try:
		    	init[k] -= 1
		    except:
		    	print("Something happened")
	        elif c != pattern[-1]:
		    init[k] += 1
	print(init)
	print("---------------")
	      
	    
