# Program to count the  number of even and odd numbers in a list.
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10] #Sample list of numbers to get 5 even numbers and 4 odd numbers
even_count = 0 # Initialize even number count
odd_count = 0 # Initialize odd number count

for num in numbers:
    if num % 2 == 0: # Check if the number is even or odd. If even, do:
        even_count +=1 # Increment even count
    else: # If odd, do:
        odd_count +=1 # Increment odd count

# Print the counts of even and odd numbers
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
