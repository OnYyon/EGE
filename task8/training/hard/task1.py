from itertools import permutations
count = []
for i in permutations('росомаха'):
    a1 = ''.join(i)
    a = ''.join(i)
    a = a.replace('о', 'n').replace('а', 'n')
    a = a.replace('р', 'c').replace('с', 'c').replace('м', 'c').replace('х', 'c')
    if ('cc' not in a) and ('nn' not in a):
        count.append(a1)
print(len(count))
