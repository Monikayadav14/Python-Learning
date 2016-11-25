x = [28.465411,77.023592]
y = [28.459771,77.031788]
my_list1 = [[28.462525,77.026853],[28.467335,77.034127]]
for i in my_list1:
	if y[0] < i[0] < x[0] and x[1] < i[1] < y[1]:
		print "inside"
	else:
		print "outside"

		# Monika