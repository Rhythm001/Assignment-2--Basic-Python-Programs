# Problem
# In a coding contest, there are prizes for the top rankers. The prize scheme is as follows:

# Top 1 participants receive rupees X each.
# Participants with rank 11 to 100 (both inclusive) receive rupees Y each.
# Find the total prize money over all the contestants.

# Input Format
# First line will contain T, number of test cases. Then the test cases follow.
# Each test case contains of a single line of input, two integers X and Y - the prize for top 10 rankers and the prize for ranks 11 to 100 respectively.
# Output Format
# For each test case, output the total prize money over all the contestants. 

t = int(input())
for i in range(t):
    X, Y = [int(x) for x in input().split()] #top10, 11-100
    prizeMoney = 10*X + 90*Y
    print(prizeMoney)