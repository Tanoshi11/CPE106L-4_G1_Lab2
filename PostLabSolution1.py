# stats.py

def mean(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if len(numbers) == 0:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2

    if n % 2 == 0:
        # If even, return the average of the two middle values
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        # If odd, return the middle value
        return sorted_numbers[middle]

def mode(numbers):
    if len(numbers) == 0:
        return 0
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Find the number with the highest frequency
    max_freq = max(frequency.values())
    mode_values = [num for num, freq in frequency.items() if freq == max_freq]
    
    if len(mode_values) == 1:
        return mode_values[0]
    else:
        return mode_values  # Return all modes if there is a tie

def main():
    # Input: ask user for numbers separated by spaces
    input_string = input("Enter a list of numbers, separated by spaces (e.g., 1 2 2 3 4): ")
    
    # Convert the input string to a list of numbers (as integers)
    try:
        numbers = list(map(int, input_string.split()))
    except ValueError:
        print("Please enter valid integers only.")
        return

    # Show the user the results
    print("\nList of numbers:", numbers)
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))

if __name__ == "__main__":
    main()
