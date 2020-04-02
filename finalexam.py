def countLetters(word):
	return(len(word.replace('a','').replace('c','')))

def recRatio():
	tarolo=[]#country, infected, death, ratio
	file=open("covid.csv","r")
	for line in file:
		sor=line.split(",")
		try:
			tarolo.append([sor[0],sor[1],float(sor[2]),(float(sor[1])-float(sor[2]))/float(sor[1])]) #type conversion also strips newline
		except:
			tarolo.append([sor[0],sor[1],0,1]) #type conversion also strips newline
	for i in tarolo:
		if max([row[3] for row in tarolo]) in i:
			print(i[0]," has the lowest ratio")

print(countLetters("attcggac"))
recRatio()



