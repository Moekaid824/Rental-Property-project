class Property:
    def __init__(self, purchase_price, down_payment, closure_costs, renovation_costs,
                 monthly_rental_income, fixed_costs, variable_costs): #declaring all these variables to put in my self tags
        self.purchase_price = purchase_price
        self.down_payment = down_payment
        self.closure_costs = closure_costs
        self.renovation_costs = renovation_costs 
        self.monthly_rental_income = monthly_rental_income #self.all variables listed above after __init__
        self.fixed_costs = fixed_costs
        self.variable_costs = variable_costs

    def calculate_total_monthly_income(self): # gets us or total monthly income
        return self.monthly_rental_income

    def calculate_total_monthly_costs(self): # gets us or total monthly costs
        return self.fixed_costs + self.variable_costs

    def calculate_monthly_cash_flow(self): # gets our cash flow by subtracting our total monthly income - total monthly expenses
        return self.calculate_total_monthly_income() - self.calculate_total_monthly_costs()

    def calculate_cash_on_cash_roi(self): # gets our percentage from our anual cash flow from our monthy cash flow from a 12 month period
        annual_cash_flow = self.calculate_monthly_cash_flow() * 12
        total_investment = self.purchase_price + self.closure_costs + self.renovation_costs - self.down_payment # adds our purchase price, closing cost and revoation expenses to subtract our down payment.
        return annual_cash_flow / total_investment # returns our results from the code above


# Sample inputs to get our total expenses, monthly cash flow, and roi
purchase_price = 300000
down_payment = 50000
closure_costs = 7500
renovation_costs = 15000
monthly_rental_income = 4000
fixed_costs = 1500
variable_costs = 750

# Create Property instance from our self.variables we delcared in the beginning
rental_property = Property(purchase_price, down_payment, closure_costs, renovation_costs,
                           monthly_rental_income, fixed_costs, variable_costs)

# Calculate required values from our def calculations with the self being the parameter
total_monthly_income = rental_property.calculate_total_monthly_income()
total_monthly_costs = rental_property.calculate_total_monthly_costs()
monthly_cash_flow = rental_property.calculate_monthly_cash_flow()
cash_on_cash_roi = rental_property.calculate_cash_on_cash_roi()

# Print results from our variables plus to get the calculations above from line 40-44 2f represents numbers in two decimal points
print(f"Purchase price: ${purchase_price:.2f}")
print(f"Down payment: ${down_payment:.2f}")
print(f"Closing costs: ${closure_costs:.2f}")
print(f"Renovation expenses: ${renovation_costs:.2f}")
print(f"Monthly rental income: ${monthly_rental_income:.2f}")
print(f"Fixed expenses: ${fixed_costs:.2f}")
print(f"Variable expenses: ${variable_costs:.2f}")
print(f"Total monthly income: ${total_monthly_income:.2f}")
print(f"Total monthly expenses: ${total_monthly_costs:.2f}")
print(f"Monthly cash flow: ${monthly_cash_flow:.2f}")
print(f"Cash on cash return on investment: {cash_on_cash_roi:.2%}")