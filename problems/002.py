"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

from euler.fibon import less_than

seq = less_than(4000000)
even = [val for val in seq if val % 2]
print(sum(even))
