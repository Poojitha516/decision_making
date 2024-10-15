'''
There are 3 labs in the CSE department(L1, L2, and L3) with a seating capacity of x, y, and z respectively. Find the lab which has minimal seating capacity.  
Input format:
Input consists of 3 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
Output format:
Print the minimal seating lab capacity
Refer the Sample output for formatting
Sample Input:
30
40
20
Sample Output:
L3
'''
capacity_L1 = int(input("Enter the seating capacity of L1: "))
capacity_L2 = int(input("Enter the seating capacity of L2: "))
capacity_L3 = int(input("Enter the seating capacity of L3: "))

# Determine the lab with the minimal seating capacity
if capacity_L1 < capacity_L2 and capacity_L1 < capacity_L3:
    print("L1")
elif capacity_L2 < capacity_L1 and capacity_L2 < capacity_L3:
    print("L2")
else:
    print("L3")
