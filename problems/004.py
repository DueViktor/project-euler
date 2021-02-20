
from euler.utils import is_palindrome


palindromes = list()

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        r = i * j
        if is_palindrome(r):
            palindromes.append(int(r))

print(max(palindromes))
