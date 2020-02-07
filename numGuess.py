import random
idea=random.randint(1,100)
print(idea)
uNum=raw_input("Guess!")
while(uNum!=idea):
	if(uNum>idea):
		uNum=raw_input("Woah, not so high")
	elif(uNum<idea):
		uNum=raw_input("Don't think so little")
