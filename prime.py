import math

def isPrime(num):
	# Return True if Number is prime else false
	# isPrime is slower than primeSieve()

	if num < 2:
		return False

	for i in range(2, int(math.sqrt(num))+1):
		if num%i == 0:
			return False
	return True

def primeSieve():
	sieve = [True]*sieveSize # list of Boolean True that is the length of sievesize.
	sieve[0] = False # since 0 and 1 are not prime numbre
	sieve[1] = False

	#create the sieve
	for i in range(2, int(math.sqrt(sieveSize)) + 1):
		pointer = i*2

		while pointer < sieveSize:
			sieve[pointer] = False
			pointer += i

	# compile the list of primes:
	primes = []
	for i in range(sieveSize):
		if sieve[i] == True:
			primes.append(i)

	return primes