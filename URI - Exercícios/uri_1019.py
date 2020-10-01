value = int(input())

hour = int(value / 3600)
value = value - (hour * 3600)
minute = int( value / 60)
sec = int( value - (minute * 60) )
print(f'{hour}:{minute}:{sec}')
    