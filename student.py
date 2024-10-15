'''
There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1
'''
capacity_L1 = int(input("Enter the seating capacity of L1: "))
capacity_L2 = int(input("Enter the seating capacity of L2: "))
capacity_L3 = int(input("Enter the seating capacity of L3: "))
number_of_students = int(input("Enter the number of students: "))

# Initialize variables to track the best lab
suitable_lab = None
max_capacity_used = -1

# Check each lab to see if it can accommodate the students
if capacity_L1 >= number_of_students:
    capacity_used = capacity_L1
    if capacity_used > max_capacity_used:
        max_capacity_used = capacity_used
        suitable_lab = "L1"

if capacity_L2 >= number_of_students:
    capacity_used = capacity_L2
    if capacity_used > max_capacity_used:
        max_capacity_used = capacity_used
        suitable_lab = "L2"

if capacity_L3 >= number_of_students:
    capacity_used = capacity_L3
    if capacity_used > max_capacity_used:
        max_capacity_used = capacity_used
        suitable_lab = "L3"

# Print the suitable lab
if suitable_lab:
    print(suitable_lab)
else:
    print("No suitable lab available")
