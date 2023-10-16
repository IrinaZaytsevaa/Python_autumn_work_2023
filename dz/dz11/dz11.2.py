spisok = []
with open('11.2.txt', encoding='utf-8') as f:
    for spi in f:
        spisok.append(spi.split(','))

import openpyxl
from openpyxl import Workbook

wb = Workbook()
wb.save('dz11.2.xlsx')
wb = openpyxl.load_workbook('dz11.2.xlsx')
ws = wb.active

spsk = sorted(spisok, key=lambda x: (x[3], x[1], x[2]))
itogo = 0
for spi in spsk:
    ws.append(spi)
    itogo += float(spi[-1])
ws.append(['ИТОГО', '', '', '', itogo])
wb.save('dz11.2.xlsx')

