class Property:
    def __init__(self, purchase_price, down_payment, closing_costs, renovation_expenses,
                 monthly_rental_income, fixed_expenses, variable_expenses):
        self.purchase_price = purchase_price
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.renovation_expenses = renovation_expenses
        self.monthly_rental_income = monthly_rental_income
        self.fixed_expenses = fixed_expenses
        self.variable_expenses = variable_expenses

    def calculate_total_monthly_income(self):
        return self.monthly_rental_income

    def calculate_total_monthly_expenses(self):
        return self.fixed_expenses + self.variable_expenses

    def calculate_monthly_cash_flow(self):
        return self.calculate_total_monthly_income() - self.calculate_total_monthly_expenses()

    def calculate_cash_on_cash_roi(self):
        annual_cash_flow = self.calculate_monthly_cash_flow() * 12
        total_investment = self.purchase_price + self.closing_costs + self.renovation_expenses - self.down_payment
        return annual_cash_flow / total_investment


# Sample inputs
purchase_price = 200000
down_payment = 40000
closing_costs = 5000
renovation_expenses = 10000
monthly_rental_income = 2000
fixed_expenses = 1000
variable_expenses = 500

# Create Property instance
rental_property = Property(purchase_price, down_payment, closing_costs, renovation_expenses,
                           monthly_rental_income, fixed_expenses, variable_expenses)

# Calculate required values
total_monthly_income = rental_property.calculate_total_monthly_income()
total_monthly_expenses = rental_property.calculate_total_monthly_expenses()
monthly_cash_flow = rental_property.calculate_monthly_cash_flow()
cash_on_cash_roi = rental_property.calculate_cash_on_cash_roi()

# Print results 
print(f"Purchase price: ${purchase_price:.2f}")
print(f"Down payment: ${down_payment:.2f}")
print(f"Closing costs: ${closing_costs:.2f}")
print(f"Renovation expenses: ${renovation_expenses:.2f}")
print(f"Monthly rental income: ${monthly_rental_income:.2f}")
print(f"Fixed expenses: ${fixed_expenses:.2f}")
print(f"Variable expenses: ${variable_expenses:.2f}")
print(f"Total monthly income: ${total_monthly_income:.2f}")
print(f"Total monthly expenses: ${total_monthly_expenses:.2f}")
print(f"Monthly cash flow: ${monthly_cash_flow:.2f}")
print(f"Cash on cash return on investment: {cash_on_cash_roi:.2%}")


try:
    purchase_price = float(input("Enter the property value: "))
    down_payment = float(input("Enter the down payment amount: "))
    closing_costs = float(input("Enter the closing costs amount: "))
    renovation_expenses = float(input("Enter the renovation expenses amount: "))
    monthly_rental_income = float(input("Enter the monthly rental income: "))
    fixed_expenses = float(input("Enter the fixed expenses amount: "))
    variable_expenses = float(input("Enter the variable expenses amount: "))
    holding_period = int(input("Enter the holding period (in years): "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Create Property instance #2
property1 = Property(purchase_price, down_payment, closing_costs, renovation_expenses,
                     monthly_rental_income, fixed_expenses, variable_expenses)

# Calculate required values #2
total_investment = property1.purchase_price + property1.closing_costs + property1.renovation_expenses - property1.down_payment
monthly_net_income = property1.calculate_monthly_cash_flow()
annual_net_income = monthly_net_income * 12
annual_roi = property1.calculate_cash_on_cash_roi() * 100

# Print results #2
print("Total Investment: $", total_investment)
print("Monthly Net Income: $", monthly_net_income)
print("Annual Net Income: $", annual_net_income)
print(f"Annual ROI: {annual_roi:+.2f}%")