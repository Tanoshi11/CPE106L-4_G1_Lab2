filename = input("Enter the filename: ")


file = open(filename, 'r') 
lines = file.readlines()
file.close()


while True:
    
    print(f"\nThe file contains {len(lines)} lines.")
    print("Enter a line number to view (Input 0 to quit):")
    
    
    line_number = int(input("Line number: ")) 
    
    
    if line_number == 0:
        print("Exiting the program...")
        break
    
    
    elif 1 <= line_number <= len(lines):
        print(f"Line {line_number}: {lines[line_number - 1].strip()}")
    else:
        print("Invalid line number. Please enter a number between 1 and the total number of lines.")
