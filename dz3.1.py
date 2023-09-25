salary = []
while True:
    cash = int(input())
    if cash == 0:
        break
    salary.append(cash)
    print(salary)
print(sum(salary) // len(salary))