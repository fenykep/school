tarolo=[]#country, infected, death, ratio
file=open("covid.txt","r")
for line in file:
	sor=line.split(" ")
	try:
		tarolo.append([sor[0],sor[1],float(sor[2]),float(sor[2])/float(sor[1])]) #type conversion also strips newline
	except:
		print("There's something shady going on in",sor[0])
for i in tarolo:
	if min([row[3] for row in tarolo]) in i:
		print(i[0]," has the lowest ratio")
		