import calendar

lis, lis1 = [], []
year = 2023
counter = 0

for month in range(1, 13):
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        dd = calendar.weekday(year, month, day)
        if dd == 3:
            counter += 1
            lis.append((day, month, year))
            if counter % 3 == 0:
                break
lis1 = reversed(lis[::-3])

for date in lis1:
    print(f"{date[0]:02d}.{date[1]:02d}.{date[2]}")