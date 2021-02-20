""" Find the sum of all the multiples of 3 or 5 below 1000. """

multiples = [i for i in range(1, 1000) if not i % 3 or not i % 5]
print(sum(multiples))
