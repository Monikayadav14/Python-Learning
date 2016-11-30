# alpha=[]
# num=[]
# str="house number 14 near 24 building"
# # def check(str):
# # 	for i in str:
# # 		if str.alpha()=True:
# # 			print str
# # 	return str
# # print check(str)
# s = str.isalpha()
# if s == False:
# 	num.append(str)
# else:
# 	print "abc"
# print str

while True:
    try:
        n = raw_input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print "Great, you successfully entered an integer!"
n = int(raw_input("Please enter a number: "))