import sys

fib_series = []

user_limit = input ("""This is a Fibonacci sequence programmette. 
Input your limit number or skip by hitting enter:
""")

def is_num(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

if user_limit == "":
    limit = 4000000
elif is_num(user_limit) != True:
    print("Nope, it has to be an integer. Goodbye!")
    sys.exit(0)
else:
    limit = int(user_limit)

a, b = 1, 1
while b <= limit:
    a, b = b, a + b
    fib_series.append(a)

print(f"Here is the Fibonacci sequence up to {limit}:", fib_series)

even_series = []

for x in fib_series:
    if x % 2 == 0:
       even_series.append(x)

print("Even numbers only:", even_series)

even_sum = sum(even_series)

print("The sum of the even numbers:", even_sum)