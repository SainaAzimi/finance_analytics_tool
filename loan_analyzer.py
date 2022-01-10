# coding: utf-8
import csv
from pathlib import Path
# Importing required libraries in order to generate a CSV file at the end of the challenge. 
#------------------------------------------------------------------------------------------------------------

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list

number_of_loans = len(loan_costs)
print(f"The total number of loans in the list is {number_of_loans}.")
# Using the 'len' function to calculates the total number of loans in the "loan_costs" list. 
# Using the print command that has a f-string inside to print the result. 
#------------------------------------------------------------------------------------------------------------------------------


# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans

total_value_of_loans = sum(loan_costs)
print(f"The total value of the loans is {total_value_of_loans}.")
# Using the 'sum' function to calculate the total value of loans in the "loan_costs" list.
# Using the print command that has a f-string inside it to print the result.
#---------------------------------------------------------------------------------------------------------------------------------


# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount

average_loan_price = total_value_of_loans / number_of_loans
print(f"The average loan amount is {average_loan_price: .2f}.")
# Finding the average of loan prices by deviding total value of loans by the number of loans.
# Using print command that has a f-string inside it to print the result with 2 decimal points. 
#------------------------------------------------------------------------------------------------------------------------------------------------------

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.

future_value = loan.get("future_value")
print(f"The future value on this loan is {future_value}.")
remaining_months = loan.get("remaining_months")
print(f"{remaining_months} months are remaining in this loan.")
# Extracting the key for "future_value" & "remaining_months" of the loan from the loan dictionary using the 'get' function. 
# Using the print command that has a f-string inside it to print the result.
#------------------------------------------------------------------------------------------------------------------------------------------------------


# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

discount_rate = 0.20
present_value = future_value / (1 + (discount_rate / 12)) * remaining_months
print(f"The present value or the fair value of this loan is ${present_value: .2f}.") 
# We are given a discount rate of 0.20 
# Calculating the present value using the given furmula and "future_value" and the "remaining_months" that we extracted above. 
# using the print command that has a f-string inside it to print the result with 2 decimal points. 
#------------------------------------------------------------------------------------------------------------------------------------------------------

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

loan_price = loan.get("loan_price")
print(f"The loan price on this loan is ${loan_price}.")
#Extracting the key for loan price of the loan from the loan dictionary using the 'get' function. 
# Using the print command that has a f-string inside it to print the result.

if present_value >= loan_price: 
    print("The loan is worth at least the cost to buy it.")
else:
    print("The Loan is too expensive and not worth the price.")
 
# Comparing "present_value" & "loan_price" by using if conditional statement to decide if this loan is worth it or too expensive. 
# using the print command, printing "The loan is worth at least the cost to buy it." if present_value is bigger than or equal to "loan_price"
# using the print command, printing "TThe Loan is too expensive and not worth the price." if present_value is smaller than "loan_price"
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------



"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
def present_value (future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + (annual_discount_rate / 12)) * remaining_months
    return present_value

# Defining "present_value" funtion in order to calculate the present value of the "new_loan" dictionary.
# Parameters of function are "future_value", "remaining_months", and "annual_discount_rate". 
# Calculating "present_value" inside the function using the given furmula.
# Returing "present_value" as output of function by using "return" command.
#----------------------------------------------------------------------------------------------------------------------------------------------



# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
annual_discount_rate = 0.20
future_value = new_loan.get("future_value")
remaining_months = new_loan.get("remaining_months")
print(f"The present value of the loan is: ${present_value (future_value, remaining_months, annual_discount_rate)}")
# Extracing the key for "future_value" & "remaining_months" from the "new_loan" dictionary using the 'get' function. 
# Using the print command with an f-string inside of it to print the output of the "present_value" function 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`

inexpensive_loans = []
# Define an empty list called "inexpensive_loans" that will be used later to save loans with cost of less than 500.
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans: 
    if loan.get("loan_price") <= 500:
        inexpensive_loans.append(loan)
# Using for loop to iterate through all loans inside "loans" dictionary
# Using if conditional statement inside the for loop to find loans that are less than or equal to 500. using "get" function to extract the "loan_price" key fronm the "loans" dictionary.
# Using "append" function to add values of the loans with "loan_price" of less than or equal to 500 to the empty list created above 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------     

    
# @TODO: Print the `inexpensive_loans` list
print(inexpensive_loans)
# We use the print command to print the inexpensive loans list. 
#--------------------------------------------------------------------

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
#Defining a list for the CSV headers(culumns)
#--------------------------------------------------------------------


# Set the output file path
output_path = Path("inexpensive_loans.csv")
# Defining a path(name) for the CSV file that will be generated in the same folder
#-----------------------------------------------------------------------------------

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
with open(output_path, 'w', newline='') as csvfile:
    # Opening a link to the file on your computer. 'w' parameter indicates that we are writing to the file. newline='' is required to handle any special characters that are in the loans dictionary. 
        csvwriter = csv.writer(csvfile, delimiter=",")
        # Allowing Writing content on the file. The delimeter="," to use commas to seperate rows and columns. 
        csvwriter.writerow(header)
        # Converting list to rows of data in csv file using the "writerow" funtion & the header list defined above. 
        for row in inexpensive_loans:
            csvwriter.writerow(row.values())
        # Using for loop to writed all values of "inexpensive_loans" to the csv file one at a time. 
        # Using values() funtion extract and write the values of the dictionary into the csv file.
#-----------------------------------------------------------------------------------------------------------------------------------------------