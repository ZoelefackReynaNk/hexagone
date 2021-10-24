while True:
	n=int(input("enter an odd integer: "))
	for i in range(1,n+1):
		print((n-i)*"  ",i*"*   ","\n")
	i=n-1
	while i>0:
		#if i%2==1:
		print((n-i)*"  ",i*"*   ","\n")
		i-=1