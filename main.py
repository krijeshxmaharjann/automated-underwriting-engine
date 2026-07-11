from underwriter import LoanApplication

def get_numeric_input(message):
            while True:
                user_input = input(message).strip()
                
                try:
                    # Attempt to convert the string input into a decimal number
                    value = float(user_input)

                    # Defensive check: Financial metrics cannot be negative numbers
                    if value < 0:
                        print("Error: Input value Cannot be Negative. Please try again.")
                        continue

                    return value
                
                except ValueError:
                    # This intercepts the crash if they typed letters or special characters
                    print(f"Invalid Input ('{user_input}'). Please Enter a Valid number.")

print("--FANNIE MAE Automated UNDERWRITING INTIALIZED--")
print("Ready to process Live Application. Follows message below.\n")

income = get_numeric_input("Enter Borrower Monthly Gross Income ($): ")
debts = get_numeric_input("Enter Borrower Total Monthly Debts ($): ")
credit = int(get_numeric_input("Enter Borrower Credit Score (300-850): "))
loan = get_numeric_input("Enter Requested Loan Amount ($): ")
value = get_numeric_input("Enter Property Appraised Value ($): ")

print("\n" + "="*50)
print("GENERATING AUTOMATED VERDICT REPORT...")
print("="*50)

# Create the application object with the verified dynamic data
current_application = LoanApplication(income, debts, credit, loan, value)

# Print out the final risk verdict string
print(current_application.evaluate_risk())
print("="*50 + "\n")
