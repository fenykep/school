def pevens(n=500):
	for i in range(5,n+1):
		if(i%2==0):
			print(i)

def  check_list(A, B, C):
	if(len(A)==len(B) and len(B)==len(C)):
		for x in range(len(A)):
			if(A[x]/B[x]==C[x]):
				check=True
			else:
				return False
		if(check):
			return True


	else:
		print("Sorry, the list lengths do not match")
		return
print(pevens())
print(check_list(A= [6,4,1],B=[2,2,1],C=[3,2,1]))
print(check_list(A= [1,2,3],B=[1,1,3],C=[1,3,4]))