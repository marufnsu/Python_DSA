# Using Memoization (top-down)
memo = [None] * 100
counter = 0
def fib(n):
    global counter
    counter += 1
    if memo[n] is not None:
        return memo[n]
    if n == 0 or n == 1:
        return n
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

print("Fib number:", fib(99))
print("Counter", counter)


# Using Bottom-Up solution
counter = 0
def fib2(n):
    fib_list = [0, 1]
    global counter
    counter += 1
    for index in range(2, n + 1):
        next_fib = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(next_fib)
    return fib_list[n]


print("Fib number:", fib2(99))
print("Counter", counter)