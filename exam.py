def sumodd(tol=89,ig=887):
	ossz=0
	for i in range(tol,ig+1):
		if i%2:
			ossz+=i
	return(ossz)
print(sumodd())

def  check_list(A, B, C):
	for x in range(len(A)):
		if(A[x]+B[x]==C[x]):
			check=True
		else:
			return False
	if(check):
		return True

A,B,C=[1,2,3],[0,1,3],[1,3,6]
print(check_list(A,B,C))
A,B,C=[1,2,3],[0,1,3],[1,3,4]
print(check_list(A,B,C))
