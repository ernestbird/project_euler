#n = 13195
n = 600851475143

i = 2

prime_nums = []

while i <= n:
    if n % i != 0:
        i = i+1
    else:
        n = n/i
        prime_nums.append(i)

print(prime_nums)
print(f"The biggest prime number is {i}")


    
