# Instructions
# - Given the “gross” salary of a person, calculate the “net”.
# Here are the constraints:
# 1.If the gross is less than 1000, then the income tax is 10%
# 2.If the gross is less than 2000, then the income tax is 12%
# 3.If the gross is less than 4000, then the income tax is 14%
# 4.If the gross is more than 4000, then the income tax is 18%
# 5.If the gross is less than 2000, every child gets you a tax cut of 1%
# 6.If the gross is more than 2000, every child gets you a tax cut of 0.5%
# Read the “gross” and the number of children
# Print the “net”
# Use try/except when reading the inputs '

print("Welcome to Lichtenberger Tax Advisory. Please answer the following questions, so we can create your tax report:")

try:
    gross_salary = float(input("What is your monthly gross salary? (0 Deicmals)"))
    no_kids = int(input("How many children do you have?"))
    if gross_salary < 1000:
        tax_rate = 0.1
    elif gross_salary < 2000:
        tax_rate = 0.12
    elif gross_salary < 4000:
        tax_rate = 0.14
    else:
        tax_rate = 0.18
    if gross_salary < 2000:
        tax_cut = 0.01 * no_kids
    else:
        tax_cut = 0.005 * no_kids
    real_tax_rate = max(tax_rate - tax_cut, 0)
    tax_amount = gross_salary*(real_tax_rate)
    net_salary = gross_salary - tax_amount
    print(f"Your tax rate is {real_tax_rate*100}%. You need to pay the IRS {tax_amount}$. Your monthly net salary is {net_salary}$.")
except ValueError:
    print("Please enter a valid number.")