'''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z. A single lab needs to be allocated to a class of 'n' students. How many of the 3 labs can accommodate 'n' students?
Input format:
Input consists of 4 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the number of students(x)
Output format:
Print the number of labs which can accommodate the 'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
2 
'''
# Get input from the user for the seating capacities of the labs and number of students
capacity_L1 = int(input("Enter the seating capacity of L1: "))
capacity_L2 = int(input("Enter the seating capacity of L2: "))
capacity_L3 = int(input("Enter the seating capacity of L3: "))
number_of_students = int(input("Enter the number of students: "))

# Initialize a counter for labs that can accommodate the students
accommodating_labs = 0

# Check each lab's capacity against the number of students
if capacity_L1 >= number_of_students:
    accommodating_labs += 1
if capacity_L2 >= number_of_students:
    accommodating_labs += 1
if capacity_L3 >= number_of_students:
    accommodating_labs += 1

# Print the number of labs that can accommodate the students
print(accommodating_labs)
