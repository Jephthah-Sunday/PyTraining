#line comment

...
#string
#comment
...

#interger
number1 = 123
number2 = 234
long_number = 1234567890987654321

print(type(number1))
print(type(number2))
print(type(long_number))



#Floating-point number
float1 = 123.5
float2 = 24.
float3 = .57
float4 = 23e8

print(float1)
print(float2)
print(float3)
print(float4)


#Complex number
complex_number = 2+1j


#String
testify = 'Testify'
language = 'Python'


#Boolean
is_java = False
is_python = True


name = 10
name1 = 'Testify'
name2 = False


#Escape Sequence
article = "This is an article\na multiline article\n\tEach text.\b"

#to cancel escape sequence
article =r"This is an article\na multiline article\n\tEach text.\b"

print(article)

#Concatenation

group = "wood"
attr = "peckers"
bird = group + attr

print(bird)
print('Python' + ' programming' + ' language')


#increment and decrement
result = 6
result += 7

print(result)

result = 10
result -= 3

print(result)


#Conditional statements and Logical Operators

number1 = 23
number2 = 14

print('Logical And\n')
if number1 == 23 and number2 == 14:
    print('Number1 = 23, Number2 = 14')

if number1 == 13 and number2 == 34:
    print('Number1 = 23, Number2 = 14')
else:
    print('False')

print('Logical OR\n')
if number1 == 23 or number2 == 14:
    print('Number1 = 23, Number2 = 14')

if number1 == 13 or number2 == 14:
    print('OR Number1 = 13, Number2 = 14')
else:
    print('False')


print('\nLogical NOT\n')
if not number1 == 23:
    print('Not: Number1 = 23')

if not number1 == 13:
    print('NOT: Number1 = 13')

#for loop
print('for loop\n')

#iterate sequence
fruits = ['Apple', 'Banana', 'Coconut', 'Orange']

for fruit in fruits:
    print("fruit:", fruit)


name = "python"
for ch in name:
    print('Character:', ch)
#iterate number
number = 9
for i in range(number):
    print('\nNumber:', i)



#while loop
print('\nfor loop\n')

#iterate sequence
number = 10

while number > 0:
    print("Number is", number)
    number -= 1


print('break\n')

number = 5
for i in range(number):
    if i == 4:
        break
    print("Number:", i)

while number > 0:
    if number == 3:
        break
    print("Number:", number)
    number -=1


print('\ncontinue\n')
number = 5
for i in range(number):
    if i == 4:
        continue
    print("Number:", i)

while number > 0:
    if number == 3:
        number -= 1
        continue
    print("While-Number:", number)
    number -=1


print('\nelse\n')
number = 5
for i in range(number):
    print("for-Number:", i)
else:
    print('for-end of loop')

while number > 0:
    print("while-Number", number)
    number -= 1
else:
    print("while-end of loop")

print("\nelse, for and while\n")
number = 5
for i in range(number):
    if i == 3:
        continue
    print("for-Number:", i)
else:
    print('for-end of loop')


while number > 0:
    if number == 3:
        number -= 1
        continue
    print("while-Number", number)
    number -= 1
else:
    print("while-end of loop")


print("\nelse and break\n")
number = 5
for i in range(number):
    if i == 3:
        break
    print("for-Number:", i)
else:
    print('for-end of loop')


while number > 0:
    if number == 3:
        number -= 1
        break
    print("while-Number", number)
    number -= 1
else:
    print("while-end of loop")


print("Functions\n")

def greet():
    print('Hello World from Python')

def goodbye():
    print('Thank you')
    print('Take care,we would see some other time')

greet()

goodbye()


print('Anonymous Function')

def accept(cd):
    cd('Hello Main World')

hello = lambda : print('Hello World Anonymous')

hello()
accept(lambda x : print(x))

print('Parameters')

#required parameter
def greet(name):
    print('Hello', name)

greet('Jephthah\n')


#default parameter
def add(num1=10, num2=15):
    result = num1 + num2
    print('Result', result)


add()
add(55)
add(45, 55)


#keyword argument
def minus(num1, num2):
    result = num1 - num2
    print('Result:', result)

minus(num1=45, num2=15)
minus(num2=45, num1=75)


#arbitrary argument
def print_value(*args):
    print("*Args:", args)

print_value()
print_value(1)
print_value(1, 2)
print_value(1, 2, 3)


#arbitrary/variadic keyword parameter
def print_value(**kargs):
    print("*Args:", kargs['num1'], kargs['num2'])

print_value(num1=1, num2=2)


print('\nreturn statement')
def add_and_return(num1, num2):
    result = num1 + num2
    return result

res = add_and_return(50, 50)
print('50 + 50', res)

def check_number(number):
    if number > 5:
        return
    print('Number:', number)


check_number(1)
check_number(3)
check_number(5)
check_number(6)
check_number(10)



name = 'Testify' #This is a Global viarable

def greet():
    language = 'Python'  #This is a local variable
    print('Name', name, 'language', language)

def hello():
    framework = 'selenium' #Local viarable
    print('Name', name, 'framework', framework)


platform = 'Web'

def print_platform():
    platform = 'Mobile'
    print('Platform', platform)



print(name)
greet()
hello()
print_platform()

#Loop Recursion
def reduce_number_loop(num):
    while num >= 0:
        print(num)
        num -= 1

def reduce_number_recursion(num):
    print(num)
    if num == 0:
        return
    reduce_number_recursion(num-1)


#Recursion error
def print_now():
    print('Hello World')
    print_now()

reduce_number_loop(5)
print()
reduce_number_recursion(5)


#Basic String Operations

name = "          Testify for testing and automation school, with testify        "

#len -> get the size of a string
size = len(name)
print('size', size)

#upper -> used to convert a string to upper case
upper_value = name.upper()
print("upper:", upper_value)

#lower -> used to convert a string to lower case
lower_value = name.lower()
print("upper:", lower_value)

#capitalize -> conver the first character to upper case
capitalize_value = name.capitalize()
print("capitalize:", capitalize_value)

#count -> count the occurance of a value in a string
testify_count = name.count('testify')
print('testify count:', testify_count)

t_count = name.count('t')
print('t count', t_count)

#find - get the position of a value in the string, if the value is not in the string it returns -1
for_position = name.find('for')
print('for position', for_position)

python_position = name.find('python')
print('for position', python_position)

#index - get the position of a value in the string, if the value is not in the string it throws an exception
for_index = name.find('for')
print('for index:', for_index)

python_index = name.find('python')
print('for index:', python_index)

#strip -> trim a string, remove excess white space at the beginning and at the end of a string
stripped_name = name.strip()
print('stripped:', stripped_name)


#rstrip -> trim a string, remove excess white space at the end of a string
rstripped_name = name.rstrip()
print('Right stripped:', rstripped_name)

#lstrip -> trim a string, remove excess white space at the beginning of a string
lstripped_name = name.lstrip()
print('Left stripped:', lstripped_name)

#split -> it split a string using the specified value
split_name = name.split('and')
print('split (and):', split_name)

split_name = name.split(' ')
print('split (space):', split_name)

#format -> format the specified value of a string
#named format
unformatted_one = "My name is {name}, I am a {occupation}"
formatted_one1 = unformatted_one.format(name='Newguy', occupation='QA Engineer')
formatted_one2 = unformatted_one.format(name='Newman', occupation='QA Automation Engineer')
print('Named Formatter 1:', formatted_one1)
print('Named Formatter 2:', formatted_one2)

#indexed format
unformatted_index = "My name is {0}, I am a {1}"
formatted_index1 = unformatted_index.format('Newguy', 'QA Engineer')
formatted_index2 = unformatted_index.format('Newman', 'QA Automation Engineer')
print('Index Formatter 1:', formatted_index1)
print('Index Formatter 2:', formatted_index2)

#unindexed format
unformatted_index = "My name is {}, I am a {}"
formatted_unindex1 = unformatted_index.format('Newguy', 'QA Engineer')
formatted_unindex2 = unformatted_index.format('Newman', 'QA Automation Engineer')
print('Unnidex Formatter 1:', formatted_unindex1)
print('Unindex Formatter 2:', formatted_unindex2)


#List operator
languages = ['python', 'java', 'c#']
print('list:', languages)

#append -> add new item at the end of list
languages.append('javascript')
print('append:', languages)

#insert -> add new item at any position in the list
languages.insert(0, 'c')
languages.insert(2, 'php')
print('insert', languages)

#pop -> remove an item from the specified position
languages.pop(0)
print('pop.0:', languages)
languages.pop()
print('pop:', languages)

#remove -> remove an item by value
languages.remove('php')
print('remove', languages)

#count -> return the number of occurance of item in a list
languages.append('java')
count_java = languages.count('java')
print('list:', languages)
print('count:', count_java)

#len -> count the number of item in a list
length = len(languages)
print('len:', length)

#clear -> simply deletes all the item in a list
languages.clear()
length = len(languages)
print('clear:', languages, length)

languages = ['python', 'java', 'c#']

#copy -> return a copy of the list
languages_copy = languages.copy()
print('copy:', languages_copy)

#reverse -> reverse the order of item in the list
before_reverse = languages.copy()
languages.reverse()
print('before_reverse:', before_reverse, ',after reverse:', languages)

languages = ['python', 'java', 'c#', 'c', 'smalltalk', 'ruby']

#sort -> sort the item in the list by either ascending or descending order
languages.sort()
print('sort-asc:', languages)
languages.sort(reverse=True)
print('sort-desc:', languages)

#extend -> add the content of the specified list to the current list
languages.extend(['visual basic', 'brainfast', 'ring', 'sql', 'powershell'])
print('extend:', languages)

# Basic Dictionary Operations

animals = {
    'bird': 'Parrot',
    'mammal': 'cow',
    'fish': 'Titus'
}
print('dictionary:', animals)

#get -> fetch a value using the specified key
bird = animals.get('bird')
print('get-1:', bird)
animal = animals.get('animal')
print('get-1:', animal)

#items -> list of the dictionary key-value pair
animal_items = animals.items()
print('keys:', animal_items)

#values -> return the keys as a list
animal_values = animals.values()
print('values:', animal_values)

#pop -> remove a key-value pairs using the specified key
animals.pop('mammal')
print('pop:', animals)

#update -> add more a key-value pairs into a dictionary
animals.update({'mammal': 'Goat'})
animals.update({'Insect': 'Ant', 'reptile': 'snake'})
print('update:', animals)

#popitem -> remove the last key-value pairs from the dictionary
animals.popitem()
print('popitem:', animals)

#copy -> return a copy of a dictionary
copied_animals = animals.copy()
print('copy:', copied_animals)

#clear -> removes all the elements, item, key-value pair from the dictionary
animals.clear()
print('clear:', animals)
print('clear:', copied_animals)