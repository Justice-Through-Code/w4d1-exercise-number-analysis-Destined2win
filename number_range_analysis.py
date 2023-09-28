#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION

def calculate_sum(start, end):
    """
    Calculate the sum of numbers within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """
    # TODO: Implement the logic to calculate the sum of numbers within the range.
    # TODO: Return the calculated sum.
    # I use the variable total_sum to intialize my accumulator to 0
    total_sum = 0
# I use a for loop to iterate through my range of numbers which will begin at start(the start of my range) and goes up to and includes the end(end of range). I use the + 1 to make sure it loops to the end. total_sum is my variable that will keep track of my current number.
    for num in range(start, end + 1):

        total_sum += num
    return total_sum     
# calculate_sum()


def find_smallest_number(start, end):
    """
    Find the smallest number within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """
    # TODO: Implement the logic to find the smallest number within the range.
    # TODO: Return the found smallest number.


    # Here, a variable named smallest_num is declared and initialized with the value of start, which is the starting number of the range. This variable will be used to keep track of the smallest number found within the specified range.

    smallest_num = start
      #This line starts a for loop that iterates through a range of numbers. The range of numbers begins with start (the starting number of the range) and goes up to and includes end (the ending number of the range). The + 1 is added to ensure that the loop includes the end value in the range. and then it stores and return the value
    for num in range(start, end + 1):

        if num < smallest_num:
            smallest_num = num
    return smallest_num
# find_smallest_number()        

def find_largest_number(start, end):
    """
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """
    # TODO: Implement the logic to find the largest number within the range.
    # TODO: Return the found largest number.

   #  This variable will be used to keep track of the largest number found within the specified range.
    largest_num = start


    # This line starts a for loop that iterates through a range of numbers. The range of numbers begins with start (the starting number of the range) and goes up to and includes end (the ending number of the range). The + 1 is added to make sure that the loop includes the end value in the range. and then it returns and stores the value
    for num in range(start, end + 1):
        if num > largest_num:
            largest_num = num
    return largest_num
# find_largest_number()

  

def count_even_numbers(start, end):
    """
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """
    # TODO: Implement the logic to count even numbers within the range.
    # TODO: Return the count of even numbers.



# This variable will be used to keep track of the count of even numbers found within the specified range.
    count = 0

# This line starts a for loop that iterates through a range of numbers. The range of numbers begins with start (the starting number of the range) and goes up to and includes end (the ending number of the range). The + 1 is added to ensure that the loop includes the end value in the range. 

# Inside the for loop, there is an if statement. For each num in the range, it checks whether num is even. It does this by using the modulo operator % to check if num divided by 2 has a remainder of 0. If num is even, it increments the count variable by 1. This way, it keeps track of the count of even numbers encountered in the range.
    for num in range(start, end +1):

        if num % 2 == 0:
            count += 1
    return count    
# count_even_numbers()

def count_odd_numbers(start, end):
    """
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """
    # TODO: Implement the logic to count odd numbers within the range.
    # TODO: Return the count of odd numbers.

    # This variable will be used to keep track of the count of odd numbers found within the specified range.
    
    count = 0

    # This line starts a for loop that iterates through a range of numbers. The range of numbers begins with start (the starting number of the range) and goes up to and includes end (the ending number of the range). The + 1 is added to ensure that the loop includes the end value in the range.

    # Inside the for loop, there is an if statement. For each num in the range, it checks whether num is odd. It does this by using the modulo operator % to check if num divided by 2 does not have a remainder of 0. If num is odd (i.e., the condition is met), it increments the count variable by 1. This way, it keeps track of the count of odd numbers encountered in the range.
    for num in range(start, end + 1):
        if num % 2 != 0:
            count += 1
    return count    
# count_odd_numbers()