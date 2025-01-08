# Step 1: Define the function calculate_square
def calculate_square(n):
    return n * n

# Step 2: In the main program, ask the user to input a positive integer
n = int(input("Enter a positive integer: "))

# Step 3: Call the calculate_square function and display the result
square = calculate_square(n)
print(f"The square of {n} is: {square}")
