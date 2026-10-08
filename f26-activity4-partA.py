# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 4
# Author Name: Claire Nguyen
# Date: 06 Oct 2026

# SCENARIO
# You are wanting to save money for a particular purchase.
# Write a program that estimates how long it will take to grow your money to your desired amount.
# Consider 


# TODO 1: Create inputs for the following information 
#         - Your desired savings goal
#         - The amount of money as your base investment
#         - The annual interest rate
#         - The amount of money you want to deposit into the account every month (if any)

desire_saving_goal = float(input("GOAL: $"))
annual_interest_rate = float(input("INTEREST (%): ")) / 100
base_investment = float(input("BASE: $"))
monthly_deposit = float(input("MONTHLY DEPOSIT: $"))

# TODO 2: Create variables to hold number of months and current balance of the account
num_of_months = 0
current_balance = base_investment 

# TODO 3: Create a loop that will run until you have made at least your desired savings goal
    # TODO 4: Calculate amount of money earned that month through interest on your base investment and monthly deposit
    # TODO 5: Increment the number of times the loop has run so you can track how many months it takes to hit your goal

while current_balance < desire_saving_goal:
    monthly_interest = current_balance * (annual_interest_rate / 12)
    current_balance += monthly_interest + monthly_deposit
    num_of_months += 1
    continue

# TODO 6:  Print how long it will take for your investment to mature.  
#          If the duration is longer than 12 months, print your result in years.  Otherwise, print the result in months.
print(" ")
print("Number of Months:", num_of_months)
if num_of_months > 12:
    num_of_years = num_of_months / 12
    print("Number of Years:", num_of_years)
print("Total Investment: $", round(current_balance, 2))


# EXPECTED OUTPUT
# GOAL: $1,000,000
# INTEREST: 4%
# BASE: $1,000
# MONTHLY DEPOSIT: $100
#
# Number of Months: 1053
# Number of Years: 87.75
# Total Investment: $1,000,861.53
