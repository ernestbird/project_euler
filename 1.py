n = 1000

multiple1 = 3
multiple2 = 5

multiples = []
for i in range (1, n):
    if i % multiple1 == 0 or i % multiple2 == 0:
            multiples.append(i)

print(multiples)

print(sum(multiples))