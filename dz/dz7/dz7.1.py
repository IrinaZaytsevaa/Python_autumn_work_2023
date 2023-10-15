def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (int(a) * int(b)) // gcd(int(a), int(b))
def calculate_lcm(numbers):
    result = int(numbers[0])
    for i in range(1, len(numbers)):
        result = lcm(result, int(numbers[i]))
    return result

numbers = input().split()
lcm_result = calculate_lcm(numbers)
print("Наименьшее общее кратное для списка чисел", numbers, "равно", lcm_result)