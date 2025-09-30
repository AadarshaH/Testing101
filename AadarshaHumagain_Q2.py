#program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

numbers = [] # Initialize an empty list to store numbers
total = 0 # Initialize total sum of numbers
count = 0 # Initialize count of numbers
average = 0 # Initialize average of numbers
raw_num = 0 # Initialize variable to store user input

while True:
    raw_num = input("Enter a number (or 'done' to finish): ") # Prompt user for input

    if raw_num.lower() == 'done': # Check if the user wants to finish
        break

    try:
        num= float(raw_num) # Try to convert input to a float
        total += num # If successful, add to total
        count += 1 # Increment count of numbers
        numbers.append(num) # Append the number to the list

    except ValueError: # If conversion fails, handle the error
        print("Bad data") # Print error message
        continue

if count != 0:  # Avoid division by zero
    average = float(total / count) # Calculate average of numbers
else:
    average = 0

# Print the total, count, and average of the numbers:
print(f"Total:", total, "Count:", count, "Average:", average)