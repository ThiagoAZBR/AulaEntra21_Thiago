a, b, c = input().split()

higher_from_a_and_b = (int(a) + int(b) + abs(int(a) - int(b))) / 2
highest = (int(higher_from_a_and_b) + int(c) + abs(int(higher_from_a_and_b)- int(c))) / 2
print(f'{int(highest)} eh o maior')