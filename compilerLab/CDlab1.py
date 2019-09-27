file = open("test.txt", "r")
lines = file.readlines()

for line in lines:
	str = line
	arr1 = (str.split("//"))
	if len(arr1)==2:
		print ( arr1[1], "- is a comment")
	if len(arr1)==1:
		str.split()
		arr2 = arr1[0].split("/*")
		arr3 = arr1[0].split("*/")
		
		if arr2[0]=='':
			print ("Comment starts at line-", arr2[1])
			print ("(If comment does not end then no comment)")
		if len(arr3)!=1:
			if arr3[1]=="\n":
				print ("Comment ends at line-", arr3[0])
				print ("(If comment does not start then no comment)")
file.close()


