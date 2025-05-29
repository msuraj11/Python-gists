random_list = [1,2,3,1,2,1,5,4,6,1,2,3,1,2,5,2,'hi',10,'hello']

numeric_list = [item for item in random_list if isinstance(item, (int, float))]
print(numeric_list)
# O/P: [1, 2, 3, 1, 2, 1, 5, 4, 6, 1, 2, 3, 1, 2, 5, 2, 10]

numeric_list.sort()
# O/P: [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 5, 5, 6, 10]

print(list(filter(lambda x: x == x[::-1], ['naman', 'shreyas', 'noon', 'madam', 'racecar', 'virat'])))
# Printing Palindrome O/P: ['naman', 'noon', 'madam', 'racecar']

print(list(filter(lambda x: any(x.lower().startswith(item) for item in ['a', 'e', 'i', 'o', 'u']), ['Akash', 'Isparsh', 'kailash'])))
# Printing words starting with vowels O/P: ['Akash', 'Isparsh']

# Priting sum of first 10 odd numbers
sum = 0
printable_string = ''
odd_numbers = list(filter(lambda r: r%2 != 0,range(1,21)))
for k, num in enumerate(odd_numbers):
    if k == 0:
        print('   '.join(map(lambda o: str(o), odd_numbers)))
    sum += num
    printable_string += f'{num}' if k == 0 else f' + {num} = {sum}'
    print(printable_string)
    str_broken = printable_string.split(' =')
    printable_string = str_broken[0]
print(f'Sum of first 10 odd numbers is: {sum}')
# O/P:
'''
1   3   5   7   9   11   13   15   17   19
1
1 + 3 = 4
1 + 3 + 5 = 9
1 + 3 + 5 + 7 = 16
1 + 3 + 5 + 7 + 9 = 25
1 + 3 + 5 + 7 + 9 + 11 = 36
1 + 3 + 5 + 7 + 9 + 11 + 13 = 49
1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 = 64
1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 = 81
1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 = 100
Sum of first 10 odd numbers is: 100
'''
