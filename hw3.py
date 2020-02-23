import random as rnd
import matplotlib.pyplot as plt

def printCircle():
	c = plt.Circle((2, 2), 2, color='y')
	fig, ax = plt.subplots()
	ax.set_xlim((0, 4))
	ax.set_ylim((0, 4))
	ax.add_artist(c)
	plt.show()

def rnumbers(n):
	a=[]
	for i in range(n):
		a.append(rnd.randint(1,2))
	return(a)

def sumAvg(l):
	print("avg:",sum(l) / float(len(l)),"sum: ",sum(l))
	return(sum(l) / float(len(l)),sum(l))

def sumSub(a,b,s):
	if(len(a)==len(b)):
		if(s=='+'):
			return([a[i]+b[i] for i in range(len(a))])
			#return(a+b)
		elif(s=='-'):
			return([a[i]-b[i] for i in range(len(a))])
			#return(a-b)
		else:
			print("next time please try the '-' or '+' signs")
			pass

def spreadTheGoodBibes(l):
	r=[]
	for i in l:
		if (i<0):
			r.append(0)
		else:
			r.append(i)
	return(r)

print("random number:")
print(rnumbers(7))
printCircle()
print("Average, sum: ")
print(sumAvg([1,4,2,5,4,2,9]))
print("Add, substract (7,7,3; 3,2,1)")
print(sumSub([7,7,3],[3,2,1],'+'))
print(sumSub([7,7,3],[3,2,1],'-'))
print("Positivising 1, -2, -3, 8, 7,  -1, 0, 1")
print(spreadTheGoodBibes([1, -2, -3, 8, 7,  -1, 0, 1]))

