def fibnacci(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibnacci(n-1, memo) + fibnacci(n-2, memo)
    return memo[n]

if __name__ == "__main__":
    print(fibnacci(1000))