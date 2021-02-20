def highest_factor(n):
    """ credit to : https://stackoverflow.com/a/17311362 """
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    return int(n)
