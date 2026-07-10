# ==========================================
# PHASE 1: BORROWER PROFILE & BASIC RATIOS
# ==========================================
#1. Setup the variables
monthly_income = float(input("Enter your monthly income: "))
monthly_debt = float(input("Enter your monthly debt: "))
credit_score = float(input("Enter your Current credit score: "))
loan_amount = float(input("Enter your total loan amount "))
property_value = float(input("Enter your total property value "))

# Printing variables
print(f"Monthly Income: ${monthly_income}")
print(f"Monthly Debts: ${monthly_debt}")
print(f"Credit Score: {credit_score}")
print(f"Loan Amount: ${loan_amount}")
print(f"Property Value: ${property_value}")

#2. Calculate the Core housing finance ratios
DTI = monthly_debt/monthly_income
LTV = loan_amount/property_value

#3. Print the raw results to the Console
print("--Underwriting Engine Raw Output--")
print("Calculated DTI:", DTI)
print("Calculated DTI:", LTV)

