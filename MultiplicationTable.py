def print_multiplication_table(n):
    # Print the table headers
    print("Multiplication Table up to", n)
    print("   ", end="")
    for i in range(1, n + 1):
        print(f"{i:4}", end="")
    print()
    
    # Print the table rows
    for i in range(1, n + 1):
        print(f"{i:2}:", end="")
        for j in range(1, n + 1):
            print(f"{i * j:4}", end="")
        print()

# Input from user
try:
    n = int(input("Enter a number to print the multiplication table up to: "))
    if n > 0:
        print_multiplication_table(n)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter an integer.")
