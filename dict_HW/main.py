pupils = {'ron': 98, 'shimrit': 45, 'nehorai': 100}
print(pupils)

pupils['galit'] = 30
print(pupils)

pupils['ron'] = 96
print(pupils)

avg = 0
for v in pupils.values():
    avg += v
print(avg/len(pupils))

pupils.pop('shimrit')
print(pupils)

if 'nehorai' in pupils.keys():
    print('true(unfortunately)')
else:
    print('heydad')