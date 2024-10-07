"""
map & filter: bu tayor funksiyalardan katta massivlar bilan ishlash jarayonida, loop bor joylarda har doim foydalanishga harakat qiling

"""

# Bad
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num**2)


# Good
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))


# Bad
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)

# Good


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, numbers))

from functools import reduce

# reduce()
