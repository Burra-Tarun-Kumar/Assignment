def sum_of_evens(n):
    sum_even = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum_even += i
    return sum_even
n = int(input("Enter a positive integer n: "))
if n <= 0:
    print("Enter a positive integer only.")
else:
    print("The sum of all even numbers between 1 and", n, "is:", sum_of_evens(n))
