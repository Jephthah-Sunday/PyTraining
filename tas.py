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



