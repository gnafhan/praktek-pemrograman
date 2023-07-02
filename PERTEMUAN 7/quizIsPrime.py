def isPrime(x):
    for i in range(2, x):
        if x%i == 0:
            return ('bukan prima')
            break
    return ('prima')
            
        
print(isPrime(17))
print(isPrime(18))
print(isPrime(19))
print(isPrime(20))
print(isPrime(21))
print(isPrime(22))