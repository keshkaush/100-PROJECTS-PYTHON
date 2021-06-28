n = int(input())

prime_factors= []


def factors(n):
    count = 0
    for i in range(1,n + 1):
        if n % i == 0:
            count += 1
            prime_factors.append(i)
    return count

count = factors(n)
print(count)
print(" ".join([str(x) for x in prime_factors])) #This shows all the factors in a same line with a Space b/w THEM.
