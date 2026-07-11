class LoanApplication:
    def __init__(self, income, debts, credit_score, loan_amount, property_value):
        self.income = income
        self.debts = debts
        self.credit_score = credit_score
        self.loan_amount = loan_amount
        self.property_value = property_value

        # Automatically Calculate metrices upon object creation

        self.dti = self.debts / self.income
        self.ltv = self.loan_amount / self.property_value
    
    def evaluate_risk(self):
        print(f"---Reviewing Application Metrices---")
        print(f"DTI: {self.dti:.2f} | LTV: {self.ltv:.2f} | Credit Score: {self.credit_score}")
        if self.dti > 0.45:
            return "STATUS: DENIED | Reason: Debt-To-Income (DTI) ratio exceeds 45% maximum."
        elif self.credit_score <620:
            return "STATUS: DENIED | Reason: Credit Score falls below 620 requirements."
        else:
            if self.ltv > 0.80:
                return "STATUS: APPROVED | Note: Private Mortgage Insurance (PMI) is requred."
            
            return "STATUS: APPROVED | Note: Standard Conventional term met."
        
        



