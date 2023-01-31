data = input()
DD,MM,AA = data.split('/')

print(f'{DD}-{MM}-{AA}')
print(f'{MM}-{DD}-{AA}')
print(f'{AA}/{MM}/{DD}')