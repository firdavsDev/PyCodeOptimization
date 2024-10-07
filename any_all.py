# Bad
numbers = [1, 2, 3, 4, 5]
all_positive = True
for num in numbers:
    if num <= 0:
        all_positive = False
        break

# Good
numbers = [1, 2, 3, 4, 5]
all_positive = all(num > 0 for num in numbers)
