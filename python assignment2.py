# Q.1 Create a pattern using nested for loop in Python.

for i in range(6):
    for j in range(i):
        print('*', end=" ")
    print()

for i in range(4):
    for j in range(4-i):
        print('*', end=" ")
    print()


# Q.2Write a Python program to reverse a word after accepting the input from the user.
name = input('Enter a name: ')
print(name[::-1])






