numbers = (10, 15, 20, 25, 30, 35, 40)

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Numbers:", numbers)
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)
