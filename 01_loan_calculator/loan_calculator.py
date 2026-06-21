price=int(input("Enter the Car price: "))
down_payment=int(input("Enter the down payment: "))
if down_payment>=price:
    print("The down payment must less than price ")
    exit()
interest=float(input("Enter the interest rate: "))
duration=int(input("Enter the loan duration in years: "))
n=duration*12
loan_amount= price-down_payment
monthly_interest= interest/12/100
emi= loan_amount * monthly_interest * (1+monthly_interest)**n / ((1+monthly_interest)**n - 1)
print("The loan amount is: ",loan_amount,"\n")
print(f"The EMI is: {emi:,.2f}")
total_amount=emi*duration*12
print(f"The total amount you will pay: {total_amount:,.2f}")
total_interest=total_amount-loan_amount
print(f"The total interest you will pay is: {total_interest:,.2f}")
total_cost=total_amount+down_payment
print(f"The total cost of car is: {total_cost:,.2f}")
