input = input("Enter a number greater than or equal to 0: ")

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(input + "! is " + str(factorial(int(input))))