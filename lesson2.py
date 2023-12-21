# Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print out the total, and average of the numbers.
# If user enters anything other than a number,
# detect their mistake using try and except, and print
# an error message and skip to the next number.

total = 0  # Initialize total sum
count = 0  # Initialize count of numbers entered

while True:
    user_input = input("Enter a number or 'done' to finish: ")

    if user_input.lower() == 'done':
        break  # Exit the loop if user enters 'done'

    try:
        number = float(user_input)  # Convert input to float
        total += number  # Add number to total sum
        count += 1  # Increment count of numbers entered
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")
        continue  # Skip to the next iteration if input is not a number

if count > 0:
    average = total / count  # Calculate average if at least one number was entered
    print(f"Total: {total}")
    print(f"Count: {count}")
    print(f"Average: {average}")
else:
    print("No numbers were entered.")

