my_list = [
       [1,2,3,4,5,6,7,1,2,3,4,5,6,7],
       [1,2,3,4,5,6,7,1,2,3,4,5,6,7],
       [1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6],
       [7,1,2,3,4,5,6,7],
       [1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7]
]
for item in my_list:
	a = len(item)
	b = sum(item)
	c= item[1]
	print "Lenght of list is %s" %a
	print "Sum of list is %s" %b
	print c

