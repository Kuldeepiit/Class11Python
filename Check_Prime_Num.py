#Program To Check if a numbwr is prime or not.
n = int(input("Enter Your Number: "))
y = 0
x = 0
if n==2:
	print(n,'is a prime number')
else:
    for i in range(1,n+1):
    	if n%i == 0:
    		y += 1
    	elif n%i != 0:
    		x += 1
    if x>0 and y==2:
    	print(n,"is a prime number")
    else:
    	print(n,"is not Prime Number")
