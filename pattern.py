# n=5
# for i in range(n):
# 	for j in range(i):
# 		print "*"
# 	print " "


#print a
# for x in range(5,0,-1):
# 	print '*' * x
# n=5;  
# for i in range(n):  
#     for j in range(i):  
#         print ('*',end = "")  
#     print('')  
# n=5
# for i in range(5,0,-1):
# 	# for j in range(1,n+1):
# 	# 	print '*'
# 	print '*' * i
n=5
for i in range(n,0,-1):
	 # for j in range(i,0,-1):
	if i == n:
		print i*"*"
	else:
		print (n-i)*" "+i*"*"
		