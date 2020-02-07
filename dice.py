import random
while(True):
	rep,side=raw_input("What shall I throw?").split("D")
	for i in range(int(rep)):
		print(random.randint(1,int(side)))
