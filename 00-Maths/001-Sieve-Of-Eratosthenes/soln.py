# Python program to print all primes smaller than or equal to 
# n using Sieve of Eratosthenes 
  
def SieveOfEratosthenes(n): 
	# Create a boolean array "prime[0..n]" and initialize 
	#  all entries it as true. A value in prime[i] will 
	# finally be false if i is Not a prime, else true. 
	prime = [True for i in range(n+1)] 
	p = 2
	
	sq = int(math.sqrt(n))
	while (p <= sq): 
		  
		# If prime[p] is not changed, then it is a prime 
		if (prime[p] == True): 
			  
			# Update all multiples of p 
			for i in range(p * p, n+1, p): 
				prime[i] = False
		p += 1
	
	prime = [i for i,j in enumerate(prime[2:], start=2) if j]
	return prime
      