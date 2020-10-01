a = int(input())

year = int(a / 365)
a = a - (year * 365)
month = int(a / 30 )
day = int(a - (month * 30))

print(f'{year} ano(s)')
print(f'{month} mes(es)')
print(f'{day} dia(s)')
