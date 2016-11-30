def fab(n):
	# a,b=0,1
	series = []
	for i in range(0,n):
		if i == 0:
			series.append(i)
		elif i == 1:
			series.append(i)
		else:
			series.append((series[i-2]+series[i-1]))

		# # temp=a
		# # a=b
		# # b=temp
	return series
print fab(7)
