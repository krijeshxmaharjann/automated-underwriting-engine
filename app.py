import streamlit as st

from underwriter import LoanApplication

st.title("FANNIE MAE UNDERWRITING ENGINE")

income = st.number_input("Monthly Gross Income ($)", min_value=0.0)
debts = st.number_input("Monthly Debts ($)", min_value=0.0)
credit = st.number_input("Credit Score", min_value=300, max_value=850, step=1)
loan = st.number_input("Loan Amount", min_value=0.0)
value = st.number_input("Property value", min_value=0.0)

if st.button("Evaluate Application"):
    application = LoanApplication(income, debts, int(credit),loan, value)
    st.write(application.evaluate_risk())
