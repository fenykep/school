names = ['Nils', 'Mark', 'Marilyn', 'Mariam', 'Albert']
homework = [2, 10, 4, 6, 7]
exam = [20, 55, 33, 60]
project = [12, 30, 21, 24]
lista=[names,homework,exam,project]
temp="All kids are smart"

for i in range(4):
	for j in range(len(lista)):
		print("j: ",j,"i: ",i)
		print(lista[j][i])
print(lista[3][3])

print("bubumama")
#for i in range(len(names)):
#	for j in range(len(lista)):
#	        print(lista[j][i])

#for i in range(len(names)):
#	print(lista[1][i])

