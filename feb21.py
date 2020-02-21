import matplotlib.pyplot as plt
from pylab import show  #ez kell ahhoz hogy lathass dolgokat
			#a plt library a plotolashoz kell
			#plt.savefig('kepnev.png') ez jol elmenti a dolgokat
			#pylab import show[()] ez meg jol megmutatja a dolgokat
x=[1]
y=[1]
for i in range(14):
	b=2
	for j in range(i+1):
		b=b*2
	x.append(b)
	print(x)
	y.append(i+2)
	print(y)
plt.plot(y,x)
show()
