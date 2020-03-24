import numpy as np
def purpose():
	a=	[["0 0 0 1 0 0"],
		["0 0 0 0 1 0"],
		["1 0 0 1 1 0"],
		["0 1 0 1 1 0"],
		
		["0 0 0 0 0 1"],
		["1 0 0 1 0 1"],
		["0 1 0 0 1 1"],
		["1 1 0 1 1 1"],
		
		["0 0 1 1 0 1"],
		["0 0 1 0 1 1"],
		["1 0 1 1 1 1"],
		["0 1 1 1 1 1"]]
	ar=np.empty(shape=[12,6])
	for i in range(12):
		ar[i]=a[i][0].split(" ")
	ar=ar.astype(int)
	return ar

'''
linePoints(x,y,z,x+s,y,z)
linePoints(x,y,z,x,y+s,z)
linePoints(x+s,y,z,x+s,y+s,z)
linePoints(x,y+s,z,x+s,y+s,z)
'''