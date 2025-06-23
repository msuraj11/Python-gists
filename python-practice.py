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
# '''
# 1   3   5   7   9   11   13   15   17   19
# 1
# 1 + 3 = 4
# 1 + 3 + 5 = 9
# 1 + 3 + 5 + 7 = 16
# 1 + 3 + 5 + 7 + 9 = 25
# 1 + 3 + 5 + 7 + 9 + 11 = 36
# 1 + 3 + 5 + 7 + 9 + 11 + 13 = 49
# 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 = 64
# 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 = 81
# 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 = 100
# Sum of first 10 odd numbers is: 100
# '''

points = [[1,2,3], [0,4], [0], [1,2,3], [4], [0,4], [1,2,3]]

for point in points:
  print(''.join(['s' if i in point else ' ' for i in range(5)]))
# """
#  sss 
# s   s
# s    
#  sss 
#     s
# s   s
#  sss 
# """

x = 25

def printer(y = x):
  global x
  print(x, y)
  x = y
  print(x, y)
  x = 50
  return x

y = printer(7)
print(x, y)

# '''
# 25 7
# 7 7
# 50 50
# '''

x = 'jkjkljkljl'

def outer(x):
  x = 20 #Enclosing Scope
  return lambda: print(x)

inner_func = outer(x)
inner_func()
# 20

def give_vowel_count(sentence):
  return {vowel: sentence.lower().count(vowel) for vowel in 'aeiou'}

give_vowel_count('This sentence has vowels with only one "u"')
# {'a': 1, 'e': 5, 'i': 2, 'o': 3, 'u': 1}

class Dog:
  def __init__(self, **kwargs):
    self.dog_props = kwargs

  def extract_single_prop(self, prop_name):
    return self.dog_props.get(prop_name)

  def push_direct_props(self):
    for prop_name, prop_value in self.dog_props.items():
      setattr(self, prop_name, prop_value)

  def get_all_props(self):
    return self.dog_props

  def __str__(self):
    return str(self.dog_props)

  def add_prop(self, **kwargs):
    if len(kwargs) == 0:
      return 'Please add some details before invoking this function :('
    for prop_name, prop_value in kwargs.items():
      self.dog_props[prop_name] = prop_value
    self.push_direct_props()

  def delete_prop(self, prop_name):
    del self.dog_props[prop_name]

roland = Dog(breed = 'Labrador', name = 'Roland', color = 'white', age = 3)
roland.dog_props
# """
# {'breed': 'Labrador', 'name': 'Roland', 'color': 'white', 'age': 3}
# """
roland.extract_single_prop('age')
# 3
roland.push_direct_props()
roland.breed
# Labrador
roland.get_all_props()
# {'breed': 'Labrador', 'name': 'Roland', 'color': 'white', 'age': 3}
type(print(roland))
# {'breed': 'Labrador', 'name': 'Roland', 'color': 'white', 'age': 3}
# NoneType
def bark():
  print('Woof!')

eat = lambda: print('Eating Pedigree...')
roland.add_prop(bark=bark, eat=eat)
roland.get_all_props()['bark']()
# Woof!
