import numpy as np

lets="ZABCDEFGHIJKLMNOPQRSTUVWXY"
E=np.array([[11,20,20],[2,1,24],[9,3,3]])
F=np.array([[9,0,18],[2,9,10],[23,17,23]])


#the message has to be provided without spaces
def code(key,msg):
	size=len(key)

	splitted = [msg[i:i+size].upper() for i in range(0, len(msg), size)]
	#this splits up the message into chunks, the size of the key

	if (len(splitted[-1])<size):
		for i in range(size-len(splitted[-1])):
			splitted[-1]+=splitted[-1][-1]
	#this fills up the last vector
		
	print(splitted)
	nums=[]
	temp=[]
	for i in range(len(splitted)): #this is very messy, sorry, but it converts numbers to numbers
		for j in range(size):
			temp.append(lets.index(splitted[i][j]))
		nums.append(temp)
		temp=[]
		

	transnums=np.empty([len(nums),size])
	toletters=np.empty([len(nums),size],dtype=str)

	for i in range(len(nums)): #this just does the calculation
		for j in range(size):
			transnums[i][j]=(np.matmul(key,nums[i])[j])%26
			toletters[i][j]=lets[int(transnums[i][j])]
	print(toletters)

code(E,"REDSKYATNIGHT")
code(F,"GWUCJZDWFZUSSOKZHDXMZKXBVUPMEIYHU")

#whatawonderfulday
