def lab1Question1(input_gb):
    # Convert the input of a number of gigabytes to the number of bytes
    num_bytes = None
    # Do the work here
    # The solution to this goes here (and in all of them below...)
    # Set the variable num_bytes to the answer and return it
    num_bytes = input_gb * 1024 * 1024 * 1024 # 1024 Bytes > 1 Kilobyte, 1024 Kilobytes > 1 Megabyte, 1024 Megabytes > 1 Gigbyte
    return num_bytes

def lab1Question2(name):
    # Take an input of a name, return True if there is an odd number of characters in the name, False otherwise
    # Return None if the input is not a string
    is_odd = None
    # Check if name is a string type
    if type(name) is str: 
        if (len(name)%2 > 0):
            is_odd = True
        elif (len(name)%2 == 0):
            is_odd = False
    return is_odd

def lab1Question3(input_string, input_number):
    # Take in two inputs - a string and a number
    # Return the character of the string in the index given by number.  If this index does not exist, then return -1.
    character_at = -1
    # Checks if the input_number is in range of the lowest index to the highest index number for input_string
    if (len(input_string) - 1 >= input_number) and (-(len(input_string) - 1) <= input_number): 
        character_at = input_string[input_number]
    return character_at

def lab1Question4(file_name):
    # Take an input of a file name. 
    # Read that file and return a list of all numbers in that file
    list_of_nums = []
    file = open(file_name)
    for line in file:
        print(line)
        list_of_nums.append(line)
    file.close()
    return list_of_nums

print(lab1Question4('github/test_file1.txt'))

def lab1Question5(list_numbers):
    # Take an input of a list of numbers
    # Return the mode from that list. 
    mode_of_list = None
    number_dict = {}
    for number in list_numbers:
        if not number in number_dict:
            number_dict[number] = 1
        else:
            counter = number_dict[number] + 1
            number_dict.update({number: counter})
    print(number_dict)
    var_mode = 0
    for key, number in number_dict.items():
        if number > var_mode:
            var_mode = number
            mode_of_list = key
    return mode_of_list

'''
print("      ")
my_list = [2,2,1,1]
print(lab1Question5(my_list))
'''

def lab1Question6(quarters, dimes, nickels, pennies):
    # Take in 4 inputs - the number of quarters, dimes, nickels, and pennies in a handful
    # Return the total amount in dollars
    # For example, if the handful contains 4 quarters, 3 dimes, 2 nickels, and 1 penny, the function should return 1.41.
    total = None
    return total

## Example of calling a function to test these... 
# Question 1 Check:
in_gb = 10
expected_bytes = 10*1024*1024*1024
calculated_bytes = lab1Question1(in_gb)

print("Input gigabytes: ", in_gb)
print("Expected bytes: ", expected_bytes)
print("Calculated bytes: ", calculated_bytes)
if expected_bytes == calculated_bytes:
    print("Test passed")
else:
    print("Test failed")

# You can make similar tests to check if things work for you. 
# This is kind of annoying, I am aware, but it is a really important skill in programming. 
# Determining how to check if your code works, and define specific tests for what "working" means is 
# something that allows you to tackele any larger problem - you can break it into smaller bits, attack one bit at a time,
# check to ensure you've done it correctly, and then move on to the next bit.