#Implement collatz(n) as a generator: if n is even the next term is n // 2, otherwise 3n + 1; stop
#after yieldinng 1.

def callatz(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield 1


sequence=callatz(6)
for num in sequence:
    print(num)


length = len(list(callatz(6)))
print("length of the sequnece is:", length)


maximum=max(callatz(6))
print("maximum of the sequence is:", maximum)


even_numbers=[num for num in callatz(6) if num % 2 == 0]

print("even numbers in the sequence are:", even_numbers)