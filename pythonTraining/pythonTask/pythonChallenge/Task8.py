a = [1, 2, 3, 4, 5, 6]
b = [34, 2, 9, 91, 19, 401, 0]

def print_even_numbers(array):

    for i in array:
        if i % 2 == 0:
            print("These is an even number of the array:", i)

print_even_numbers(a)

print_even_numbers(b)