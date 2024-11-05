# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random

def random_numbers_to_file(filename, num_numbers):
    with open(filename, 'w') as file:
        for _ in range(num_numbers):
            random_number = random.randint(1, 500)
            file.write(f"{random_number}\n")

def main():
    while True:
        try:
            num_numbers = int(input("Enter the number of random numbers to generate (up to 1000): "))
            if 1 <= num_numbers <= 1000:
                break
            else:
                print("Please enter a number between 1 and 1000.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    
    filename = "random_numbers.txt"

random_numbers_to_file(filename, num_numbers)

    print(f"{num_numbers} random numbers have been written to {filename}.")

if __name__ == '__main__':
    main()
