def find_largest_numbers(x):
    largest_numbers = []
    for row in x:
        for num in row:
            if len(largest_numbers) < 3 or num > largest_numbers[0]:
                largest_numbers.insert(0, num)
                if len(largest_numbers) > 3:
                    largest_numbers.sort()
                    largest_numbers.pop(0)

    return largest_numbers
n = 2
m = 3
x = [[1, 6, 3], [4, 5, 4]]
result = find_largest_numbers(x)
print(result)
